# ragagent_client.McpApiApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**execute_tool_api_v1_tools_tool_name_post**](McpApiApi.md#execute_tool_api_v1_tools_tool_name_post) | **POST** /api/v1/tools/{tool_name} | Execute Tool
[**get_openapi_spec_api_v1_openapi_get**](McpApiApi.md#get_openapi_spec_api_v1_openapi_get) | **GET** /api/v1/openapi | Get Openapi Spec
[**get_openrpc_spec_api_v1_openrpc_get**](McpApiApi.md#get_openrpc_spec_api_v1_openrpc_get) | **GET** /api/v1/openrpc | Get Openrpc Spec
[**list_all_tools_api_v1_tools_list_all_tools_post**](McpApiApi.md#list_all_tools_api_v1_tools_list_all_tools_post) | **POST** /api/v1/tools/list_all_tools | List All Tools
[**list_prompts_api_v1_prompts_list_get**](McpApiApi.md#list_prompts_api_v1_prompts_list_get) | **GET** /api/v1/prompts/list | List Prompts
[**list_resources_api_v1_resources_list_get**](McpApiApi.md#list_resources_api_v1_resources_list_get) | **GET** /api/v1/resources/list | List Resources
[**mcp_api_health_api_v1_health_get**](McpApiApi.md#mcp_api_health_api_v1_health_get) | **GET** /api/v1/health | Mcp Api Health


# **execute_tool_api_v1_tools_tool_name_post**
> ApiResponse execute_tool_api_v1_tools_tool_name_post(tool_name, tool_execution_request)

Execute Tool

Execute a specific MCP tool

Executes the specified tool with the provided arguments and returns the result.
The tool must be available in the MCP gateway's tool registry.

### Example


```python
import ragagent_client
from ragagent_client.models.api_response import ApiResponse
from ragagent_client.models.tool_execution_request import ToolExecutionRequest
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
    api_instance = ragagent_client.McpApiApi(api_client)
    tool_name = 'tool_name_example' # str | 
    tool_execution_request = ragagent_client.ToolExecutionRequest() # ToolExecutionRequest | 

    try:
        # Execute Tool
        api_response = api_instance.execute_tool_api_v1_tools_tool_name_post(tool_name, tool_execution_request)
        print("The response of McpApiApi->execute_tool_api_v1_tools_tool_name_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling McpApiApi->execute_tool_api_v1_tools_tool_name_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tool_name** | **str**|  | 
 **tool_execution_request** | [**ToolExecutionRequest**](ToolExecutionRequest.md)|  | 

### Return type

[**ApiResponse**](ApiResponse.md)

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

# **get_openapi_spec_api_v1_openapi_get**
> ApiResponse get_openapi_spec_api_v1_openapi_get()

Get Openapi Spec

Get OpenAPI specification

Returns the OpenAPI specification for the REST API endpoints.

### Example


```python
import ragagent_client
from ragagent_client.models.api_response import ApiResponse
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
    api_instance = ragagent_client.McpApiApi(api_client)

    try:
        # Get Openapi Spec
        api_response = api_instance.get_openapi_spec_api_v1_openapi_get()
        print("The response of McpApiApi->get_openapi_spec_api_v1_openapi_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling McpApiApi->get_openapi_spec_api_v1_openapi_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiResponse**](ApiResponse.md)

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

# **get_openrpc_spec_api_v1_openrpc_get**
> ApiResponse get_openrpc_spec_api_v1_openrpc_get()

Get Openrpc Spec

Get OpenRPC specification

Returns the OpenRPC specification for the MCP JSON-RPC interface.

### Example


```python
import ragagent_client
from ragagent_client.models.api_response import ApiResponse
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
    api_instance = ragagent_client.McpApiApi(api_client)

    try:
        # Get Openrpc Spec
        api_response = api_instance.get_openrpc_spec_api_v1_openrpc_get()
        print("The response of McpApiApi->get_openrpc_spec_api_v1_openrpc_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling McpApiApi->get_openrpc_spec_api_v1_openrpc_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiResponse**](ApiResponse.md)

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

# **list_all_tools_api_v1_tools_list_all_tools_post**
> ApiResponse list_all_tools_api_v1_tools_list_all_tools_post()

List All Tools

List all available MCP tools

Returns a comprehensive list of all tools available through the MCP gateway,
including tool names, descriptions, parameters schemas, and metadata.

### Example


```python
import ragagent_client
from ragagent_client.models.api_response import ApiResponse
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
    api_instance = ragagent_client.McpApiApi(api_client)

    try:
        # List All Tools
        api_response = api_instance.list_all_tools_api_v1_tools_list_all_tools_post()
        print("The response of McpApiApi->list_all_tools_api_v1_tools_list_all_tools_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling McpApiApi->list_all_tools_api_v1_tools_list_all_tools_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiResponse**](ApiResponse.md)

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

# **list_prompts_api_v1_prompts_list_get**
> ApiResponse list_prompts_api_v1_prompts_list_get()

List Prompts

List all available MCP prompts

Returns a list of all prompts available through the MCP gateway,
including prompt names, descriptions, and argument schemas.

### Example


```python
import ragagent_client
from ragagent_client.models.api_response import ApiResponse
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
    api_instance = ragagent_client.McpApiApi(api_client)

    try:
        # List Prompts
        api_response = api_instance.list_prompts_api_v1_prompts_list_get()
        print("The response of McpApiApi->list_prompts_api_v1_prompts_list_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling McpApiApi->list_prompts_api_v1_prompts_list_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiResponse**](ApiResponse.md)

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

# **list_resources_api_v1_resources_list_get**
> ApiResponse list_resources_api_v1_resources_list_get()

List Resources

List all available MCP resources

Returns a list of all resources available through the MCP gateway,
including resource URIs, descriptions, and MIME types.

### Example


```python
import ragagent_client
from ragagent_client.models.api_response import ApiResponse
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
    api_instance = ragagent_client.McpApiApi(api_client)

    try:
        # List Resources
        api_response = api_instance.list_resources_api_v1_resources_list_get()
        print("The response of McpApiApi->list_resources_api_v1_resources_list_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling McpApiApi->list_resources_api_v1_resources_list_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiResponse**](ApiResponse.md)

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

# **mcp_api_health_api_v1_health_get**
> ApiResponse mcp_api_health_api_v1_health_get()

Mcp Api Health

Health check for MCP API endpoints

Verifies that the MCP server and gateway router are properly initialized
and can respond to basic requests.

### Example


```python
import ragagent_client
from ragagent_client.models.api_response import ApiResponse
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
    api_instance = ragagent_client.McpApiApi(api_client)

    try:
        # Mcp Api Health
        api_response = api_instance.mcp_api_health_api_v1_health_get()
        print("The response of McpApiApi->mcp_api_health_api_v1_health_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling McpApiApi->mcp_api_health_api_v1_health_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ApiResponse**](ApiResponse.md)

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

