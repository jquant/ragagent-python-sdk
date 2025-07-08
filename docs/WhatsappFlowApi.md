# ragagent_client.WhatsappFlowApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**frequencia_premiada_webhook_flows_frequencia_premiada_webhook_post**](WhatsappFlowApi.md#frequencia_premiada_webhook_flows_frequencia_premiada_webhook_post) | **POST** /flows/frequencia-premiada/webhook | Frequencia Premiada Webhook


# **frequencia_premiada_webhook_flows_frequencia_premiada_webhook_post**
> object frequencia_premiada_webhook_flows_frequencia_premiada_webhook_post(ragagent_ragatanga_flows_flow_webhook_handler_encrypted_flow_data=ragagent_ragatanga_flows_flow_webhook_handler_encrypted_flow_data)

Frequencia Premiada Webhook

Webhook endpoint for WhatsApp Flow Frequencia Premiada.

This implementation is for development and testing purposes.
It doesn't actually decrypt the data, but returns valid responses.

### Example


```python
import ragagent_client
from ragagent_client.models.ragagent_ragatanga_flows_flow_webhook_handler_encrypted_flow_data import RagagentRagatangaFlowsFlowWebhookHandlerEncryptedFlowData
from ragagent_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = ragagent_client.Configuration(
    host = "http://localhost"
)


# Enter a context with an instance of the API client
with ragagent_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ragagent_client.WhatsappFlowApi(api_client)
    ragagent_ragatanga_flows_flow_webhook_handler_encrypted_flow_data = ragagent_client.RagagentRagatangaFlowsFlowWebhookHandlerEncryptedFlowData() # RagagentRagatangaFlowsFlowWebhookHandlerEncryptedFlowData |  (optional)

    try:
        # Frequencia Premiada Webhook
        api_response = api_instance.frequencia_premiada_webhook_flows_frequencia_premiada_webhook_post(ragagent_ragatanga_flows_flow_webhook_handler_encrypted_flow_data=ragagent_ragatanga_flows_flow_webhook_handler_encrypted_flow_data)
        print("The response of WhatsappFlowApi->frequencia_premiada_webhook_flows_frequencia_premiada_webhook_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WhatsappFlowApi->frequencia_premiada_webhook_flows_frequencia_premiada_webhook_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ragagent_ragatanga_flows_flow_webhook_handler_encrypted_flow_data** | [**RagagentRagatangaFlowsFlowWebhookHandlerEncryptedFlowData**](RagagentRagatangaFlowsFlowWebhookHandlerEncryptedFlowData.md)|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

