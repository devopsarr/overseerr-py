# CreateIssueRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**issue_type** | **float** |  | [optional] 
**message** | **str** |  | [optional] 
**media_id** | **float** |  | [optional] 

## Example

```python
from overseerr.models.create_issue_request import CreateIssueRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateIssueRequest from a JSON string
create_issue_request_instance = CreateIssueRequest.from_json(json)
# print the JSON string representation of the object
print(CreateIssueRequest.to_json())

# convert the object into a dict
create_issue_request_dict = create_issue_request_instance.to_dict()
# create an instance of CreateIssueRequest from a dict
create_issue_request_from_dict = CreateIssueRequest.from_dict(create_issue_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


