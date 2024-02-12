# coding: utf-8

"""
    Overseerr API

    This is the documentation for the Overseerr API backend.  Two primary authentication methods are supported:  - **Cookie Authentication**: A valid sign-in to the `/auth/plex` or `/auth/local` will generate a valid authentication cookie. - **API Key Authentication**: Sign-in is also possible by passing an `X-Api-Key` header along with a valid API Key generated by Overseerr. 

    The version of the OpenAPI document: 1.0.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from overseerr.models.external_ids import ExternalIds
from overseerr.models.genre import Genre
from overseerr.models.media_info import MediaInfo
from overseerr.models.movie_details_collection import MovieDetailsCollection
from overseerr.models.movie_details_credits import MovieDetailsCredits
from overseerr.models.movie_details_production_countries_inner import MovieDetailsProductionCountriesInner
from overseerr.models.movie_details_releases import MovieDetailsReleases
from overseerr.models.production_company import ProductionCompany
from overseerr.models.related_video import RelatedVideo
from overseerr.models.spoken_language import SpokenLanguage
from overseerr.models.watch_providers_inner import WatchProvidersInner
from typing import Optional, Set
from typing_extensions import Self

class MovieDetails(BaseModel):
    """
    MovieDetails
    """ # noqa: E501
    id: Optional[Union[StrictFloat, StrictInt]] = None
    imdb_id: Optional[StrictStr] = Field(default=None, alias="imdbId")
    adult: Optional[StrictBool] = None
    backdrop_path: Optional[StrictStr] = Field(default=None, alias="backdropPath")
    poster_path: Optional[StrictStr] = Field(default=None, alias="posterPath")
    budget: Optional[Union[StrictFloat, StrictInt]] = None
    genres: Optional[List[Genre]] = None
    homepage: Optional[StrictStr] = None
    related_videos: Optional[List[RelatedVideo]] = Field(default=None, alias="relatedVideos")
    original_language: Optional[StrictStr] = Field(default=None, alias="originalLanguage")
    original_title: Optional[StrictStr] = Field(default=None, alias="originalTitle")
    overview: Optional[StrictStr] = None
    popularity: Optional[Union[StrictFloat, StrictInt]] = None
    production_companies: Optional[List[ProductionCompany]] = Field(default=None, alias="productionCompanies")
    production_countries: Optional[List[MovieDetailsProductionCountriesInner]] = Field(default=None, alias="productionCountries")
    release_date: Optional[StrictStr] = Field(default=None, alias="releaseDate")
    releases: Optional[MovieDetailsReleases] = None
    revenue: Optional[Union[StrictFloat, StrictInt]] = None
    runtime: Optional[Union[StrictFloat, StrictInt]] = None
    spoken_languages: Optional[List[SpokenLanguage]] = Field(default=None, alias="spokenLanguages")
    status: Optional[StrictStr] = None
    tagline: Optional[StrictStr] = None
    title: Optional[StrictStr] = None
    video: Optional[StrictBool] = None
    vote_average: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="voteAverage")
    vote_count: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="voteCount")
    credits: Optional[MovieDetailsCredits] = None
    collection: Optional[MovieDetailsCollection] = None
    external_ids: Optional[ExternalIds] = Field(default=None, alias="externalIds")
    media_info: Optional[MediaInfo] = Field(default=None, alias="mediaInfo")
    watch_providers: Optional[List[List[WatchProvidersInner]]] = Field(default=None, alias="watchProviders")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["id", "imdbId", "adult", "backdropPath", "posterPath", "budget", "genres", "homepage", "relatedVideos", "originalLanguage", "originalTitle", "overview", "popularity", "productionCompanies", "productionCountries", "releaseDate", "releases", "revenue", "runtime", "spokenLanguages", "status", "tagline", "title", "video", "voteAverage", "voteCount", "credits", "collection", "externalIds", "mediaInfo", "watchProviders"]

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
        """Create an instance of MovieDetails from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "id",
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in genres (list)
        _items = []
        if self.genres:
            for _item in self.genres:
                if _item:
                    _items.append(_item.to_dict())
            _dict['genres'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in related_videos (list)
        _items = []
        if self.related_videos:
            for _item in self.related_videos:
                if _item:
                    _items.append(_item.to_dict())
            _dict['relatedVideos'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in production_companies (list)
        _items = []
        if self.production_companies:
            for _item in self.production_companies:
                if _item:
                    _items.append(_item.to_dict())
            _dict['productionCompanies'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in production_countries (list)
        _items = []
        if self.production_countries:
            for _item in self.production_countries:
                if _item:
                    _items.append(_item.to_dict())
            _dict['productionCountries'] = _items
        # override the default output from pydantic by calling `to_dict()` of releases
        if self.releases:
            _dict['releases'] = self.releases.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in spoken_languages (list)
        _items = []
        if self.spoken_languages:
            for _item in self.spoken_languages:
                if _item:
                    _items.append(_item.to_dict())
            _dict['spokenLanguages'] = _items
        # override the default output from pydantic by calling `to_dict()` of credits
        if self.credits:
            _dict['credits'] = self.credits.to_dict()
        # override the default output from pydantic by calling `to_dict()` of collection
        if self.collection:
            _dict['collection'] = self.collection.to_dict()
        # override the default output from pydantic by calling `to_dict()` of external_ids
        if self.external_ids:
            _dict['externalIds'] = self.external_ids.to_dict()
        # override the default output from pydantic by calling `to_dict()` of media_info
        if self.media_info:
            _dict['mediaInfo'] = self.media_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in watch_providers (list of list)
        _items = []
        if self.watch_providers:
            for _item in self.watch_providers:
                if _item:
                    _items.append(
                         [_inner_item.to_dict() for _inner_item in _item if _inner_item is not None]
                    )
            _dict['watchProviders'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if revenue (nullable) is None
        # and model_fields_set contains the field
        if self.revenue is None and "revenue" in self.model_fields_set:
            _dict['revenue'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MovieDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "imdbId": obj.get("imdbId"),
            "adult": obj.get("adult"),
            "backdropPath": obj.get("backdropPath"),
            "posterPath": obj.get("posterPath"),
            "budget": obj.get("budget"),
            "genres": [Genre.from_dict(_item) for _item in obj["genres"]] if obj.get("genres") is not None else None,
            "homepage": obj.get("homepage"),
            "relatedVideos": [RelatedVideo.from_dict(_item) for _item in obj["relatedVideos"]] if obj.get("relatedVideos") is not None else None,
            "originalLanguage": obj.get("originalLanguage"),
            "originalTitle": obj.get("originalTitle"),
            "overview": obj.get("overview"),
            "popularity": obj.get("popularity"),
            "productionCompanies": [ProductionCompany.from_dict(_item) for _item in obj["productionCompanies"]] if obj.get("productionCompanies") is not None else None,
            "productionCountries": [MovieDetailsProductionCountriesInner.from_dict(_item) for _item in obj["productionCountries"]] if obj.get("productionCountries") is not None else None,
            "releaseDate": obj.get("releaseDate"),
            "releases": MovieDetailsReleases.from_dict(obj["releases"]) if obj.get("releases") is not None else None,
            "revenue": obj.get("revenue"),
            "runtime": obj.get("runtime"),
            "spokenLanguages": [SpokenLanguage.from_dict(_item) for _item in obj["spokenLanguages"]] if obj.get("spokenLanguages") is not None else None,
            "status": obj.get("status"),
            "tagline": obj.get("tagline"),
            "title": obj.get("title"),
            "video": obj.get("video"),
            "voteAverage": obj.get("voteAverage"),
            "voteCount": obj.get("voteCount"),
            "credits": MovieDetailsCredits.from_dict(obj["credits"]) if obj.get("credits") is not None else None,
            "collection": MovieDetailsCollection.from_dict(obj["collection"]) if obj.get("collection") is not None else None,
            "externalIds": ExternalIds.from_dict(obj["externalIds"]) if obj.get("externalIds") is not None else None,
            "mediaInfo": MediaInfo.from_dict(obj["mediaInfo"]) if obj.get("mediaInfo") is not None else None,
            "watchProviders": [
                    [WatchProvidersInner.from_dict(_inner_item) for _inner_item in _item]
                    for _item in obj["watchProviders"]
                ] if obj.get("watchProviders") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


