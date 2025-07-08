# RagagentModelsFlowWebhookEncryptedFlowData

Encrypted flow data from WhatsApp Flow webhook.  WhatsApp Flow sends encrypted data in this format when using the data_exchange component. This model represents the raw encrypted data that needs to be decrypted using the private key associated with the public key provided during flow configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**encrypted_flow_data** | **str** |  | 
**encrypted_aes_key** | **str** |  | 
**initial_vector** | **str** |  | 

## Example

```python
from ragagent_client.models.ragagent_models_flow_webhook_encrypted_flow_data import RagagentModelsFlowWebhookEncryptedFlowData

# TODO update the JSON string below
json = "{}"
# create an instance of RagagentModelsFlowWebhookEncryptedFlowData from a JSON string
ragagent_models_flow_webhook_encrypted_flow_data_instance = RagagentModelsFlowWebhookEncryptedFlowData.from_json(json)
# print the JSON string representation of the object
print(RagagentModelsFlowWebhookEncryptedFlowData.to_json())

# convert the object into a dict
ragagent_models_flow_webhook_encrypted_flow_data_dict = ragagent_models_flow_webhook_encrypted_flow_data_instance.to_dict()
# create an instance of RagagentModelsFlowWebhookEncryptedFlowData from a dict
ragagent_models_flow_webhook_encrypted_flow_data_from_dict = RagagentModelsFlowWebhookEncryptedFlowData.from_dict(ragagent_models_flow_webhook_encrypted_flow_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


