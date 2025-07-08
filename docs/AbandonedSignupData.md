# AbandonedSignupData

Data structure for abandoned WABA signup flow.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_step** | **str** | Screen where customer abandoned the flow | 

## Example

```python
from ragagent_client.models.abandoned_signup_data import AbandonedSignupData

# TODO update the JSON string below
json = "{}"
# create an instance of AbandonedSignupData from a JSON string
abandoned_signup_data_instance = AbandonedSignupData.from_json(json)
# print the JSON string representation of the object
print(AbandonedSignupData.to_json())

# convert the object into a dict
abandoned_signup_data_dict = abandoned_signup_data_instance.to_dict()
# create an instance of AbandonedSignupData from a dict
abandoned_signup_data_from_dict = AbandonedSignupData.from_dict(abandoned_signup_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


