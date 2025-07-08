# UIEventPayload


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tenant_id** | **str** |  | 
**user_prompt** | **str** |  | 
**conversation_id** | **str** |  | [optional] 
**request_id** | **str** |  | [optional] 
**source** | **str** |  | [optional] 

## Example

```python
from ragagent_client.models.ui_event_payload import UIEventPayload

# TODO update the JSON string below
json = "{}"
# create an instance of UIEventPayload from a JSON string
ui_event_payload_instance = UIEventPayload.from_json(json)
# print the JSON string representation of the object
print(UIEventPayload.to_json())

# convert the object into a dict
ui_event_payload_dict = ui_event_payload_instance.to_dict()
# create an instance of UIEventPayload from a dict
ui_event_payload_from_dict = UIEventPayload.from_dict(ui_event_payload_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


