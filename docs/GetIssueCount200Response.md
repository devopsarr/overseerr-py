# GetIssueCount200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **float** |  | [optional] 
**video** | **float** |  | [optional] 
**audio** | **float** |  | [optional] 
**subtitles** | **float** |  | [optional] 
**others** | **float** |  | [optional] 
**open** | **float** |  | [optional] 
**closed** | **float** |  | [optional] 

## Example

```python
from overseerr.models.get_issue_count200_response import GetIssueCount200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetIssueCount200Response from a JSON string
get_issue_count200_response_instance = GetIssueCount200Response.from_json(json)
# print the JSON string representation of the object
print GetIssueCount200Response.to_json()

# convert the object into a dict
get_issue_count200_response_dict = get_issue_count200_response_instance.to_dict()
# create an instance of GetIssueCount200Response from a dict
get_issue_count200_response_form_dict = get_issue_count200_response.from_dict(get_issue_count200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


