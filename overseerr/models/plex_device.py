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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from overseerr.models.plex_connection import PlexConnection
from typing import Optional, Set
from typing_extensions import Self

class PlexDevice(BaseModel):
    """
    PlexDevice
    """ # noqa: E501
    name: StrictStr
    product: StrictStr
    product_version: StrictStr = Field(alias="productVersion")
    platform: StrictStr
    platform_version: Optional[StrictStr] = Field(default=None, alias="platformVersion")
    device: StrictStr
    client_identifier: StrictStr = Field(alias="clientIdentifier")
    created_at: StrictStr = Field(alias="createdAt")
    last_seen_at: StrictStr = Field(alias="lastSeenAt")
    provides: List[StrictStr]
    owned: StrictBool
    owner_id: Optional[StrictStr] = Field(default=None, alias="ownerID")
    home: Optional[StrictBool] = None
    source_title: Optional[StrictStr] = Field(default=None, alias="sourceTitle")
    access_token: Optional[StrictStr] = Field(default=None, alias="accessToken")
    public_address: Optional[StrictStr] = Field(default=None, alias="publicAddress")
    https_required: Optional[StrictBool] = Field(default=None, alias="httpsRequired")
    synced: Optional[StrictBool] = None
    relay: Optional[StrictBool] = None
    dns_rebinding_protection: Optional[StrictBool] = Field(default=None, alias="dnsRebindingProtection")
    nat_loopback_supported: Optional[StrictBool] = Field(default=None, alias="natLoopbackSupported")
    public_address_matches: Optional[StrictBool] = Field(default=None, alias="publicAddressMatches")
    presence: Optional[StrictBool] = None
    connection: List[PlexConnection]
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["name", "product", "productVersion", "platform", "platformVersion", "device", "clientIdentifier", "createdAt", "lastSeenAt", "provides", "owned", "ownerID", "home", "sourceTitle", "accessToken", "publicAddress", "httpsRequired", "synced", "relay", "dnsRebindingProtection", "natLoopbackSupported", "publicAddressMatches", "presence", "connection"]

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
        """Create an instance of PlexDevice from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in connection (list)
        _items = []
        if self.connection:
            for _item_connection in self.connection:
                if _item_connection:
                    _items.append(_item_connection.to_dict())
            _dict['connection'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PlexDevice from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "product": obj.get("product"),
            "productVersion": obj.get("productVersion"),
            "platform": obj.get("platform"),
            "platformVersion": obj.get("platformVersion"),
            "device": obj.get("device"),
            "clientIdentifier": obj.get("clientIdentifier"),
            "createdAt": obj.get("createdAt"),
            "lastSeenAt": obj.get("lastSeenAt"),
            "provides": obj.get("provides"),
            "owned": obj.get("owned"),
            "ownerID": obj.get("ownerID"),
            "home": obj.get("home"),
            "sourceTitle": obj.get("sourceTitle"),
            "accessToken": obj.get("accessToken"),
            "publicAddress": obj.get("publicAddress"),
            "httpsRequired": obj.get("httpsRequired"),
            "synced": obj.get("synced"),
            "relay": obj.get("relay"),
            "dnsRebindingProtection": obj.get("dnsRebindingProtection"),
            "natLoopbackSupported": obj.get("natLoopbackSupported"),
            "publicAddressMatches": obj.get("publicAddressMatches"),
            "presence": obj.get("presence"),
            "connection": [PlexConnection.from_dict(_item) for _item in obj["connection"]] if obj.get("connection") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


