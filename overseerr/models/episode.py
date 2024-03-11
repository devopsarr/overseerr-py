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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class Episode(BaseModel):
    """
    Episode
    """ # noqa: E501
    id: Optional[Union[StrictFloat, StrictInt]] = None
    name: Optional[StrictStr] = None
    air_date: Optional[StrictStr] = Field(default=None, alias="airDate")
    episode_number: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="episodeNumber")
    overview: Optional[StrictStr] = None
    production_code: Optional[StrictStr] = Field(default=None, alias="productionCode")
    season_number: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="seasonNumber")
    show_id: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="showId")
    still_path: Optional[StrictStr] = Field(default=None, alias="stillPath")
    vote_average: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="voteAverage")
    vote_count: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="voteCount")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["id", "name", "airDate", "episodeNumber", "overview", "productionCode", "seasonNumber", "showId", "stillPath", "voteAverage", "voteCount"]

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
        """Create an instance of Episode from a JSON string"""
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
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        # set to None if air_date (nullable) is None
        # and model_fields_set contains the field
        if self.air_date is None and "air_date" in self.model_fields_set:
            _dict['airDate'] = None

        # set to None if still_path (nullable) is None
        # and model_fields_set contains the field
        if self.still_path is None and "still_path" in self.model_fields_set:
            _dict['stillPath'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Episode from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "name": obj.get("name"),
            "airDate": obj.get("airDate"),
            "episodeNumber": obj.get("episodeNumber"),
            "overview": obj.get("overview"),
            "productionCode": obj.get("productionCode"),
            "seasonNumber": obj.get("seasonNumber"),
            "showId": obj.get("showId"),
            "stillPath": obj.get("stillPath"),
            "voteAverage": obj.get("voteAverage"),
            "voteCount": obj.get("voteCount")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


