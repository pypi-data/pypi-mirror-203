#!/usr/bin/env python
# -*-coding:utf-8 -*-
'''
  ████
██    ██   Datature
  ██  ██   Powering Breakthrough AI
    ██

@File    :   config.py
@Author  :   Raighne.Weng
@Version :   0.7.1
@Contact :   raighne@datature.io
@License :   Apache License 2.0
@Desc    :   CLI config class
'''

import io
import sys
import base64
from pathlib import Path
from typing import Any, Dict, List, Optional, Union

import yaml
from datature.messages import INVALID_PROJECT_MESSAGE, NO_PROJECT_MESSAGE


class Config():
    """Handles YAML configuration files"""

    def __init__(self):
        """Init config file"""

        config_path = Path.home() / ".datature" / "config.yaml"
        config_path.parent.mkdir(exist_ok=True)

        self._path = config_path
        self._data = self._parse()

    def _parse(self) -> Dict[str, Any]:
        """Parses config from YAML configuration file"""

        if not self._path:
            return {}
        try:
            with open(self._path, "r", encoding="utf8") as stream:
                return yaml.safe_load(stream)
        except FileNotFoundError:
            return {}

    def _get(self, key: str, default: Optional[Any] = None) -> Dict[str, Any]:
        """Get JSON value from self._data """

        data: Any = self._data.copy()

        while True:
            if isinstance(key, str):
                key = key.split("/")
            key, *keys = key

            data = data.get(key)

            if data is None:
                return default
            if len(keys) == 0:
                return data
            key = keys

    def _save(self) -> None:
        """Persist the config to the file system"""

        if not self._path:
            return
        with io.open(self._path, "w", encoding="utf8") as config_file:
            yaml.dump(self._data,
                      config_file,
                      default_flow_style=False,
                      allow_unicode=True)

    def set(self,
            key: Union[str, List[str]],
            value: Any,
            save: bool = True) -> None:
        """
        Sets the value for the specified key.

        :param key: The key where the value is going to be stored.
        :param value: The value to be stored.
        :param save: If ``True``, persists the value in the FileSystem. Defaults to ``True``.
        :return: None
        """
        if isinstance(key, str):
            key = key.split("/")

        pointer = self._data

        for k in key[:-1]:
            pointer = pointer.setdefault(k, {})
        pointer[key[-1]] = str(value)

        if save:
            self._save()

    def set_project(self, project_id: str, project_name: str,
                    project_secret: str, default_project: bool) -> None:
        """
        Stores the project secret and project information.

        :param project_id: The id of the project.
        :param project_name: The name of the project.
        :param project_secret: The secret of the project.
        :param default_project: If set this project as the default project.
        :return: None
        """
        self.set(
            f"project/{project_id}/project_secret",
            base64.b64encode(project_secret.encode("ascii")).decode("ascii"))
        self.set(f"project/{project_id}/project_name", project_name)

        if default_project or len(self._get("project").keys()) == 1:
            self.set("default_project", project_id)

    def get_all_project_names(self) -> [str]:
        """
        list all saved projects name

        :return: [str]
        """
        projects = self._get("project")
        if projects is None:
            print(NO_PROJECT_MESSAGE)
            sys.exit(1)

        project_ids = projects.keys()
        projects = []

        for project_id in project_ids:
            projects.append(self._get(f"project/{project_id}/project_name"))

        return projects

    def get_default_project(self) -> dict:
        """
        list all saved projects

        :return: [str]
        """
        project_id = self._get("default_project")

        if project_id is None:
            print(NO_PROJECT_MESSAGE)
            sys.exit(1)

        return {
            "project_name":
            self._get(f"project/{project_id}/project_name"),
            "project_id":
            project_id,
            "project_secret":
            base64.b64decode(
                self._get(f"project/{project_id}/project_secret").encode(
                    'ascii')).decode('ascii'),
        }

    def set_default_project(self, project_id: str) -> None:
        """
        Set default project

        :param project_id: The id of the project.
        :return: None
        """
        self.set("default_project", project_id)

    def get_project(self, project_id: str) -> dict:
        """
        get selected project

        :param project_id: The id of the project.
        :return: dict
        """
        return self._get(f"project/{project_id}")

    def get_project_by_name(self, project_name: str) -> dict:
        """
        get project by project name

        :param project_name: The name of the project.
        :return: dict
        """
        project_ids = list(self._get("project").keys())

        for project_id in project_ids:
            if project_name == self._get(f"project/{project_id}/project_name"):
                return {
                    "project_name":
                    self._get(f"project/{project_id}/project_name"),
                    "project_id":
                    project_id,
                    "project_secret":
                    base64.b64decode(
                        self._get(f"project/{project_id}/project_secret").
                        encode('ascii')).decode('ascii'),
                }

        print(INVALID_PROJECT_MESSAGE)
        sys.exit(1)
