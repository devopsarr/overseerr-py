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

from typing import Optional
from pydantic import BaseModel, Field, StrictStr, ValidationError, validator
from overseerr.models.movie_result import MovieResult
from overseerr.models.person_result import PersonResult
from overseerr.models.tv_result import TvResult
from typing import Any, List
from pydantic import StrictStr, Field

GETSEARCH200RESPONSERESULTSINNER_ANY_OF_SCHEMAS = ["MovieResult", "PersonResult", "TvResult"]

class GetSearch200ResponseResultsInner(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    # data type: MovieResult
    anyof_schema_1_validator: Optional[MovieResult] = None
    # data type: TvResult
    anyof_schema_2_validator: Optional[TvResult] = None
    # data type: PersonResult
    anyof_schema_3_validator: Optional[PersonResult] = None
    actual_instance: Any
    any_of_schemas: List[str] = Field(GETSEARCH200RESPONSERESULTSINNER_ANY_OF_SCHEMAS, const=True)

    class Config:
        validate_assignment = True

    @validator('actual_instance')
    def actual_instance_must_validate_anyof(cls, v):
        error_messages = []
        # validate data type: MovieResult
        if type(v) is not MovieResult:
            error_messages.append(f"Error! Input type `{type(v)}` is not `MovieResult`")
        else:
            return v

        # validate data type: TvResult
        if type(v) is not TvResult:
            error_messages.append(f"Error! Input type `{type(v)}` is not `TvResult`")
        else:
            return v

        # validate data type: PersonResult
        if type(v) is not PersonResult:
            error_messages.append(f"Error! Input type `{type(v)}` is not `PersonResult`")
        else:
            return v

        if error_messages:
            # no match
            raise ValueError("No match found when deserializing the JSON string into GetSearch200ResponseResultsInner with anyOf schemas: MovieResult, PersonResult, TvResult. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_json(cls, json_str: str) -> GetSearch200ResponseResultsInner:
        """Returns the object represented by the json string"""
        instance = cls()
        error_messages = []
        # anyof_schema_1_validator: Optional[MovieResult] = None
        try:
            instance.actual_instance = MovieResult.from_json(json_str)
            return instance
        except ValidationError as e:
             error_messages.append(str(e))
        # anyof_schema_2_validator: Optional[TvResult] = None
        try:
            instance.actual_instance = TvResult.from_json(json_str)
            return instance
        except ValidationError as e:
             error_messages.append(str(e))
        # anyof_schema_3_validator: Optional[PersonResult] = None
        try:
            instance.actual_instance = PersonResult.from_json(json_str)
            return instance
        except ValidationError as e:
             error_messages.append(str(e))

        if error_messages:
            # no match
            raise ValueError("No match found when deserializing the JSON string into GetSearch200ResponseResultsInner with anyOf schemas: MovieResult, PersonResult, TvResult. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is not None:
            return self.actual_instance.to_json()
        else:
            return "null"

    def to_dict(self) -> dict:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is not None:
            return self.actual_instance.to_dict()
        else:
            return dict()

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.dict())

