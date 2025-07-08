# ragagent_client.MCPApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_mcp_server_spec_mcp_server_spec_get**](MCPApi.md#get_mcp_server_spec_mcp_server_spec_get) | **GET** /mcp-server/spec | Get MCP server specification


# **get_mcp_server_spec_mcp_server_spec_get**
> object get_mcp_server_spec_mcp_server_spec_get()

Get MCP server specification

Return a consolidated specification of all tools exposed by the MCP server.

The response contains, for each registered tool:

* name – The public tool name.
* description – Human-readable description.
* parameters – JSON schema for the tool arguments (if available).
* sample_input – An auto-generated example payload that conforms to the
  parameters schema (best-effort).

This endpoint is *read-only* and does **not** proxy the request to the
mounted MCP app – instead it inspects the in-memory ``mcp_server_instance``
that is initialised during application startup.  This keeps the dependency
surface minimal and avoids additional network hops.

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
    api_instance = ragagent_client.MCPApi(api_client)

    try:
        # Get MCP server specification
        api_response = api_instance.get_mcp_server_spec_mcp_server_spec_get()
        print("The response of MCPApi->get_mcp_server_spec_mcp_server_spec_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MCPApi->get_mcp_server_spec_mcp_server_spec_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

