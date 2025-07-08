# WABASignupCompleteResponse

Response after completing WABA signup.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | 
**waba_id** | **str** |  | [optional] 
**phone_number_id** | **str** |  | [optional] 
**business_id** | **str** |  | [optional] 
**access_token** | **str** |  | [optional] 
**error** | **str** |  | [optional] 

## Example

```python
from ragagent_client.models.waba_signup_complete_response import WABASignupCompleteResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WABASignupCompleteResponse from a JSON string
waba_signup_complete_response_instance = WABASignupCompleteResponse.from_json(json)
# print the JSON string representation of the object
print(WABASignupCompleteResponse.to_json())

# convert the object into a dict
waba_signup_complete_response_dict = waba_signup_complete_response_instance.to_dict()
# create an instance of WABASignupCompleteResponse from a dict
waba_signup_complete_response_from_dict = WABASignupCompleteResponse.from_dict(waba_signup_complete_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


