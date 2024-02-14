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

from pydantic import BaseModel, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class ExternalIds(BaseModel):
    """
    ExternalIds
    """ # noqa: E501
    facebook_id: Optional[StrictStr] = Field(default=None, alias="facebookId")
    freebase_id: Optional[StrictStr] = Field(default=None, alias="freebaseId")
    freebase_mid: Optional[StrictStr] = Field(default=None, alias="freebaseMid")
    imdb_id: Optional[StrictStr] = Field(default=None, alias="imdbId")
    instagram_id: Optional[StrictStr] = Field(default=None, alias="instagramId")
    tvdb_id: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="tvdbId")
    tvrage_id: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="tvrageId")
    twitter_id: Optional[StrictStr] = Field(default=None, alias="twitterId")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["facebookId", "freebaseId", "freebaseMid", "imdbId", "instagramId", "tvdbId", "tvrageId", "twitterId"]

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
        """Create an instance of ExternalIds from a JSON string"""
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

        # set to None if facebook_id (nullable) is None
        # and model_fields_set contains the field
        if self.facebook_id is None and "facebook_id" in self.model_fields_set:
            _dict['facebookId'] = None

        # set to None if freebase_id (nullable) is None
        # and model_fields_set contains the field
        if self.freebase_id is None and "freebase_id" in self.model_fields_set:
            _dict['freebaseId'] = None

        # set to None if freebase_mid (nullable) is None
        # and model_fields_set contains the field
        if self.freebase_mid is None and "freebase_mid" in self.model_fields_set:
            _dict['freebaseMid'] = None

        # set to None if imdb_id (nullable) is None
        # and model_fields_set contains the field
        if self.imdb_id is None and "imdb_id" in self.model_fields_set:
            _dict['imdbId'] = None

        # set to None if instagram_id (nullable) is None
        # and model_fields_set contains the field
        if self.instagram_id is None and "instagram_id" in self.model_fields_set:
            _dict['instagramId'] = None

        # set to None if tvdb_id (nullable) is None
        # and model_fields_set contains the field
        if self.tvdb_id is None and "tvdb_id" in self.model_fields_set:
            _dict['tvdbId'] = None

        # set to None if tvrage_id (nullable) is None
        # and model_fields_set contains the field
        if self.tvrage_id is None and "tvrage_id" in self.model_fields_set:
            _dict['tvrageId'] = None

        # set to None if twitter_id (nullable) is None
        # and model_fields_set contains the field
        if self.twitter_id is None and "twitter_id" in self.model_fields_set:
            _dict['twitterId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ExternalIds from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "facebookId": obj.get("facebookId"),
            "freebaseId": obj.get("freebaseId"),
            "freebaseMid": obj.get("freebaseMid"),
            "imdbId": obj.get("imdbId"),
            "instagramId": obj.get("instagramId"),
            "tvdbId": obj.get("tvdbId"),
            "tvrageId": obj.get("tvrageId"),
            "twitterId": obj.get("twitterId")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


