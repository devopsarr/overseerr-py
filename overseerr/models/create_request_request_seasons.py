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
import json
import re  # noqa: F401

from typing import Any, List, Optional, Union
from pydantic import BaseModel, Field, StrictStr, ValidationError, field_validator
from typing import Any, List
from pydantic import StrictStr, Field

CREATEREQUESTREQUESTSEASONS_ONE_OF_SCHEMAS = ["List[float]", "str"]

class CreateRequestRequestSeasons(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    # data type: List[float]
    oneof_schema_1_validator: Optional[List[Union[Annotated[float, Field(strict=True, ge=1)], Annotated[int, Field(strict=True, ge=1)]]]] = None
    # data type: str
    oneof_schema_2_validator: Optional[StrictStr] = None
    actual_instance: Any
    one_of_schemas: List[str] = Field(CREATEREQUESTREQUESTSEASONS_ONE_OF_SCHEMAS, const=True)

    class Config:
        validate_assignment = True

    @validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        error_messages = []
        match = 0
        # validate data type: List[float]
        if type(v) is not List[float]:
            error_messages.append(f"Error! Input type `{type(v)}` is not `List[float]`")
        else:
            match += 1

        # validate data type: str
        if type(v) is not str:
            error_messages.append(f"Error! Input type `{type(v)}` is not `str`")
        else:
            match += 1

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into CreateRequestRequestSeasons with oneOf schemas: List[float], str. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into CreateRequestRequestSeasons with oneOf schemas: List[float], str. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: dict) -> CreateRequestRequestSeasons:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> CreateRequestRequestSeasons:
        """Returns the object represented by the json string"""
        instance = cls()
        error_messages = []
        match = 0


        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into CreateRequestRequestSeasons with oneOf schemas: List[float], str. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into CreateRequestRequestSeasons with oneOf schemas: List[float], str. Details: " + ", ".join(error_messages))
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





