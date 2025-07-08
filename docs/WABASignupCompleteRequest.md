# WABASignupCompleteRequest

Request to complete WABA signup process.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | 
**auth_code** | **str** |  | 
**signup_data** | [**SignupData**](SignupData.md) |  | 
**session_id** | **str** |  | [optional] 

## Example

```python
from ragagent_client.models.waba_signup_complete_request import WABASignupCompleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WABASignupCompleteRequest from a JSON string
waba_signup_complete_request_instance = WABASignupCompleteRequest.from_json(json)
# print the JSON string representation of the object
print(WABASignupCompleteRequest.to_json())

# convert the object into a dict
waba_signup_complete_request_dict = waba_signup_complete_request_instance.to_dict()
# create an instance of WABASignupCompleteRequest from a dict
waba_signup_complete_request_from_dict = WABASignupCompleteRequest.from_dict(waba_signup_complete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


