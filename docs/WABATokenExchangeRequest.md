# WABATokenExchangeRequest

Request to exchange authorization code for access token.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_id** | **str** |  | 
**client_secret** | **str** |  | 
**code** | **str** |  | 
**redirect_uri** | **str** |  | [optional] 

## Example

```python
from ragagent_client.models.waba_token_exchange_request import WABATokenExchangeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WABATokenExchangeRequest from a JSON string
waba_token_exchange_request_instance = WABATokenExchangeRequest.from_json(json)
# print the JSON string representation of the object
print(WABATokenExchangeRequest.to_json())

# convert the object into a dict
waba_token_exchange_request_dict = waba_token_exchange_request_instance.to_dict()
# create an instance of WABATokenExchangeRequest from a dict
waba_token_exchange_request_from_dict = WABATokenExchangeRequest.from_dict(waba_token_exchange_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


