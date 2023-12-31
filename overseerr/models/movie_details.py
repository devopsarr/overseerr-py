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

class MovieDetails(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id: Optional[float]
    imdb_id: Optional[str]
    adult: Optional[bool]
    backdrop_path: Optional[str]
    poster_path: Optional[str]
    budget: Optional[float]
    genres: Optional[List]
    homepage: Optional[str]
    related_videos: Optional[List]
    original_language: Optional[str]
    original_title: Optional[str]
    overview: Optional[str]
    popularity: Optional[float]
    production_companies: Optional[List]
    production_countries: Optional[List]
    release_date: Optional[str]
    releases: Optional[MovieDetailsReleases]
    revenue: Optional[float]
    runtime: Optional[float]
    spoken_languages: Optional[List]
    status: Optional[str]
    tagline: Optional[str]
    title: Optional[str]
    video: Optional[bool]
    vote_average: Optional[float]
    vote_count: Optional[float]
    credits: Optional[MovieDetailsCredits]
    collection: Optional[MovieDetailsCollection]
    external_ids: Optional[ExternalIds]
    media_info: Optional[MediaInfo]
    watch_providers: Optional[List]
    additional_properties: Dict[str, Any] = {}
    __properties = ["id", "imdbId", "adult", "backdropPath", "posterPath", "budget", "genres", "homepage", "relatedVideos", "originalLanguage", "originalTitle", "overview", "popularity", "productionCompanies", "productionCountries", "releaseDate", "releases", "revenue", "runtime", "spokenLanguages", "status", "tagline", "title", "video", "voteAverage", "voteCount", "credits", "collection", "externalIds", "mediaInfo", "watchProviders"]

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
    def from_json(cls, json_str: str) -> MovieDetails:
        """Create an instance of MovieDetails from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "id",
                            "additional_properties"
                          },
                          exclude_none=True)
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
        # override the default output from pydantic by calling `to_dict()` of each item in watch_providers (list)
        _items = []
        if self.watch_providers:
            for _item in self.watch_providers:
                if _item:
                    _items.append(_item.to_dict())
            _dict['watchProviders'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if revenue (nullable) is None
        if self.revenue is None:
            _dict['revenue'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MovieDetails:
        """Create an instance of MovieDetails from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return MovieDetails.parse_obj(obj)

        _obj = MovieDetails.parse_obj({
            "id": obj.get("id"),
            "imdb_id": obj.get("imdbId"),
            "adult": obj.get("adult"),
            "backdrop_path": obj.get("backdropPath"),
            "poster_path": obj.get("posterPath"),
            "budget": obj.get("budget"),
            "genres": [Genre.from_dict(_item) for _item in obj.get("genres")] if obj.get("genres") is not None else None,
            "homepage": obj.get("homepage"),
            "related_videos": [RelatedVideo.from_dict(_item) for _item in obj.get("relatedVideos")] if obj.get("relatedVideos") is not None else None,
            "original_language": obj.get("originalLanguage"),
            "original_title": obj.get("originalTitle"),
            "overview": obj.get("overview"),
            "popularity": obj.get("popularity"),
            "production_companies": [ProductionCompany.from_dict(_item) for _item in obj.get("productionCompanies")] if obj.get("productionCompanies") is not None else None,
            "production_countries": [MovieDetailsProductionCountriesInner.from_dict(_item) for _item in obj.get("productionCountries")] if obj.get("productionCountries") is not None else None,
            "release_date": obj.get("releaseDate"),
            "releases": MovieDetailsReleases.from_dict(obj.get("releases")) if obj.get("releases") is not None else None,
            "revenue": obj.get("revenue"),
            "runtime": obj.get("runtime"),
            "spoken_languages": [SpokenLanguage.from_dict(_item) for _item in obj.get("spokenLanguages")] if obj.get("spokenLanguages") is not None else None,
            "status": obj.get("status"),
            "tagline": obj.get("tagline"),
            "title": obj.get("title"),
            "video": obj.get("video"),
            "vote_average": obj.get("voteAverage"),
            "vote_count": obj.get("voteCount"),
            "credits": MovieDetailsCredits.from_dict(obj.get("credits")) if obj.get("credits") is not None else None,
            "collection": MovieDetailsCollection.from_dict(obj.get("collection")) if obj.get("collection") is not None else None,
            "external_ids": ExternalIds.from_dict(obj.get("externalIds")) if obj.get("externalIds") is not None else None,
            "media_info": MediaInfo.from_dict(obj.get("mediaInfo")) if obj.get("mediaInfo") is not None else None,
            "watch_providers": [List[WatchProvidersInner].from_dict(_item) for _item in obj.get("watchProviders")] if obj.get("watchProviders") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

