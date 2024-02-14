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

class User(BaseModel):
    """
    User
    """ # noqa: E501
    id: StrictInt
    email: StrictStr
    username: Optional[StrictStr] = None
    plex_token: Optional[StrictStr] = Field(default=None, alias="plexToken")
    plex_username: Optional[StrictStr] = Field(default=None, alias="plexUsername")
    user_type: Optional[StrictInt] = Field(default=None, alias="userType")
    permissions: Optional[Union[StrictFloat, StrictInt]] = None
    avatar: Optional[StrictStr] = None
    created_at: StrictStr = Field(alias="createdAt")
    updated_at: StrictStr = Field(alias="updatedAt")
    request_count: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="requestCount")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["id", "email", "username", "plexToken", "plexUsername", "userType", "permissions", "avatar", "createdAt", "updatedAt", "requestCount"]

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
        """Create an instance of User from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "id",
            "email",
            "plex_token",
            "plex_username",
            "user_type",
            "avatar",
            "created_at",
            "updated_at",
            "request_count",
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

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of User from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "email": obj.get("email"),
            "username": obj.get("username"),
            "plexToken": obj.get("plexToken"),
            "plexUsername": obj.get("plexUsername"),
            "userType": obj.get("userType"),
            "permissions": obj.get("permissions"),
            "avatar": obj.get("avatar"),
            "createdAt": obj.get("createdAt"),
            "updatedAt": obj.get("updatedAt"),
            "requestCount": obj.get("requestCount")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


