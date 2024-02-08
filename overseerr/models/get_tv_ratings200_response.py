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



from pydantic import BaseModel, validator

class GetTvRatings200Response(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    title: Optional[str]
    year: Optional[float]
    url: Optional[str]
    critics_score: Optional[float]
    critics_rating: Optional[str]
    additional_properties: Dict[str, Any] = {}
    __properties = ["title", "year", "url", "criticsScore", "criticsRating"]

    @validator('critics_rating')
    def critics_rating_validate_enum(cls, v):
        if v is None:
            return v

        if v not in ('Rotten', 'Fresh'):
            raise ValueError("must validate the enum values ('Rotten', 'Fresh')")
        return v

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
    def from_json(cls, json_str: str) -> GetTvRatings200Response:
        """Create an instance of GetTvRatings200Response from a JSON string"""
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

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GetTvRatings200Response:
        """Create an instance of GetTvRatings200Response from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return GetTvRatings200Response.parse_obj(obj)

        _obj = GetTvRatings200Response.parse_obj({
            "title": obj.get("title"),
            "year": obj.get("year"),
            "url": obj.get("url"),
            "critics_score": obj.get("criticsScore"),
            "critics_rating": obj.get("criticsRating")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

