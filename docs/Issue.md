# Issue


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** |  | [optional] 
**issue_type** | **float** |  | [optional] 
**media** | [**MediaInfo**](MediaInfo.md) |  | [optional] 
**created_by** | [**User**](User.md) |  | [optional] 
**modified_by** | [**User**](User.md) |  | [optional] 
**comments** | [**List[IssueComment]**](IssueComment.md) |  | [optional] 

## Example

```python
from overseerr.models.issue import Issue

# TODO update the JSON string below
json = "{}"
# create an instance of Issue from a JSON string
issue_instance = Issue.from_json(json)
# print the JSON string representation of the object
print(Issue.to_json())

# convert the object into a dict
issue_dict = issue_instance.to_dict()
# create an instance of Issue from a dict
issue_from_dict = Issue.from_dict(issue_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


