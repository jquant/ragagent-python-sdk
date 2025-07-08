# ragagent_client.CicApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**download_local_file_cic_search_download_local_task_id_get**](CicApi.md#download_local_file_cic_search_download_local_task_id_get) | **GET** /cic/search/download-local/{task_id} | Download Local File
[**get_task_download_url_cic_search_download_task_id_get**](CicApi.md#get_task_download_url_cic_search_download_task_id_get) | **GET** /cic/search/download/{task_id} | Get Task Download Url
[**get_task_results_cic_search_results_task_id_get**](CicApi.md#get_task_results_cic_search_results_task_id_get) | **GET** /cic/search/results/{task_id} | Get Task Results
[**get_task_status_cic_search_status_task_id_get**](CicApi.md#get_task_status_cic_search_status_task_id_get) | **GET** /cic/search/status/{task_id} | Get Task Status
[**process_cic_search_cic_search_post**](CicApi.md#process_cic_search_cic_search_post) | **POST** /cic/search | Process Cic Search


# **download_local_file_cic_search_download_local_task_id_get**
> object download_local_file_cic_search_download_local_task_id_get(task_id)

Download Local File

Download the task results directly from local storage

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
    api_instance = ragagent_client.CicApi(api_client)
    task_id = 'task_id_example' # str | 

    try:
        # Download Local File
        api_response = api_instance.download_local_file_cic_search_download_local_task_id_get(task_id)
        print("The response of CicApi->download_local_file_cic_search_download_local_task_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CicApi->download_local_file_cic_search_download_local_task_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**|  | 

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

# **get_task_download_url_cic_search_download_task_id_get**
> Dict[str, Optional[str]] get_task_download_url_cic_search_download_task_id_get(task_id)

Get Task Download Url

Get a download URL for the task results from blob storage

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
    api_instance = ragagent_client.CicApi(api_client)
    task_id = 'task_id_example' # str | 

    try:
        # Get Task Download Url
        api_response = api_instance.get_task_download_url_cic_search_download_task_id_get(task_id)
        print("The response of CicApi->get_task_download_url_cic_search_download_task_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CicApi->get_task_download_url_cic_search_download_task_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**|  | 

### Return type

**Dict[str, Optional[str]]**

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

# **get_task_results_cic_search_results_task_id_get**
> Dict[str, object] get_task_results_cic_search_results_task_id_get(task_id)

Get Task Results

Get the final results of a completed CIC processing task

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
    api_instance = ragagent_client.CicApi(api_client)
    task_id = 'task_id_example' # str | 

    try:
        # Get Task Results
        api_response = api_instance.get_task_results_cic_search_results_task_id_get(task_id)
        print("The response of CicApi->get_task_results_cic_search_results_task_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CicApi->get_task_results_cic_search_results_task_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**|  | 

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
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_task_status_cic_search_status_task_id_get**
> Dict[str, object] get_task_status_cic_search_status_task_id_get(task_id)

Get Task Status

Get the status of a CIC processing task

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
    api_instance = ragagent_client.CicApi(api_client)
    task_id = 'task_id_example' # str | 

    try:
        # Get Task Status
        api_response = api_instance.get_task_status_cic_search_status_task_id_get(task_id)
        print("The response of CicApi->get_task_status_cic_search_status_task_id_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CicApi->get_task_status_cic_search_status_task_id_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **task_id** | **str**|  | 

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
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **process_cic_search_cic_search_post**
> Dict[str, object] process_cic_search_cic_search_post(file, cic_column=cic_column, max_cics=max_cics, parallel_workers=parallel_workers, server_url=server_url)

Process Cic Search

Process CICs from a CSV or XLSX file through the CobranSaaS search and CSV update tools with parallelism.

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
    api_instance = ragagent_client.CicApi(api_client)
    file = None # bytearray | CSV or XLSX file containing CICs
    cic_column = 'NO_CPF_CNPJ' # str | Column name containing CICs (optional) (default to 'NO_CPF_CNPJ')
    max_cics = 10000 # int | Maximum number of CICs to process (optional) (default to 10000)
    parallel_workers = 5 # int | Number of parallel workers (1-20) (optional) (default to 5)
    server_url = 'http://localhost:8006/mcp' # str | MCP server URL (optional) (default to 'http://localhost:8006/mcp')

    try:
        # Process Cic Search
        api_response = api_instance.process_cic_search_cic_search_post(file, cic_column=cic_column, max_cics=max_cics, parallel_workers=parallel_workers, server_url=server_url)
        print("The response of CicApi->process_cic_search_cic_search_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CicApi->process_cic_search_cic_search_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **bytearray**| CSV or XLSX file containing CICs | 
 **cic_column** | **str**| Column name containing CICs | [optional] [default to &#39;NO_CPF_CNPJ&#39;]
 **max_cics** | **int**| Maximum number of CICs to process | [optional] [default to 10000]
 **parallel_workers** | **int**| Number of parallel workers (1-20) | [optional] [default to 5]
 **server_url** | **str**| MCP server URL | [optional] [default to &#39;http://localhost:8006/mcp&#39;]

### Return type

**Dict[str, object]**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful Response |  -  |
**422** | Validation Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

