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
from pydantic import BaseModel

class ExternalIds(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    facebook_id: Optional[str]
    freebase_id: Optional[str]
    freebase_mid: Optional[str]
    imdb_id: Optional[str]
    instagram_id: Optional[str]
    tvdb_id: Optional[float]
    tvrage_id: Optional[float]
    twitter_id: Optional[str]
    additional_properties: Dict[str, Any] = {}
    __properties = ["facebookId", "freebaseId", "freebaseMid", "imdbId", "instagramId", "tvdbId", "tvrageId", "twitterId"]

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
    def from_json(cls, json_str: str) -> ExternalIds:
        """Create an instance of ExternalIds from a JSON string"""
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

        # set to None if facebook_id (nullable) is None
        if self.facebook_id is None:
            _dict['facebookId'] = None

        # set to None if freebase_id (nullable) is None
        if self.freebase_id is None:
            _dict['freebaseId'] = None

        # set to None if freebase_mid (nullable) is None
        if self.freebase_mid is None:
            _dict['freebaseMid'] = None

        # set to None if imdb_id (nullable) is None
        if self.imdb_id is None:
            _dict['imdbId'] = None

        # set to None if instagram_id (nullable) is None
        if self.instagram_id is None:
            _dict['instagramId'] = None

        # set to None if tvdb_id (nullable) is None
        if self.tvdb_id is None:
            _dict['tvdbId'] = None

        # set to None if tvrage_id (nullable) is None
        if self.tvrage_id is None:
            _dict['tvrageId'] = None

        # set to None if twitter_id (nullable) is None
        if self.twitter_id is None:
            _dict['twitterId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> ExternalIds:
        """Create an instance of ExternalIds from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return ExternalIds.parse_obj(obj)

        _obj = ExternalIds.parse_obj({
            "facebook_id": obj.get("facebookId"),
            "freebase_id": obj.get("freebaseId"),
            "freebase_mid": obj.get("freebaseMid"),
            "imdb_id": obj.get("imdbId"),
            "instagram_id": obj.get("instagramId"),
            "tvdb_id": obj.get("tvdbId"),
            "tvrage_id": obj.get("tvrageId"),
            "twitter_id": obj.get("twitterId")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

