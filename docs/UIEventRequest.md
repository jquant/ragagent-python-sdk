# UIEventRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | 
**user_prompt** | **str** |  | 
**conversation_id** | **str** |  | [optional] [default to '']
**source** | **str** |  | [optional] [default to '']
**request_id** | **str** |  | [optional] [default to '']

## Example

```python
from ragagent_client.models.ui_event_request import UIEventRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UIEventRequest from a JSON string
ui_event_request_instance = UIEventRequest.from_json(json)
# print the JSON string representation of the object
print(UIEventRequest.to_json())

# convert the object into a dict
ui_event_request_dict = ui_event_request_instance.to_dict()
# create an instance of UIEventRequest from a dict
ui_event_request_from_dict = UIEventRequest.from_dict(ui_event_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


