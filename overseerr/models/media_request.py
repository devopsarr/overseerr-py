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
from overseerr.models.media_request_modified_by import MediaRequestModifiedBy
from overseerr.models.user import User
from typing import Optional, Set
from typing_extensions import Self

class MediaRequest(BaseModel):
    """
    MediaRequest
    """ # noqa: E501
    id: Union[StrictFloat, StrictInt]
    status: Union[StrictFloat, StrictInt] = Field(description="Status of the request. 1 = PENDING APPROVAL, 2 = APPROVED, 3 = DECLINED")
    media: Optional[MediaInfo] = None
    created_at: Optional[StrictStr] = Field(default=None, alias="createdAt")
    updated_at: Optional[StrictStr] = Field(default=None, alias="updatedAt")
    requested_by: Optional[User] = Field(default=None, alias="requestedBy")
    modified_by: Optional[MediaRequestModifiedBy] = Field(default=None, alias="modifiedBy")
    is4k: Optional[StrictBool] = None
    server_id: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="serverId")
    profile_id: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="profileId")
    root_folder: Optional[StrictStr] = Field(default=None, alias="rootFolder")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["id", "status", "media", "createdAt", "updatedAt", "requestedBy", "modifiedBy", "is4k", "serverId", "profileId", "rootFolder"]

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
        """Create an instance of MediaRequest from a JSON string"""
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
        * Fields in `self.additional_properties` are added to the output dict.
        """
        excluded_fields: Set[str] = set([
            "id",
            "status",
            "created_at",
            "updated_at",
            "additional_properties",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of media
        if self.media:
            _dict['media'] = self.media.to_dict()
        # override the default output from pydantic by calling `to_dict()` of requested_by
        if self.requested_by:
            _dict['requestedBy'] = self.requested_by.to_dict()
        # override the default output from pydantic by calling `to_dict()` of modified_by
        if self.modified_by:
            _dict['modifiedBy'] = self.modified_by.to_dict()
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MediaRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "id": obj.get("id"),
            "status": obj.get("status"),
            "media": MediaInfo.from_dict(obj["media"]) if obj.get("media") is not None else None,
            "createdAt": obj.get("createdAt"),
            "updatedAt": obj.get("updatedAt"),
            "requestedBy": User.from_dict(obj["requestedBy"]) if obj.get("requestedBy") is not None else None,
            "modifiedBy": MediaRequestModifiedBy.from_dict(obj["modifiedBy"]) if obj.get("modifiedBy") is not None else None,
            "is4k": obj.get("is4k"),
            "serverId": obj.get("serverId"),
            "profileId": obj.get("profileId"),
            "rootFolder": obj.get("rootFolder")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

from overseerr.models.media_info import MediaInfo
# TODO: Rewrite to not use raise_errors
MediaRequest.model_rebuild(raise_errors=False)

