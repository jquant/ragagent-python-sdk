# ToolExecutionRequest

Request model for tool execution

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**arguments** | **Dict[str, object]** |  | [optional] 

## Example

```python
from ragagent_client.models.tool_execution_request import ToolExecutionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ToolExecutionRequest from a JSON string
tool_execution_request_instance = ToolExecutionRequest.from_json(json)
# print the JSON string representation of the object
print(ToolExecutionRequest.to_json())

# convert the object into a dict
tool_execution_request_dict = tool_execution_request_instance.to_dict()
# create an instance of ToolExecutionRequest from a dict
tool_execution_request_from_dict = ToolExecutionRequest.from_dict(tool_execution_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


