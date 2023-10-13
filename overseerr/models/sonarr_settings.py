# coding: utf-8

"""
    Overseerr API

    This is the documentation for the Overseerr API backend.  Two primary authentication methods are supported:  - **Cookie Authentication**: A valid sign-in to the `/auth/plex` or `/auth/local` will generate a valid authentication cookie. - **API Key Authentication**: Sign-in is also possible by passing an `X-Api-Key` header along with a valid API Key generated by Overseerr.   # noqa: E501

    The version of the OpenAPI document: 1.0.0
    Generated by: https://openapi-generator.tech
"""


from __future__ import annotations
from inspect import getfullargspec
import pprint
import re  # noqa: F401
import json


from typing import Optional, Union
from pydantic import BaseModel

class SonarrSettings(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id: Optional[float]
    name: Optional[str]
    hostname: Optional[str]
    port: Optional[float]
    api_key: Optional[str]
    use_ssl: Optional[bool]
    base_url: Optional[str]
    active_profile_id: Optional[float]
    active_profile_name: Optional[str]
    active_directory: Optional[str]
    active_language_profile_id: Optional[float]
    active_anime_profile_id: Optional[float]
    active_anime_language_profile_id: Optional[float]
    active_anime_profile_name: Optional[str]
    active_anime_directory: Optional[str]
    is4k: Optional[bool]
    enable_season_folders: Optional[bool]
    is_default: Optional[bool]
    external_url: Optional[str]
    sync_enabled: Optional[bool]
    prevent_search: Optional[bool]
    additional_properties: Dict[str, Any] = {}
    __properties = ["id", "name", "hostname", "port", "apiKey", "useSsl", "baseUrl", "activeProfileId", "activeProfileName", "activeDirectory", "activeLanguageProfileId", "activeAnimeProfileId", "activeAnimeLanguageProfileId", "activeAnimeProfileName", "activeAnimeDirectory", "is4k", "enableSeasonFolders", "isDefault", "externalUrl", "syncEnabled", "preventSearch"]

    class Config:
        allow_population_by_field_name = True
        validate_assignment = True
        alias_generator = lambda x: x.split("_")[0] + "".join(word.capitalize() for word in x.split("_")[1:])

    def __getitem__(self, item):
        return getattr(self, item)

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> SonarrSettings:
        """Create an instance of SonarrSettings from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "id",
                            "additional_properties"
                          },
                          exclude_none=True)
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if active_anime_profile_id (nullable) is None
        if self.active_anime_profile_id is None:
            _dict['activeAnimeProfileId'] = None

        # set to None if active_anime_language_profile_id (nullable) is None
        if self.active_anime_language_profile_id is None:
            _dict['activeAnimeLanguageProfileId'] = None

        # set to None if active_anime_profile_name (nullable) is None
        if self.active_anime_profile_name is None:
            _dict['activeAnimeProfileName'] = None

        # set to None if active_anime_directory (nullable) is None
        if self.active_anime_directory is None:
            _dict['activeAnimeDirectory'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> SonarrSettings:
        """Create an instance of SonarrSettings from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return SonarrSettings.parse_obj(obj)

        _obj = SonarrSettings.parse_obj({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "hostname": obj.get("hostname"),
            "port": obj.get("port"),
            "api_key": obj.get("apiKey"),
            "use_ssl": obj.get("useSsl"),
            "base_url": obj.get("baseUrl"),
            "active_profile_id": obj.get("activeProfileId"),
            "active_profile_name": obj.get("activeProfileName"),
            "active_directory": obj.get("activeDirectory"),
            "active_language_profile_id": obj.get("activeLanguageProfileId"),
            "active_anime_profile_id": obj.get("activeAnimeProfileId"),
            "active_anime_language_profile_id": obj.get("activeAnimeLanguageProfileId"),
            "active_anime_profile_name": obj.get("activeAnimeProfileName"),
            "active_anime_directory": obj.get("activeAnimeDirectory"),
            "is4k": obj.get("is4k"),
            "enable_season_folders": obj.get("enableSeasonFolders"),
            "is_default": obj.get("isDefault"),
            "external_url": obj.get("externalUrl"),
            "sync_enabled": obj.get("syncEnabled"),
            "prevent_search": obj.get("preventSearch")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

