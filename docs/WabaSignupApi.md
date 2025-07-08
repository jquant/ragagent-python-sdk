# ragagent_client.WabaSignupApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**complete_waba_signup_waba_signup_complete_post**](WabaSignupApi.md#complete_waba_signup_waba_signup_complete_post) | **POST** /waba-signup/complete | Complete Waba Signup
[**exchange_token_waba_signup_exchange_token_post**](WabaSignupApi.md#exchange_token_waba_signup_exchange_token_post) | **POST** /waba-signup/exchange-token | Exchange Token
[**initiate_waba_signup_waba_signup_initiate_post**](WabaSignupApi.md#initiate_waba_signup_waba_signup_initiate_post) | **POST** /waba-signup/initiate | Initiate Waba Signup
[**waba_signup_demo_waba_signup_demo_get**](WabaSignupApi.md#waba_signup_demo_waba_signup_demo_get) | **GET** /waba-signup/demo | Waba Signup Demo
[**waba_signup_webhook_waba_signup_webhook_post**](WabaSignupApi.md#waba_signup_webhook_waba_signup_webhook_post) | **POST** /waba-signup/webhook | Waba Signup Webhook


# **complete_waba_signup_waba_signup_complete_post**
> WABASignupCompleteResponse complete_waba_signup_waba_signup_complete_post(waba_signup_complete_request)

Complete Waba Signup

Complete WABA signup process and update tenant configuration.

This endpoint processes the signup completion, exchanges tokens, and updates
the tenant configuration with the new WABA credentials.

### Example


```python
import ragagent_client
from ragagent_client.models.waba_signup_complete_request import WABASignupCompleteRequest
from ragagent_client.models.waba_signup_complete_response import WABASignupCompleteResponse
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
    api_instance = ragagent_client.WabaSignupApi(api_client)
    waba_signup_complete_request = ragagent_client.WABASignupCompleteRequest() # WABASignupCompleteRequest | 

    try:
        # Complete Waba Signup
        api_response = api_instance.complete_waba_signup_waba_signup_complete_post(waba_signup_complete_request)
        print("The response of WabaSignupApi->complete_waba_signup_waba_signup_complete_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WabaSignupApi->complete_waba_signup_waba_signup_complete_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **waba_signup_complete_request** | [**WABASignupCompleteRequest**](WABASignupCompleteRequest.md)|  | 

### Return type

[**WABASignupCompleteResponse**](WABASignupCompleteResponse.md)

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

# **exchange_token_waba_signup_exchange_token_post**
> WABATokenExchangeResponse exchange_token_waba_signup_exchange_token_post(waba_token_exchange_request)

Exchange Token

Exchange authorization code for access token.

This endpoint handles the OAuth token exchange with Facebook's Graph API.

### Example


```python
import ragagent_client
from ragagent_client.models.waba_token_exchange_request import WABATokenExchangeRequest
from ragagent_client.models.waba_token_exchange_response import WABATokenExchangeResponse
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
    api_instance = ragagent_client.WabaSignupApi(api_client)
    waba_token_exchange_request = ragagent_client.WABATokenExchangeRequest() # WABATokenExchangeRequest | 

    try:
        # Exchange Token
        api_response = api_instance.exchange_token_waba_signup_exchange_token_post(waba_token_exchange_request)
        print("The response of WabaSignupApi->exchange_token_waba_signup_exchange_token_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WabaSignupApi->exchange_token_waba_signup_exchange_token_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **waba_token_exchange_request** | [**WABATokenExchangeRequest**](WABATokenExchangeRequest.md)|  | 

### Return type

[**WABATokenExchangeResponse**](WABATokenExchangeResponse.md)

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

# **initiate_waba_signup_waba_signup_initiate_post**
> WABASignupSessionResponse initiate_waba_signup_waba_signup_initiate_post(waba_signup_session_request)

Initiate Waba Signup

Initiate WABA signup session.

This endpoint creates a signup session URL for Meta's WABA signup flow.
It uses the Facebook App configuration to generate the session parameters.

### Example


```python
import ragagent_client
from ragagent_client.models.waba_signup_session_request import WABASignupSessionRequest
from ragagent_client.models.waba_signup_session_response import WABASignupSessionResponse
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
    api_instance = ragagent_client.WabaSignupApi(api_client)
    waba_signup_session_request = ragagent_client.WABASignupSessionRequest() # WABASignupSessionRequest | 

    try:
        # Initiate Waba Signup
        api_response = api_instance.initiate_waba_signup_waba_signup_initiate_post(waba_signup_session_request)
        print("The response of WabaSignupApi->initiate_waba_signup_waba_signup_initiate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WabaSignupApi->initiate_waba_signup_waba_signup_initiate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **waba_signup_session_request** | [**WABASignupSessionRequest**](WABASignupSessionRequest.md)|  | 

### Return type

[**WABASignupSessionResponse**](WABASignupSessionResponse.md)

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

# **waba_signup_demo_waba_signup_demo_get**
> object waba_signup_demo_waba_signup_demo_get(tenant_id=tenant_id)

Waba Signup Demo

Serve a demo page for testing WABA Embedded Signup.

This endpoint provides a complete HTML page with the Facebook SDK integration
for testing the embedded signup flow.

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
    api_instance = ragagent_client.WabaSignupApi(api_client)
    tenant_id = 'agm_tw' # str |  (optional) (default to 'agm_tw')

    try:
        # Waba Signup Demo
        api_response = api_instance.waba_signup_demo_waba_signup_demo_get(tenant_id=tenant_id)
        print("The response of WabaSignupApi->waba_signup_demo_waba_signup_demo_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WabaSignupApi->waba_signup_demo_waba_signup_demo_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tenant_id** | **str**|  | [optional] [default to &#39;agm_tw&#39;]

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

# **waba_signup_webhook_waba_signup_webhook_post**
> object waba_signup_webhook_waba_signup_webhook_post()

Waba Signup Webhook

Handle webhook events from Facebook WABA Embedded Signup.

This endpoint receives message events and other notifications from the
embedded signup flow.

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
    api_instance = ragagent_client.WabaSignupApi(api_client)

    try:
        # Waba Signup Webhook
        api_response = api_instance.waba_signup_webhook_waba_signup_webhook_post()
        print("The response of WabaSignupApi->waba_signup_webhook_waba_signup_webhook_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling WabaSignupApi->waba_signup_webhook_waba_signup_webhook_post: %s\n" % e)
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

