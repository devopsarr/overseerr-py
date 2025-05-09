# coding: utf-8

"""
    Overseerr API

    This is the documentation for the Overseerr API backend.  Two primary authentication methods are supported:  - **Cookie Authentication**: A valid sign-in to the `/auth/plex` or `/auth/local` will generate a valid authentication cookie. - **API Key Authentication**: Sign-in is also possible by passing an `X-Api-Key` header along with a valid API Key generated by Overseerr. 

    The version of the OpenAPI document: v1.34.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from overseerr.models.sonarr_series_add_options_inner import SonarrSeriesAddOptionsInner
from overseerr.models.sonarr_series_images_inner import SonarrSeriesImagesInner
from overseerr.models.sonarr_series_ratings_inner import SonarrSeriesRatingsInner
from overseerr.models.sonarr_series_seasons_inner import SonarrSeriesSeasonsInner
from typing import Optional, Set
from typing_extensions import Self

class SonarrSeries(BaseModel):
    """
    SonarrSeries
    """ # noqa: E501
    title: Optional[StrictStr] = None
    sort_title: Optional[StrictStr] = Field(default=None, alias="sortTitle")
    season_count: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="seasonCount")
    status: Optional[StrictStr] = None
    overview: Optional[StrictStr] = None
    network: Optional[StrictStr] = None
    air_time: Optional[StrictStr] = Field(default=None, alias="airTime")
    images: Optional[List[SonarrSeriesImagesInner]] = None
    remote_poster: Optional[StrictStr] = Field(default=None, alias="remotePoster")
    seasons: Optional[List[SonarrSeriesSeasonsInner]] = None
    year: Optional[Union[StrictFloat, StrictInt]] = None
    path: Optional[StrictStr] = None
    profile_id: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="profileId")
    language_profile_id: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="languageProfileId")
    season_folder: Optional[StrictBool] = Field(default=None, alias="seasonFolder")
    monitored: Optional[StrictBool] = None
    use_scene_numbering: Optional[StrictBool] = Field(default=None, alias="useSceneNumbering")
    runtime: Optional[Union[StrictFloat, StrictInt]] = None
    tvdb_id: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="tvdbId")
    tv_rage_id: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="tvRageId")
    tv_maze_id: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="tvMazeId")
    first_aired: Optional[StrictStr] = Field(default=None, alias="firstAired")
    last_info_sync: Optional[StrictStr] = Field(default=None, alias="lastInfoSync")
    series_type: Optional[StrictStr] = Field(default=None, alias="seriesType")
    clean_title: Optional[StrictStr] = Field(default=None, alias="cleanTitle")
    imdb_id: Optional[StrictStr] = Field(default=None, alias="imdbId")
    title_slug: Optional[StrictStr] = Field(default=None, alias="titleSlug")
    certification: Optional[StrictStr] = None
    genres: Optional[List[StrictStr]] = None
    tags: Optional[List[StrictStr]] = None
    added: Optional[StrictStr] = None
    ratings: Optional[List[SonarrSeriesRatingsInner]] = None
    quality_profile_id: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="qualityProfileId")
    id: Optional[Union[StrictFloat, StrictInt]] = None
    root_folder_path: Optional[StrictStr] = Field(default=None, alias="rootFolderPath")
    add_options: Optional[List[SonarrSeriesAddOptionsInner]] = Field(default=None, alias="addOptions")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["title", "sortTitle", "seasonCount", "status", "overview", "network", "airTime", "images", "remotePoster", "seasons", "year", "path", "profileId", "languageProfileId", "seasonFolder", "monitored", "useSceneNumbering", "runtime", "tvdbId", "tvRageId", "tvMazeId", "firstAired", "lastInfoSync", "seriesType", "cleanTitle", "imdbId", "titleSlug", "certification", "genres", "tags", "added", "ratings", "qualityProfileId", "id", "rootFolderPath", "addOptions"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of SonarrSeries from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in images (list)
        _items = []
        if self.images:
            for _item_images in self.images:
                if _item_images:
                    _items.append(_item_images.to_dict())
            _dict['images'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in seasons (list)
        _items = []
        if self.seasons:
            for _item_seasons in self.seasons:
                if _item_seasons:
                    _items.append(_item_seasons.to_dict())
            _dict['seasons'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in ratings (list)
        _items = []
        if self.ratings:
            for _item_ratings in self.ratings:
                if _item_ratings:
                    _items.append(_item_ratings.to_dict())
            _dict['ratings'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in add_options (list)
        _items = []
        if self.add_options:
            for _item_add_options in self.add_options:
                if _item_add_options:
                    _items.append(_item_add_options.to_dict())
            _dict['addOptions'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if last_info_sync (nullable) is None
        # and model_fields_set contains the field
        if self.last_info_sync is None and "last_info_sync" in self.model_fields_set:
            _dict['lastInfoSync'] = None

        # set to None if id (nullable) is None
        # and model_fields_set contains the field
        if self.id is None and "id" in self.model_fields_set:
            _dict['id'] = None

        # set to None if root_folder_path (nullable) is None
        # and model_fields_set contains the field
        if self.root_folder_path is None and "root_folder_path" in self.model_fields_set:
            _dict['rootFolderPath'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SonarrSeries from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "title": obj.get("title"),
            "sortTitle": obj.get("sortTitle"),
            "seasonCount": obj.get("seasonCount"),
            "status": obj.get("status"),
            "overview": obj.get("overview"),
            "network": obj.get("network"),
            "airTime": obj.get("airTime"),
            "images": [SonarrSeriesImagesInner.from_dict(_item) for _item in obj["images"]] if obj.get("images") is not None else None,
            "remotePoster": obj.get("remotePoster"),
            "seasons": [SonarrSeriesSeasonsInner.from_dict(_item) for _item in obj["seasons"]] if obj.get("seasons") is not None else None,
            "year": obj.get("year"),
            "path": obj.get("path"),
            "profileId": obj.get("profileId"),
            "languageProfileId": obj.get("languageProfileId"),
            "seasonFolder": obj.get("seasonFolder"),
            "monitored": obj.get("monitored"),
            "useSceneNumbering": obj.get("useSceneNumbering"),
            "runtime": obj.get("runtime"),
            "tvdbId": obj.get("tvdbId"),
            "tvRageId": obj.get("tvRageId"),
            "tvMazeId": obj.get("tvMazeId"),
            "firstAired": obj.get("firstAired"),
            "lastInfoSync": obj.get("lastInfoSync"),
            "seriesType": obj.get("seriesType"),
            "cleanTitle": obj.get("cleanTitle"),
            "imdbId": obj.get("imdbId"),
            "titleSlug": obj.get("titleSlug"),
            "certification": obj.get("certification"),
            "genres": obj.get("genres"),
            "tags": obj.get("tags"),
            "added": obj.get("added"),
            "ratings": [SonarrSeriesRatingsInner.from_dict(_item) for _item in obj["ratings"]] if obj.get("ratings") is not None else None,
            "qualityProfileId": obj.get("qualityProfileId"),
            "id": obj.get("id"),
            "rootFolderPath": obj.get("rootFolderPath"),
            "addOptions": [SonarrSeriesAddOptionsInner.from_dict(_item) for _item in obj["addOptions"]] if obj.get("addOptions") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


