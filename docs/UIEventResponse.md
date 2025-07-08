# UIEventResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**request_id** | **str** |  | 
**conversation_id** | **str** |  | 
**tenant_id** | **str** |  | 
**agent_response** | **str** |  | 
**timestamp** | **str** |  | 
**status** | **str** |  | 

## Example

```python
from ragagent_client.models.ui_event_response import UIEventResponse

# TODO update the JSON string below
json = "{}"
# create an instance of UIEventResponse from a JSON string
ui_event_response_instance = UIEventResponse.from_json(json)
# print the JSON string representation of the object
print(UIEventResponse.to_json())

# convert the object into a dict
ui_event_response_dict = ui_event_response_instance.to_dict()
# create an instance of UIEventResponse from a dict
ui_event_response_from_dict = UIEventResponse.from_dict(ui_event_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


