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
from overseerr.models.episode import Episode
from overseerr.models.external_ids import ExternalIds
from overseerr.models.genre import Genre
from overseerr.models.keyword import Keyword
from overseerr.models.media_info import MediaInfo
from overseerr.models.movie_details_credits import MovieDetailsCredits
from overseerr.models.movie_details_production_countries_inner import MovieDetailsProductionCountriesInner
from overseerr.models.production_company import ProductionCompany
from overseerr.models.season import Season
from overseerr.models.spoken_language import SpokenLanguage
from overseerr.models.tv_details_content_ratings import TvDetailsContentRatings
from overseerr.models.tv_details_created_by_inner import TvDetailsCreatedByInner
from overseerr.models.watch_providers_inner import WatchProvidersInner
from typing import Optional, Set
from typing_extensions import Self

class TvDetails(BaseModel):
    """
    TvDetails
    """ # noqa: E501
    id: Optional[Union[StrictFloat, StrictInt]] = None
    backdrop_path: Optional[StrictStr] = Field(default=None, alias="backdropPath")
    poster_path: Optional[StrictStr] = Field(default=None, alias="posterPath")
    content_ratings: Optional[TvDetailsContentRatings] = Field(default=None, alias="contentRatings")
    created_by: Optional[List[TvDetailsCreatedByInner]] = Field(default=None, alias="createdBy")
    episode_run_time: Optional[List[Union[StrictFloat, StrictInt]]] = Field(default=None, alias="episodeRunTime")
    first_air_date: Optional[StrictStr] = Field(default=None, alias="firstAirDate")
    genres: Optional[List[Genre]] = None
    homepage: Optional[StrictStr] = None
    in_production: Optional[StrictBool] = Field(default=None, alias="inProduction")
    languages: Optional[List[StrictStr]] = None
    last_air_date: Optional[StrictStr] = Field(default=None, alias="lastAirDate")
    last_episode_to_air: Optional[Episode] = Field(default=None, alias="lastEpisodeToAir")
    name: Optional[StrictStr] = None
    next_episode_to_air: Optional[Episode] = Field(default=None, alias="nextEpisodeToAir")
    networks: Optional[List[ProductionCompany]] = None
    number_of_episodes: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="numberOfEpisodes")
    number_of_season: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="numberOfSeason")
    origin_country: Optional[List[StrictStr]] = Field(default=None, alias="originCountry")
    original_language: Optional[StrictStr] = Field(default=None, alias="originalLanguage")
    original_name: Optional[StrictStr] = Field(default=None, alias="originalName")
    overview: Optional[StrictStr] = None
    popularity: Optional[Union[StrictFloat, StrictInt]] = None
    production_companies: Optional[List[ProductionCompany]] = Field(default=None, alias="productionCompanies")
    production_countries: Optional[List[MovieDetailsProductionCountriesInner]] = Field(default=None, alias="productionCountries")
    spoken_languages: Optional[List[SpokenLanguage]] = Field(default=None, alias="spokenLanguages")
    seasons: Optional[List[Season]] = None
    status: Optional[StrictStr] = None
    tagline: Optional[StrictStr] = None
    type: Optional[StrictStr] = None
    vote_average: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="voteAverage")
    vote_count: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="voteCount")
    credits: Optional[MovieDetailsCredits] = None
    external_ids: Optional[ExternalIds] = Field(default=None, alias="externalIds")
    keywords: Optional[List[Keyword]] = None
    media_info: Optional[MediaInfo] = Field(default=None, alias="mediaInfo")
    watch_providers: Optional[List[List[WatchProvidersInner]]] = Field(default=None, alias="watchProviders")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["id", "backdropPath", "posterPath", "contentRatings", "createdBy", "episodeRunTime", "firstAirDate", "genres", "homepage", "inProduction", "languages", "lastAirDate", "lastEpisodeToAir", "name", "nextEpisodeToAir", "networks", "numberOfEpisodes", "numberOfSeason", "originCountry", "originalLanguage", "originalName", "overview", "popularity", "productionCompanies", "productionCountries", "spokenLanguages", "seasons", "status", "tagline", "type", "voteAverage", "voteCount", "credits", "externalIds", "keywords", "mediaInfo", "watchProviders"]

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
        """Create an instance of TvDetails from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of content_ratings
        if self.content_ratings:
            _dict['contentRatings'] = self.content_ratings.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in created_by (list)
        _items = []
        if self.created_by:
            for _item_created_by in self.created_by:
                if _item_created_by:
                    _items.append(_item_created_by.to_dict())
            _dict['createdBy'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in genres (list)
        _items = []
        if self.genres:
            for _item_genres in self.genres:
                if _item_genres:
                    _items.append(_item_genres.to_dict())
            _dict['genres'] = _items
        # override the default output from pydantic by calling `to_dict()` of last_episode_to_air
        if self.last_episode_to_air:
            _dict['lastEpisodeToAir'] = self.last_episode_to_air.to_dict()
        # override the default output from pydantic by calling `to_dict()` of next_episode_to_air
        if self.next_episode_to_air:
            _dict['nextEpisodeToAir'] = self.next_episode_to_air.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in networks (list)
        _items = []
        if self.networks:
            for _item_networks in self.networks:
                if _item_networks:
                    _items.append(_item_networks.to_dict())
            _dict['networks'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in production_companies (list)
        _items = []
        if self.production_companies:
            for _item_production_companies in self.production_companies:
                if _item_production_companies:
                    _items.append(_item_production_companies.to_dict())
            _dict['productionCompanies'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in production_countries (list)
        _items = []
        if self.production_countries:
            for _item_production_countries in self.production_countries:
                if _item_production_countries:
                    _items.append(_item_production_countries.to_dict())
            _dict['productionCountries'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in spoken_languages (list)
        _items = []
        if self.spoken_languages:
            for _item_spoken_languages in self.spoken_languages:
                if _item_spoken_languages:
                    _items.append(_item_spoken_languages.to_dict())
            _dict['spokenLanguages'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in seasons (list)
        _items = []
        if self.seasons:
            for _item_seasons in self.seasons:
                if _item_seasons:
                    _items.append(_item_seasons.to_dict())
            _dict['seasons'] = _items
        # override the default output from pydantic by calling `to_dict()` of credits
        if self.credits:
            _dict['credits'] = self.credits.to_dict()
        # override the default output from pydantic by calling `to_dict()` of external_ids
        if self.external_ids:
            _dict['externalIds'] = self.external_ids.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in keywords (list)
        _items = []
        if self.keywords:
            for _item_keywords in self.keywords:
                if _item_keywords:
                    _items.append(_item_keywords.to_dict())
            _dict['keywords'] = _items
        # override the default output from pydantic by calling `to_dict()` of media_info
        if self.media_info:
            _dict['mediaInfo'] = self.media_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in watch_providers (list of list)
        _items = []
        if self.watch_providers:
            for _item_watch_providers in self.watch_providers:
                if _item_watch_providers:
                    _items.append(
                         [_inner_item.to_dict() for _inner_item in _item_watch_providers if _inner_item is not None]
                    )
            _dict['watchProviders'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TvDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "backdropPath": obj.get("backdropPath"),
            "posterPath": obj.get("posterPath"),
            "contentRatings": TvDetailsContentRatings.from_dict(obj["contentRatings"]) if obj.get("contentRatings") is not None else None,
            "createdBy": [TvDetailsCreatedByInner.from_dict(_item) for _item in obj["createdBy"]] if obj.get("createdBy") is not None else None,
            "episodeRunTime": obj.get("episodeRunTime"),
            "firstAirDate": obj.get("firstAirDate"),
            "genres": [Genre.from_dict(_item) for _item in obj["genres"]] if obj.get("genres") is not None else None,
            "homepage": obj.get("homepage"),
            "inProduction": obj.get("inProduction"),
            "languages": obj.get("languages"),
            "lastAirDate": obj.get("lastAirDate"),
            "lastEpisodeToAir": Episode.from_dict(obj["lastEpisodeToAir"]) if obj.get("lastEpisodeToAir") is not None else None,
            "name": obj.get("name"),
            "nextEpisodeToAir": Episode.from_dict(obj["nextEpisodeToAir"]) if obj.get("nextEpisodeToAir") is not None else None,
            "networks": [ProductionCompany.from_dict(_item) for _item in obj["networks"]] if obj.get("networks") is not None else None,
            "numberOfEpisodes": obj.get("numberOfEpisodes"),
            "numberOfSeason": obj.get("numberOfSeason"),
            "originCountry": obj.get("originCountry"),
            "originalLanguage": obj.get("originalLanguage"),
            "originalName": obj.get("originalName"),
            "overview": obj.get("overview"),
            "popularity": obj.get("popularity"),
            "productionCompanies": [ProductionCompany.from_dict(_item) for _item in obj["productionCompanies"]] if obj.get("productionCompanies") is not None else None,
            "productionCountries": [MovieDetailsProductionCountriesInner.from_dict(_item) for _item in obj["productionCountries"]] if obj.get("productionCountries") is not None else None,
            "spokenLanguages": [SpokenLanguage.from_dict(_item) for _item in obj["spokenLanguages"]] if obj.get("spokenLanguages") is not None else None,
            "seasons": [Season.from_dict(_item) for _item in obj["seasons"]] if obj.get("seasons") is not None else None,
            "status": obj.get("status"),
            "tagline": obj.get("tagline"),
            "type": obj.get("type"),
            "voteAverage": obj.get("voteAverage"),
            "voteCount": obj.get("voteCount"),
            "credits": MovieDetailsCredits.from_dict(obj["credits"]) if obj.get("credits") is not None else None,
            "externalIds": ExternalIds.from_dict(obj["externalIds"]) if obj.get("externalIds") is not None else None,
            "keywords": [Keyword.from_dict(_item) for _item in obj["keywords"]] if obj.get("keywords") is not None else None,
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


