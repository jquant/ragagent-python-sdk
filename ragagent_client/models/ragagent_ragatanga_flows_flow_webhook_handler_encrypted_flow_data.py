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
from typing import Any, ClassVar, Dict, List
from typing import Optional, Set
from typing_extensions import Self

class RagagentRagatangaFlowsFlowWebhookHandlerEncryptedFlowData(BaseModel):
    """
    Encrypted flow data from WhatsApp webhook.
    """ # noqa: E501
    encrypted_flow_data: StrictStr
    encrypted_aes_key: StrictStr
    initial_vector: StrictStr
    __properties: ClassVar[List[str]] = ["encrypted_flow_data", "encrypted_aes_key", "initial_vector"]

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
        """Create an instance of RagagentRagatangaFlowsFlowWebhookHandlerEncryptedFlowData from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RagagentRagatangaFlowsFlowWebhookHandlerEncryptedFlowData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "encrypted_flow_data": obj.get("encrypted_flow_data"),
            "encrypted_aes_key": obj.get("encrypted_aes_key"),
            "initial_vector": obj.get("initial_vector")
        })
        return _obj


