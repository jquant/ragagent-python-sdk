# WABASignupSessionRequest

Request to initiate WABA signup session.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | 
**redirect_uri** | **str** |  | [optional] 
**feature_type** | **str** |  | [optional] 

## Example

```python
from ragagent_client.models.waba_signup_session_request import WABASignupSessionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of WABASignupSessionRequest from a JSON string
waba_signup_session_request_instance = WABASignupSessionRequest.from_json(json)
# print the JSON string representation of the object
print(WABASignupSessionRequest.to_json())

# convert the object into a dict
waba_signup_session_request_dict = waba_signup_session_request_instance.to_dict()
# create an instance of WABASignupSessionRequest from a dict
waba_signup_session_request_from_dict = WABASignupSessionRequest.from_dict(waba_signup_session_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


