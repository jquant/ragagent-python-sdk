# WABATokenExchangeResponse

Response from Facebook token exchange.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** |  | 
**token_type** | **str** |  | [optional] [default to 'bearer']
**expires_in** | **int** |  | [optional] 

## Example

```python
from ragagent_client.models.waba_token_exchange_response import WABATokenExchangeResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WABATokenExchangeResponse from a JSON string
waba_token_exchange_response_instance = WABATokenExchangeResponse.from_json(json)
# print the JSON string representation of the object
print(WABATokenExchangeResponse.to_json())

# convert the object into a dict
waba_token_exchange_response_dict = waba_token_exchange_response_instance.to_dict()
# create an instance of WABATokenExchangeResponse from a dict
waba_token_exchange_response_from_dict = WABATokenExchangeResponse.from_dict(waba_token_exchange_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


