# RagagentRagatangaFlowsFlowWebhookHandlerEncryptedFlowData

Encrypted flow data from WhatsApp webhook.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**encrypted_flow_data** | **str** |  | 
**encrypted_aes_key** | **str** |  | 
**initial_vector** | **str** |  | 

## Example

```python
from ragagent_client.models.ragagent_ragatanga_flows_flow_webhook_handler_encrypted_flow_data import RagagentRagatangaFlowsFlowWebhookHandlerEncryptedFlowData

# TODO update the JSON string below
json = "{}"
# create an instance of RagagentRagatangaFlowsFlowWebhookHandlerEncryptedFlowData from a JSON string
ragagent_ragatanga_flows_flow_webhook_handler_encrypted_flow_data_instance = RagagentRagatangaFlowsFlowWebhookHandlerEncryptedFlowData.from_json(json)
# print the JSON string representation of the object
print(RagagentRagatangaFlowsFlowWebhookHandlerEncryptedFlowData.to_json())

# convert the object into a dict
ragagent_ragatanga_flows_flow_webhook_handler_encrypted_flow_data_dict = ragagent_ragatanga_flows_flow_webhook_handler_encrypted_flow_data_instance.to_dict()
# create an instance of RagagentRagatangaFlowsFlowWebhookHandlerEncryptedFlowData from a dict
ragagent_ragatanga_flows_flow_webhook_handler_encrypted_flow_data_from_dict = RagagentRagatangaFlowsFlowWebhookHandlerEncryptedFlowData.from_dict(ragagent_ragatanga_flows_flow_webhook_handler_encrypted_flow_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


