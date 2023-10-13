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

class GetAbout200Response(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    version: Optional[str]
    total_requests: Optional[float]
    total_media_items: Optional[float]
    tz: Optional[str]
    app_data_path: Optional[str]
    additional_properties: Dict[str, Any] = {}
    __properties = ["version", "totalRequests", "totalMediaItems", "tz", "appDataPath"]

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
    def from_json(cls, json_str: str) -> GetAbout200Response:
        """Create an instance of GetAbout200Response from a JSON string"""
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

        # set to None if tz (nullable) is None
        if self.tz is None:
            _dict['tz'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GetAbout200Response:
        """Create an instance of GetAbout200Response from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return GetAbout200Response.parse_obj(obj)

        _obj = GetAbout200Response.parse_obj({
            "version": obj.get("version"),
            "total_requests": obj.get("totalRequests"),
            "total_media_items": obj.get("totalMediaItems"),
            "tz": obj.get("tz"),
            "app_data_path": obj.get("appDataPath")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

