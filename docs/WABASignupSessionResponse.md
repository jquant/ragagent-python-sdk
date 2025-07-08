# WABASignupSessionResponse

Response with signup session configuration.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **str** |  | 
**configuration_id** | **str** |  | 
**graph_api_version** | **str** |  | 
**feature_type** | **str** |  | [optional] 
**redirect_uri** | **str** |  | [optional] 

## Example

```python
from ragagent_client.models.waba_signup_session_response import WABASignupSessionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of WABASignupSessionResponse from a JSON string
waba_signup_session_response_instance = WABASignupSessionResponse.from_json(json)
# print the JSON string representation of the object
print(WABASignupSessionResponse.to_json())

# convert the object into a dict
waba_signup_session_response_dict = waba_signup_session_response_instance.to_dict()
# create an instance of WABASignupSessionResponse from a dict
waba_signup_session_response_from_dict = WABASignupSessionResponse.from_dict(waba_signup_session_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


