# GetIssue2XXResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_info** | [**PageInfo**](PageInfo.md) |  | [optional] 
**results** | [**List[Issue]**](Issue.md) |  | [optional] 

## Example

```python
from overseerr.models.get_issue2_xx_response import GetIssue2XXResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetIssue2XXResponse from a JSON string
get_issue2_xx_response_instance = GetIssue2XXResponse.from_json(json)
# print the JSON string representation of the object
print(GetIssue2XXResponse.to_json())

# convert the object into a dict
get_issue2_xx_response_dict = get_issue2_xx_response_instance.to_dict()
# create an instance of GetIssue2XXResponse from a dict
get_issue2_xx_response_from_dict = GetIssue2XXResponse.from_dict(get_issue2_xx_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


