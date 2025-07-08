# ragagent_client.AgentApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**agent_direct_message_api_agent_direct_message_post**](AgentApi.md#agent_direct_message_api_agent_direct_message_post) | **POST** /api/agent/direct_message |  Agent Direct Message
[**list_agents_api_agent_agents_get**](AgentApi.md#list_agents_api_agent_agents_get) | **GET** /api/agent/agents | List Agents


# **agent_direct_message_api_agent_direct_message_post**
> UIEventResponse agent_direct_message_api_agent_direct_message_post(ui_event_payload)

 Agent Direct Message

Receives a UI event, processes it with an agent, and returns the agent's response.

### Example


```python
import ragagent_client
from ragagent_client.models.ui_event_payload import UIEventPayload
from ragagent_client.models.ui_event_response import UIEventResponse
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
    api_instance = ragagent_client.AgentApi(api_client)
    ui_event_payload = ragagent_client.UIEventPayload() # UIEventPayload | 

    try:
        #  Agent Direct Message
        api_response = api_instance.agent_direct_message_api_agent_direct_message_post(ui_event_payload)
        print("The response of AgentApi->agent_direct_message_api_agent_direct_message_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentApi->agent_direct_message_api_agent_direct_message_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ui_event_payload** | [**UIEventPayload**](UIEventPayload.md)|  | 

### Return type

[**UIEventResponse**](UIEventResponse.md)

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

# **list_agents_api_agent_agents_get**
> Dict[str, object] list_agents_api_agent_agents_get()

List Agents

List available agents for the frontend.
Returns a simple list of agents compatible with ragauai frontend expectations.

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
    api_instance = ragagent_client.AgentApi(api_client)

    try:
        # List Agents
        api_response = api_instance.list_agents_api_agent_agents_get()
        print("The response of AgentApi->list_agents_api_agent_agents_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AgentApi->list_agents_api_agent_agents_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

**Dict[str, object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

