# coding: utf-8

"""
    Ragagent MCP Gateway

    Advanced AI-powered conversation management system

    The version of the OpenAPI document: 0.4.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ragagent_client.models.ragagent_models_flow_webhook_encrypted_flow_data import RagagentModelsFlowWebhookEncryptedFlowData

class TestRagagentModelsFlowWebhookEncryptedFlowData(unittest.TestCase):
    """RagagentModelsFlowWebhookEncryptedFlowData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> RagagentModelsFlowWebhookEncryptedFlowData:
        """Test RagagentModelsFlowWebhookEncryptedFlowData
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `RagagentModelsFlowWebhookEncryptedFlowData`
        """
        model = RagagentModelsFlowWebhookEncryptedFlowData()
        if include_optional:
            return RagagentModelsFlowWebhookEncryptedFlowData(
                encrypted_flow_data = '',
                encrypted_aes_key = '',
                initial_vector = ''
            )
        else:
            return RagagentModelsFlowWebhookEncryptedFlowData(
                encrypted_flow_data = '',
                encrypted_aes_key = '',
                initial_vector = '',
        )
        """

    def testRagagentModelsFlowWebhookEncryptedFlowData(self):
        """Test RagagentModelsFlowWebhookEncryptedFlowData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
