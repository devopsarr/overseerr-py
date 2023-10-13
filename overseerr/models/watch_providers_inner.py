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


from typing import List, Optional
from pydantic import BaseModel
from overseerr.models.watch_provider_details import WatchProviderDetails

class WatchProvidersInner(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    iso_3166_1: Optional[str]
    link: Optional[str]
    buy: Optional[List]
    flatrate: Optional[List]
    additional_properties: Dict[str, Any] = {}
    __properties = ["iso_3166_1", "link", "buy", "flatrate"]

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
    def from_json(cls, json_str: str) -> WatchProvidersInner:
        """Create an instance of WatchProvidersInner from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in buy (list)
        _items = []
        if self.buy:
            for _item in self.buy:
                if _item:
                    _items.append(_item.to_dict())
            _dict['buy'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in flatrate (list)
        _items = []
        if self.flatrate:
            for _item in self.flatrate:
                if _item:
                    _items.append(_item.to_dict())
            _dict['flatrate'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> WatchProvidersInner:
        """Create an instance of WatchProvidersInner from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return WatchProvidersInner.parse_obj(obj)

        _obj = WatchProvidersInner.parse_obj({
            "iso_3166_1": obj.get("iso_3166_1"),
            "link": obj.get("link"),
            "buy": [WatchProviderDetails.from_dict(_item) for _item in obj.get("buy")] if obj.get("buy") is not None else None,
            "flatrate": [WatchProviderDetails.from_dict(_item) for _item in obj.get("flatrate")] if obj.get("flatrate") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

