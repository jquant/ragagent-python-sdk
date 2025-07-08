# SuccessfulSignupData

Data structure for successful WABA signup completion.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**phone_number_id** | **str** | Customer&#39;s business phone number ID | 
**waba_id** | **str** | Customer&#39;s WhatsApp Business Account ID | 
**business_id** | **str** | Customer&#39;s business portfolio ID | 

## Example

```python
from ragagent_client.models.successful_signup_data import SuccessfulSignupData

# TODO update the JSON string below
json = "{}"
# create an instance of SuccessfulSignupData from a JSON string
successful_signup_data_instance = SuccessfulSignupData.from_json(json)
# print the JSON string representation of the object
print(SuccessfulSignupData.to_json())

# convert the object into a dict
successful_signup_data_dict = successful_signup_data_instance.to_dict()
# create an instance of SuccessfulSignupData from a dict
successful_signup_data_from_dict = SuccessfulSignupData.from_dict(successful_signup_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


