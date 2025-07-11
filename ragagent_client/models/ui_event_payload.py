# coding: utf-8

"""
    Ragagent MCP Gateway

    Advanced AI-powered conversation management system

    The version of the OpenAPI document: 0.4.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Set
from typing_extensions import Self

class UIEventPayload(BaseModel):
    """
    UIEventPayload
    """ # noqa: E501
    tenant_id: StrictStr
    user_prompt: StrictStr
    conversation_id: Optional[StrictStr] = None
    request_id: Optional[StrictStr] = None
    source: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["tenant_id", "user_prompt", "conversation_id", "request_id", "source"]

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
        """Create an instance of UIEventPayload from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # set to None if conversation_id (nullable) is None
        # and model_fields_set contains the field
        if self.conversation_id is None and "conversation_id" in self.model_fields_set:
            _dict['conversation_id'] = None

        # set to None if request_id (nullable) is None
        # and model_fields_set contains the field
        if self.request_id is None and "request_id" in self.model_fields_set:
            _dict['request_id'] = None

        # set to None if source (nullable) is None
        # and model_fields_set contains the field
        if self.source is None and "source" in self.model_fields_set:
            _dict['source'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UIEventPayload from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "tenant_id": obj.get("tenant_id"),
            "user_prompt": obj.get("user_prompt"),
            "conversation_id": obj.get("conversation_id"),
            "request_id": obj.get("request_id"),
            "source": obj.get("source")
        })
        return _obj


