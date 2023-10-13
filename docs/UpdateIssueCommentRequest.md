# UpdateIssueCommentRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 

## Example

```python
from overseerr.models.update_issue_comment_request import UpdateIssueCommentRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateIssueCommentRequest from a JSON string
update_issue_comment_request_instance = UpdateIssueCommentRequest.from_json(json)
# print the JSON string representation of the object
print UpdateIssueCommentRequest.to_json()

# convert the object into a dict
update_issue_comment_request_dict = update_issue_comment_request_instance.to_dict()
# create an instance of UpdateIssueCommentRequest from a dict
update_issue_comment_request_form_dict = update_issue_comment_request.from_dict(update_issue_comment_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


