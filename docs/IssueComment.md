# IssueComment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** |  | [optional] 
**user** | [**User**](User.md) |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from overseerr.models.issue_comment import IssueComment

# TODO update the JSON string below
json = "{}"
# create an instance of IssueComment from a JSON string
issue_comment_instance = IssueComment.from_json(json)
# print the JSON string representation of the object
print(IssueComment.to_json())

# convert the object into a dict
issue_comment_dict = issue_comment_instance.to_dict()
# create an instance of IssueComment from a dict
issue_comment_from_dict = IssueComment.from_dict(issue_comment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


