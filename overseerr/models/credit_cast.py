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


from typing import List, Optional, Union
from pydantic import BaseModel
from overseerr.models.media_info import MediaInfo

class CreditCast(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id: Optional[float]
    original_language: Optional[str]
    episode_count: Optional[float]
    overview: Optional[str]
    origin_country: Optional[List]
    original_name: Optional[str]
    vote_count: Optional[float]
    name: Optional[str]
    media_type: Optional[str]
    popularity: Optional[float]
    credit_id: Optional[str]
    backdrop_path: Optional[str]
    first_air_date: Optional[str]
    vote_average: Optional[float]
    genre_ids: Optional[List]
    poster_path: Optional[str]
    original_title: Optional[str]
    video: Optional[bool]
    title: Optional[str]
    adult: Optional[bool]
    release_date: Optional[str]
    character: Optional[str]
    media_info: Optional[MediaInfo]
    additional_properties: Dict[str, Any] = {}
    __properties = ["id", "originalLanguage", "episodeCount", "overview", "originCountry", "originalName", "voteCount", "name", "mediaType", "popularity", "creditId", "backdropPath", "firstAirDate", "voteAverage", "genreIds", "posterPath", "originalTitle", "video", "title", "adult", "releaseDate", "character", "mediaInfo"]

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
    def from_json(cls, json_str: str) -> CreditCast:
        """Create an instance of CreditCast from a JSON string"""
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
    def from_dict(cls, obj: dict) -> CreditCast:
        """Create an instance of CreditCast from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return CreditCast.parse_obj(obj)

        _obj = CreditCast.parse_obj({
            "id": obj.get("id"),
            "original_language": obj.get("originalLanguage"),
            "episode_count": obj.get("episodeCount"),
            "overview": obj.get("overview"),
            "origin_country": obj.get("originCountry"),
            "original_name": obj.get("originalName"),
            "vote_count": obj.get("voteCount"),
            "name": obj.get("name"),
            "media_type": obj.get("mediaType"),
            "popularity": obj.get("popularity"),
            "credit_id": obj.get("creditId"),
            "backdrop_path": obj.get("backdropPath"),
            "first_air_date": obj.get("firstAirDate"),
            "vote_average": obj.get("voteAverage"),
            "genre_ids": obj.get("genreIds"),
            "poster_path": obj.get("posterPath"),
            "original_title": obj.get("originalTitle"),
            "video": obj.get("video"),
            "title": obj.get("title"),
            "adult": obj.get("adult"),
            "release_date": obj.get("releaseDate"),
            "character": obj.get("character"),
            "media_info": MediaInfo.from_dict(obj.get("mediaInfo")) if obj.get("mediaInfo") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

