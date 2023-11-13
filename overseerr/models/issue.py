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
from overseerr.models.issue_comment import IssueComment
from overseerr.models.media_info import MediaInfo
from overseerr.models.user import User

class Issue(BaseModel):
    """NOTE: This class is auto generated by OpenAPI Generator.
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """
    id: Optional[float]
    issue_type: Optional[float]
    media: Optional[MediaInfo]
    created_by: Optional[User]
    modified_by: Optional[User]
    comments: Optional[List]
    additional_properties: Dict[str, Any] = {}
    __properties = ["id", "issueType", "media", "createdBy", "modifiedBy", "comments"]

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
    def from_json(cls, json_str: str) -> Issue:
        """Create an instance of Issue from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                            "additional_properties"
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of media
        if self.media:
            _dict['media'] = self.media.to_dict()
        # override the default output from pydantic by calling `to_dict()` of created_by
        if self.created_by:
            _dict['createdBy'] = self.created_by.to_dict()
        # override the default output from pydantic by calling `to_dict()` of modified_by
        if self.modified_by:
            _dict['modifiedBy'] = self.modified_by.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in comments (list)
        _items = []
        if self.comments:
            for _item in self.comments:
                if _item:
                    _items.append(_item.to_dict())
            _dict['comments'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> Issue:
        """Create an instance of Issue from a dict"""
        if obj is None:
            return None

        if type(obj) is not dict:
            return Issue.parse_obj(obj)

        _obj = Issue.parse_obj({
            "id": obj.get("id"),
            "issue_type": obj.get("issueType"),
            "media": MediaInfo.from_dict(obj.get("media")) if obj.get("media") is not None else None,
            "created_by": User.from_dict(obj.get("createdBy")) if obj.get("createdBy") is not None else None,
            "modified_by": User.from_dict(obj.get("modifiedBy")) if obj.get("modifiedBy") is not None else None,
            "comments": [IssueComment.from_dict(_item) for _item in obj.get("comments")] if obj.get("comments") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj

