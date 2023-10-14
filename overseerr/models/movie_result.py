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


from typing import Any, Dict, List, Optional, Union
from pydantic import BaseModel
from overseerr.models.media_info import MediaInfo

class MovieResult(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id: Optional[float]
    media_type: Optional[str]
    popularity: Optional[float]
    poster_path: Optional[str]
    backdrop_path: Optional[str]
    vote_count: Optional[float]
    vote_average: Optional[float]
    genre_ids: Optional[List]
    overview: Optional[str]
    original_language: Optional[str]
    title: Optional[str]
    original_title: Optional[str]
    release_date: Optional[str]
    adult: Optional[bool]
    video: Optional[bool]
    media_info: Optional[MediaInfo]
    additional_properties: Dict[str, Any] = {}
    __properties = ["id", "mediaType", "popularity", "posterPath", "backdropPath", "voteCount", "voteAverage", "genreIds", "overview", "originalLanguage", "title", "originalTitle", "releaseDate", "adult", "video", "mediaInfo"]

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
    def from_json(cls, json_str: str) -> MovieResult:
        """Create an instance of MovieResult from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of media_info
        if self.media_info:
            _dict['mediaInfo'] = self.media_info.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MovieResult:
        """Create an instance of MovieResult from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return MovieResult.parse_obj(obj)

        _obj = MovieResult.parse_obj({
            "id": obj.get("id"),
            "media_type": obj.get("mediaType"),
            "popularity": obj.get("popularity"),
            "poster_path": obj.get("posterPath"),
            "backdrop_path": obj.get("backdropPath"),
            "vote_count": obj.get("voteCount"),
            "vote_average": obj.get("voteAverage"),
            "genre_ids": obj.get("genreIds"),
            "overview": obj.get("overview"),
            "original_language": obj.get("originalLanguage"),
            "title": obj.get("title"),
            "original_title": obj.get("originalTitle"),
            "release_date": obj.get("releaseDate"),
            "adult": obj.get("adult"),
            "video": obj.get("video"),
            "media_info": MediaInfo.from_dict(obj.get("mediaInfo")) if obj.get("mediaInfo") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

