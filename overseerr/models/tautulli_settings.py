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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class TautulliSettings(BaseModel):
    """
    TautulliSettings
    """ # noqa: E501
    hostname: Optional[StrictStr] = None
    port: Optional[Union[StrictFloat, StrictInt]] = None
    use_ssl: Optional[StrictBool] = Field(default=None, alias="useSsl")
    api_key: Optional[StrictStr] = Field(default=None, alias="apiKey")
    external_url: Optional[StrictStr] = Field(default=None, alias="externalUrl")
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["hostname", "port", "useSsl", "apiKey", "externalUrl"]

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
        """Create an instance of TautulliSettings from a JSON string"""
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

        # set to None if hostname (nullable) is None
        # and model_fields_set contains the field
        if self.hostname is None and "hostname" in self.model_fields_set:
            _dict['hostname'] = None

        # set to None if port (nullable) is None
        # and model_fields_set contains the field
        if self.port is None and "port" in self.model_fields_set:
            _dict['port'] = None

        # set to None if use_ssl (nullable) is None
        # and model_fields_set contains the field
        if self.use_ssl is None and "use_ssl" in self.model_fields_set:
            _dict['useSsl'] = None

        # set to None if api_key (nullable) is None
        # and model_fields_set contains the field
        if self.api_key is None and "api_key" in self.model_fields_set:
            _dict['apiKey'] = None

        # set to None if external_url (nullable) is None
        # and model_fields_set contains the field
        if self.external_url is None and "external_url" in self.model_fields_set:
            _dict['externalUrl'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TautulliSettings from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "hostname": obj.get("hostname"),
            "port": obj.get("port"),
            "useSsl": obj.get("useSsl"),
            "apiKey": obj.get("apiKey"),
            "externalUrl": obj.get("externalUrl")
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


