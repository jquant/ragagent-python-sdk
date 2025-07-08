# SignupData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone_number_id** | **str** | Customer&#39;s business phone number ID | 
**waba_id** | **str** | Customer&#39;s WhatsApp Business Account ID | 
**business_id** | **str** | Customer&#39;s business portfolio ID | 
**current_step** | **str** | Screen where customer abandoned the flow | 
**error_message** | **str** | Error description displayed to customer | 
**error_id** | **str** | Error ID for support | 
**session_id** | **str** | Unique session ID for support | 
**timestamp** | **int** | Unix timestamp when error was reported | 

## Example

```python
from ragagent_client.models.signup_data import SignupData

# TODO update the JSON string below
json = "{}"
# create an instance of SignupData from a JSON string
signup_data_instance = SignupData.from_json(json)
# print the JSON string representation of the object
print(SignupData.to_json())

# convert the object into a dict
signup_data_dict = signup_data_instance.to_dict()
# create an instance of SignupData from a dict
signup_data_from_dict = SignupData.from_dict(signup_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


