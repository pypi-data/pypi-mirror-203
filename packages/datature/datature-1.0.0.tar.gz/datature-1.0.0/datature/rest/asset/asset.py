#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
  ████
██    ██   Datature
  ██  ██   Powering Breakthrough AI
    ██

@File    :   asset.py
@Author  :   Raighne.Weng
@Version :   0.7.6
@Contact :   raighne@datature.io
@License :   Apache License 2.0
@Desc    :   Datature Asset API
'''

from datature.http.resource import RESTResource
from datature.rest.asset.upload_session import UploadSession
from datature.rest.types import AssetMetadata, Pagination


class Asset(RESTResource):
    """Datature Annotation API Resource."""

    @classmethod
    def list(cls, pagination: Pagination = None) -> dict:
        """Get a list of assets

        :param pagination: the pagination of return list
        :return: response json data
        """
        return cls.request("GET", "/asset/list", query=pagination)

    @classmethod
    def retrieve(cls, asset_id_or_name: str) -> dict:
        """Get an asset

        :param asset_id_or_name: the id or name of the asset
        :return: response json data
        """
        return cls.request("GET", f"/asset/{asset_id_or_name}")

    @classmethod
    def modify(cls, asset_id_or_name: str, asset_meta: AssetMetadata) -> dict:
        """Update an asset

        :param asset_id_or_name: the id or name of the asset
        :param asset_meta: the metadata of asset
        :return: response json data
        """
        request_body = {}
        if asset_meta.get("status") is not None:
            request_body["status"] = asset_meta.get("status")

        if asset_meta.get("custom_metadata") is not None:
            request_body["customMetadata"] = asset_meta.get("custom_metadata")

        return cls.request("PUT",
                           f"/asset/{asset_id_or_name}",
                           request_body=request_body)

    @classmethod
    def delete(cls, asset_id_or_name: str) -> dict:
        """Delete a asset

        :param asset_id_or_name: the id or name of the asset
        :return: response json data
        """
        return cls.request("DELETE", f"/asset/{asset_id_or_name}")

    @classmethod
    def upload_session(cls) -> dict:
        """Bulk update assets

        :return: UploadSession class
        """
        return UploadSession()

    @classmethod
    def group(cls, group: str = None) -> dict:
        """Retrieve assets groups

        :param group: the name of group
        :return: response json data
        """
        return cls.request("GET", "/asset/group", query={"group": group})
