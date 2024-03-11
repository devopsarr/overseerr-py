# ListLogs2XXResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**label** | **str** |  | [optional] 
**level** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**timestamp** | **str** |  | [optional] 

## Example

```python
from overseerr.models.list_logs2_xx_response_inner import ListLogs2XXResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListLogs2XXResponseInner from a JSON string
list_logs2_xx_response_inner_instance = ListLogs2XXResponseInner.from_json(json)
# print the JSON string representation of the object
print(ListLogs2XXResponseInner.to_json())

# convert the object into a dict
list_logs2_xx_response_inner_dict = list_logs2_xx_response_inner_instance.to_dict()
# create an instance of ListLogs2XXResponseInner from a dict
list_logs2_xx_response_inner_form_dict = list_logs2_xx_response_inner.from_dict(list_logs2_xx_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


