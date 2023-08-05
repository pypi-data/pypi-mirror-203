#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
  ████
██    ██   Datature
  ██  ██   Powering Breakthrough AI
    ██

@File    :   upload_session.py
@Author  :   Raighne.Weng
@Version :   0.7.6
@Contact :   raighne@datature.io
@License :   Apache License 2.0
@Desc    :   Datature Asset Upload Session
'''

import json
import struct
from os import path
from pathlib import Path

import cv2
import google_crc32c
from requests import request
from filetype import filetype
from alive_progress import alive_bar

import datature
from datature.utils import utils
from datature import error, logger
from datature.http.resource import RESTResource
from datature.processor import get_processor
from datature.rest.operation import Operation


# pylint: disable=E1102,R0914,R0912
class UploadSession(RESTResource):
    """Datature Asset Upload Session Class."""

    def __init__(self):
        self.assets = []
        self.file_name_map = {}
        self.custom_metadata_map = {}
        project = datature.Project.retrieve()

        self.metadata_limit = utils.get_asset_metadata_limit_by_tier(
            project.get("tier", "free"))

    def add(self, file_path: str, custom_metadata: dict = None, **kwargs):
        """Add asset to upload."""
        if len(self.assets) >= datature.ASSET_UPLOAD_BATCH_SIZE:
            raise error.Error("One upload session allow max 5000 assets.")

        if not path.exists(file_path):
            raise error.Error("Cannot find the Asset file")

        # Prepare filename size and mime type
        filename = path.basename(file_path)

        # Convert DICOM and NII file to video asset
        if file_path.lower().endswith(('.dcm', '.nii')):
            processor = get_processor(file_path)

            process_data = {"file": file_path, "options": kwargs}
            processor.valid(process_data)
            resp = processor.process(process_data)

            if resp:
                # change the converted file_path and filename
                file_path = resp
                filename = Path(file_path).stem

        with open(file_path, 'rb') as file:
            contents = file.read()

            # calculate file crc32
            file_hash = google_crc32c.Checksum()
            file_hash.update(contents)

            # To fix the wrong crc32 caused by mac M1 clip
            crc32 = struct.unpack(">l", file_hash.digest())[0]

            size = path.getsize(file_path)

            mime_kind = filetype.guess(file_path)

            file.close()

            if self.file_name_map.get(filename) is not None:
                raise error.Error(
                    f"Cannot add multiple files with the same name, {filename}"
                )

            if (filename and size and crc32 and mime_kind):
                if mime_kind.mime in ["image/jpeg", "image/png"]:
                    asset_metadata = {
                        "filename": filename,
                        "size": size,
                        "crc32c": crc32,
                        "mime": mime_kind.mime
                    }
                elif mime_kind.mime == "video/mp4":
                    cap = cv2.VideoCapture(file_path)
                    frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
                    four_c_c = int(cap.get(cv2.CAP_PROP_FOURCC))
                    codec = chr(four_c_c
                                & 0xff) + chr((four_c_c >> 8) & 0xff) + chr(
                                    (four_c_c >> 16)
                                    & 0xff) + chr((four_c_c >> 24) & 0xff)
                    if not codec.startswith('avc1'):
                        raise error.Error("UnSupported asset file")

                    asset_metadata = {
                        "filename": filename,
                        "size": size,
                        "crc32c": crc32,
                        "mime": mime_kind.mime,
                        "frames": frames,
                        "encoder": {
                            "profile": "h264Saver",
                            "everyNthFrame": 1
                        },
                    }
                else:
                    raise error.Error("UnSupported asset file")

                self.assets.append(asset_metadata)
                self.file_name_map[filename] = {"path": file_path}

                if custom_metadata is not None:
                    if len(json.dumps(custom_metadata)) > self.metadata_limit:
                        raise error.Error(
                            f"Your tier only allow upload {self.metadata_limit} bytes metadata."
                        )

                    self.custom_metadata_map[filename] = custom_metadata

                logger.log_info("Add asset:", metadata=asset_metadata)
            else:
                raise error.Error("UnSupported asset file")

    def start(self, groups: [str] = None, background: bool = False) -> dict:
        """Request server to get signed ur and upload file to gcp."""

        # Set default groups
        if groups is None:
            groups = ["main"]

        # check asset length
        if not self.assets:
            raise error.Error("Assets to upload is empty")

        if self.custom_metadata_map and background:
            logger.log_info(
                "Warning: have custom metadata, force set background to False."
            )
            datature.SHOW_PROGRESS = False
            background = False

        # call API to get signed url
        response = self.request("POST",
                                "/asset/uploadSession",
                                request_body={
                                    "groups": groups,
                                    "assets": self.assets
                                })
        op_link = response["op_link"]

        if datature.SHOW_PROGRESS:
            with alive_bar(
                    len(response["assets"]),
                    title='Uploading',
                    title_length=12,
            ) as progress_bar:
                for asset_upload in response["assets"]:
                    file_name = asset_upload["metadata"]["filename"]
                    file_path = self.file_name_map.get(file_name)["path"]

                    with open(file_path, 'rb') as file:
                        contents = file.read()

                        # upload asset to GCP one by one
                        request("PUT",
                                asset_upload["upload"]["url"],
                                headers=asset_upload["upload"]["headers"],
                                data=contents,
                                timeout=10)
                    progress_bar()

            return {"op_link": op_link}

        for asset_upload in response["assets"]:
            file_name = asset_upload["metadata"]["filename"]
            file_path = self.file_name_map.get(file_name)["path"]

            with open(file_path, 'rb') as file:
                contents = file.read()

                logger.log_info("Start Uploading" + file_path)

                # upload asset to GCP one by one
                request("PUT",
                        asset_upload["upload"]["url"],
                        headers=asset_upload["upload"]["headers"],
                        data=contents,
                        timeout=10)
                logger.log_info("Done Uploading" + file_path)

        if background:
            return {"op_link": op_link}

        # Wait server finish generate thumbnail
        Operation.loop_retrieve(op_link)

        # Update custom_metadata
        for filename in self.custom_metadata_map:
            datature.Asset.modify(filename, {
                "custom_metadata":
                self.custom_metadata_map.get(filename, {})
            })

        return {"op_link": op_link}
