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


from typing import Any, ClassVar, Dict, List, Optional, Union
from pydantic import BaseModel, validator

class UpdateRequestRequest(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    media_type: Optional[str]
    seasons: Optional[List]
    is4k: Optional[bool]
    server_id: Optional[float]
    profile_id: Optional[float]
    root_folder: Optional[str]
    language_profile_id: Optional[float]
    user_id: Optional[float]
    additional_properties: Dict[str, Any] = {}
    __properties = ["mediaType", "seasons", "is4k", "serverId", "profileId", "rootFolder", "languageProfileId", "userId"]

    @validator('media_type')
    def media_type_validate_enum(cls, v):
        if v not in ('movie', 'tv'):
            raise ValueError("must validate the enum values ('movie', 'tv')")
        return v

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
    def from_json(cls, json_str: str) -> UpdateRequestRequest:
        """Create an instance of UpdateRequestRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if user_id (nullable) is None
        if self.user_id is None:
            _dict['userId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> UpdateRequestRequest:
        """Create an instance of UpdateRequestRequest from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return UpdateRequestRequest.parse_obj(obj)

        _obj = UpdateRequestRequest.parse_obj({
            "media_type": obj.get("mediaType"),
            "seasons": obj.get("seasons"),
            "is4k": obj.get("is4k"),
            "server_id": obj.get("serverId"),
            "profile_id": obj.get("profileId"),
            "root_folder": obj.get("rootFolder"),
            "language_profile_id": obj.get("languageProfileId"),
            "user_id": obj.get("userId")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

