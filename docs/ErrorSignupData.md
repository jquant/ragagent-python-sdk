# ErrorSignupData

Data structure for error reported during WABA signup.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error_message** | **str** | Error description displayed to customer | 
**error_id** | **str** | Error ID for support | 
**session_id** | **str** | Unique session ID for support | 
**timestamp** | **int** | Unix timestamp when error was reported | 

## Example

```python
from ragagent_client.models.error_signup_data import ErrorSignupData

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorSignupData from a JSON string
error_signup_data_instance = ErrorSignupData.from_json(json)
# print the JSON string representation of the object
print(ErrorSignupData.to_json())

# convert the object into a dict
error_signup_data_dict = error_signup_data_instance.to_dict()
# create an instance of ErrorSignupData from a dict
error_signup_data_from_dict = ErrorSignupData.from_dict(error_signup_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


