# coding: utf-8

"""
    Overseerr API

    This is the documentation for the Overseerr API backend.  Two primary authentication methods are supported:  - **Cookie Authentication**: A valid sign-in to the `/auth/plex` or `/auth/local` will generate a valid authentication cookie. - **API Key Authentication**: Sign-in is also possible by passing an `X-Api-Key` header along with a valid API Key generated by Overseerr. 

    The version of the OpenAPI document: v1.33.2
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from overseerr.models.media_info import MediaInfo
from typing import Optional, Set
from typing_extensions import Self

class CreditCast(BaseModel):
    """
    CreditCast
    """ # noqa: E501
    id: Optional[Union[StrictFloat, StrictInt]] = None
    original_language: Optional[StrictStr] = Field(default=None, alias="originalLanguage")
    episode_count: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="episodeCount")
    overview: Optional[StrictStr] = None
    origin_country: Optional[List[StrictStr]] = Field(default=None, alias="originCountry")
    original_name: Optional[StrictStr] = Field(default=None, alias="originalName")
    vote_count: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="voteCount")
    name: Optional[StrictStr] = None
    media_type: Optional[StrictStr] = Field(default=None, alias="mediaType")
    popularity: Optional[Union[StrictFloat, StrictInt]] = None
    credit_id: Optional[StrictStr] = Field(default=None, alias="creditId")
    backdrop_path: Optional[StrictStr] = Field(default=None, alias="backdropPath")
    first_air_date: Optional[StrictStr] = Field(default=None, alias="firstAirDate")
    vote_average: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="voteAverage")
    genre_ids: Optional[List[Union[StrictFloat, StrictInt]]] = Field(default=None, alias="genreIds")
    poster_path: Optional[StrictStr] = Field(default=None, alias="posterPath")
    original_title: Optional[StrictStr] = Field(default=None, alias="originalTitle")
    video: Optional[StrictBool] = None
    title: Optional[StrictStr] = None
    adult: Optional[StrictBool] = None
    release_date: Optional[StrictStr] = Field(default=None, alias="releaseDate")
    character: Optional[StrictStr] = None
    media_info: Optional[MediaInfo] = Field(default=None, alias="mediaInfo")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["id", "originalLanguage", "episodeCount", "overview", "originCountry", "originalName", "voteCount", "name", "mediaType", "popularity", "creditId", "backdropPath", "firstAirDate", "voteAverage", "genreIds", "posterPath", "originalTitle", "video", "title", "adult", "releaseDate", "character", "mediaInfo"]

    model_config = {
        "populate_by_name": True,
        "validate_assignment": True,
        "protected_namespaces": (),
    }


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of CreditCast from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of media_info
        if self.media_info:
            _dict['mediaInfo'] = self.media_info.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CreditCast from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "originalLanguage": obj.get("originalLanguage"),
            "episodeCount": obj.get("episodeCount"),
            "overview": obj.get("overview"),
            "originCountry": obj.get("originCountry"),
            "originalName": obj.get("originalName"),
            "voteCount": obj.get("voteCount"),
            "name": obj.get("name"),
            "mediaType": obj.get("mediaType"),
            "popularity": obj.get("popularity"),
            "creditId": obj.get("creditId"),
            "backdropPath": obj.get("backdropPath"),
            "firstAirDate": obj.get("firstAirDate"),
            "voteAverage": obj.get("voteAverage"),
            "genreIds": obj.get("genreIds"),
            "posterPath": obj.get("posterPath"),
            "originalTitle": obj.get("originalTitle"),
            "video": obj.get("video"),
            "title": obj.get("title"),
            "adult": obj.get("adult"),
            "releaseDate": obj.get("releaseDate"),
            "character": obj.get("character"),
            "mediaInfo": MediaInfo.from_dict(obj["mediaInfo"]) if obj.get("mediaInfo") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


