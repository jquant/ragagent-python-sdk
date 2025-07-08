# ragagent_client.UiEventsApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**handle_ui_chat_event_ui_events_chat_post**](UiEventsApi.md#handle_ui_chat_event_ui_events_chat_post) | **POST** /ui-events/chat | Handle Ui Chat Event


# **handle_ui_chat_event_ui_events_chat_post**
> object handle_ui_chat_event_ui_events_chat_post(ui_event_request)

Handle Ui Chat Event

Handle UI chat events via service

### Example


```python
import ragagent_client
from ragagent_client.models.ui_event_request import UIEventRequest
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
    api_instance = ragagent_client.UiEventsApi(api_client)
    ui_event_request = ragagent_client.UIEventRequest() # UIEventRequest | 

    try:
        # Handle Ui Chat Event
        api_response = api_instance.handle_ui_chat_event_ui_events_chat_post(ui_event_request)
        print("The response of UiEventsApi->handle_ui_chat_event_ui_events_chat_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UiEventsApi->handle_ui_chat_event_ui_events_chat_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ui_event_request** | [**UIEventRequest**](UIEventRequest.md)|  | 

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

