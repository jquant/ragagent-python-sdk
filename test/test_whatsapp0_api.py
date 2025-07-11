# coding: utf-8

"""
    Ragagent MCP Gateway

    Advanced AI-powered conversation management system

    The version of the OpenAPI document: 0.4.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ragagent_client.api.whatsapp_api import WhatsappApi


class TestWhatsappApi(unittest.TestCase):
    """WhatsappApi unit test stubs"""

    def setUp(self) -> None:
        self.api = WhatsappApi()

    def tearDown(self) -> None:
        pass

    def test_legacy_flow_endpoint_whatsapp_flow_post(self) -> None:
        """Test case for legacy_flow_endpoint_whatsapp_flow_post

        Legacy Flow Endpoint
        """
        pass

    def test_webhook_verify_whatsapp_webhook_get(self) -> None:
        """Test case for webhook_verify_whatsapp_webhook_get

        Webhook Verify
        """
        pass

    def test_webhook_whatsapp_webhook_post(self) -> None:
        """Test case for webhook_whatsapp_webhook_post

        Webhook
        """
        pass


if __name__ == '__main__':
    unittest.main()
