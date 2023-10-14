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


from typing import Any, Dict, Optional, Union
from pydantic import BaseModel

class TautulliSettings(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    hostname: Optional[str]
    port: Optional[float]
    use_ssl: Optional[bool]
    api_key: Optional[str]
    external_url: Optional[str]
    additional_properties: Dict[str, Any] = {}
    __properties = ["hostname", "port", "useSsl", "apiKey", "externalUrl"]

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
    def from_json(cls, json_str: str) -> TautulliSettings:
        """Create an instance of TautulliSettings from a JSON string"""
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

        # set to None if hostname (nullable) is None
        if self.hostname is None:
            _dict['hostname'] = None

        # set to None if port (nullable) is None
        if self.port is None:
            _dict['port'] = None

        # set to None if use_ssl (nullable) is None
        if self.use_ssl is None:
            _dict['useSsl'] = None

        # set to None if api_key (nullable) is None
        if self.api_key is None:
            _dict['apiKey'] = None

        # set to None if external_url (nullable) is None
        if self.external_url is None:
            _dict['externalUrl'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> TautulliSettings:
        """Create an instance of TautulliSettings from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return TautulliSettings.parse_obj(obj)

        _obj = TautulliSettings.parse_obj({
            "hostname": obj.get("hostname"),
            "port": obj.get("port"),
            "use_ssl": obj.get("useSsl"),
            "api_key": obj.get("apiKey"),
            "external_url": obj.get("externalUrl")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

