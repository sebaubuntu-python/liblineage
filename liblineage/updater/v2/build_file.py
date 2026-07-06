#
# SPDX-FileCopyrightText: The LineageOS Project
# SPDX-License-Identifier: LGPL-3.0-or-later
#

from datetime import datetime
from typing import Any, Dict, Optional


class BuildFile:
    """LineageOS device build files informations.

    Attributes:
    - filename (str): The filename of the file
    - filepath (str): The filepath of the file in the server
    - sha1 (str): The SHA1 hash of the file
    - sha256 (str): The SHA256 hash of the file
    - size (int): The size of the file, in bytes
    - url (str): The URL to download the file
    """

    def __init__(
        self,
        date: Optional[str],
        datetime: Optional[datetime],
        filename: str,
        filepath: str,
        os_patch_level: Optional[str],
        os_sdk_level: Optional[int],
        ota_property_files: Optional[str],
        sha1: str,
        sha256: str,
        size: int,
        build_type: Optional[str],
        url: str,
    ) -> None:
        self.date = date
        self.datetime = datetime
        self.filename = filename
        self.filepath = filepath
        self.os_patch_level = os_patch_level
        self.os_sdk_level = os_sdk_level
        self.ota_property_files = ota_property_files
        self.sha1 = sha1
        self.sha256 = sha256
        self.size = size
        self.build_type = build_type
        self.url = url

    @classmethod
    def from_json(cls, json: Dict[str, Any]):
        """Create an object from a JSON object."""
        return cls(
            json.get("date"),
            datetime.fromtimestamp(json["datetime"]) if json.get("datetime") else None,
            json["filename"],
            json["filepath"],
            json.get("os_patch_level"),
            json.get("os_sdk_level"),
            json.get("ota_property_files"),
            json["sha1"],
            json["sha256"],
            json["size"],
            json.get("type"),
            json["url"],
        )
