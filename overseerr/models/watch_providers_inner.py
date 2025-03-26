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

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from overseerr.models.watch_provider_details import WatchProviderDetails
from typing import Optional, Set
from typing_extensions import Self

class WatchProvidersInner(BaseModel):
    """
    WatchProvidersInner
    """ # noqa: E501
    iso_3166_1: Optional[StrictStr] = None
    link: Optional[StrictStr] = None
    buy: Optional[List[WatchProviderDetails]] = None
    flatrate: Optional[List[WatchProviderDetails]] = None
    additional_properties: Dict[str, Any] = {}
    __properties: ClassVar[List[str]] = ["iso_3166_1", "link", "buy", "flatrate"]

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
        """Create an instance of WatchProvidersInner from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in buy (list)
        _items = []
        if self.buy:
            for _item_buy in self.buy:
                if _item_buy:
                    _items.append(_item_buy.to_dict())
            _dict['buy'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in flatrate (list)
        _items = []
        if self.flatrate:
            for _item_flatrate in self.flatrate:
                if _item_flatrate:
                    _items.append(_item_flatrate.to_dict())
            _dict['flatrate'] = _items
        # puts key-value pairs in additional_properties in the top level
        if self.additional_properties is not None:
            for _key, _value in self.additional_properties.items():
                _dict[_key] = _value

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WatchProvidersInner from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "iso_3166_1": obj.get("iso_3166_1"),
            "link": obj.get("link"),
            "buy": [WatchProviderDetails.from_dict(_item) for _item in obj["buy"]] if obj.get("buy") is not None else None,
            "flatrate": [WatchProviderDetails.from_dict(_item) for _item in obj["flatrate"]] if obj.get("flatrate") is not None else None
        })
        # store additional fields in additional_properties
        for _key in obj.keys():
            if _key not in cls.__properties:
                _obj.additional_properties[_key] = obj.get(_key)

        return _obj


