# ragagent_client.WhatsAppApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**webhook_verify_whatsapp_webhook_get**](WhatsAppApi.md#webhook_verify_whatsapp_webhook_get) | **GET** /whatsapp/webhook | Webhook Verify
[**webhook_whatsapp_webhook_post**](WhatsAppApi.md#webhook_whatsapp_webhook_post) | **POST** /whatsapp/webhook | Webhook


# **webhook_verify_whatsapp_webhook_get**
> object webhook_verify_whatsapp_webhook_get(hub_mode=hub_mode, hub_verify_token=hub_verify_token, hub_challenge=hub_challenge)

Webhook Verify

Webhook verification endpoint for WhatsApp.

### Example


```python
import ragagent_client
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
    api_instance = ragagent_client.WhatsAppApi(api_client)
    hub_mode = 'hub_mode_example' # str |  (optional)
    hub_verify_token = 'hub_verify_token_example' # str |  (optional)
    hub_challenge = 'hub_challenge_example' # str |  (optional)

    try:
        # Webhook Verify
        api_response = api_instance.webhook_verify_whatsapp_webhook_get(hub_mode=hub_mode, hub_verify_token=hub_verify_token, hub_challenge=hub_challenge)
        print("The response of WhatsAppApi->webhook_verify_whatsapp_webhook_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WhatsAppApi->webhook_verify_whatsapp_webhook_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **hub_mode** | **str**|  | [optional] 
 **hub_verify_token** | **str**|  | [optional] 
 **hub_challenge** | **str**|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **webhook_whatsapp_webhook_post**
> object webhook_whatsapp_webhook_post(x_hub_signature_256=x_hub_signature_256)

Webhook

Webhook endpoint to receive WhatsApp messages and flow data.

### Example


```python
import ragagent_client
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
    api_instance = ragagent_client.WhatsAppApi(api_client)
    x_hub_signature_256 = 'x_hub_signature_256_example' # str |  (optional)

    try:
        # Webhook
        api_response = api_instance.webhook_whatsapp_webhook_post(x_hub_signature_256=x_hub_signature_256)
        print("The response of WhatsAppApi->webhook_whatsapp_webhook_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WhatsAppApi->webhook_whatsapp_webhook_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_hub_signature_256** | **str**|  | [optional] 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

