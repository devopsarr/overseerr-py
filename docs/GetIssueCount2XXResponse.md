# GetIssueCount2XXResponse


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
from overseerr.models.get_issue_count2_xx_response import GetIssueCount2XXResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetIssueCount2XXResponse from a JSON string
get_issue_count2_xx_response_instance = GetIssueCount2XXResponse.from_json(json)
# print the JSON string representation of the object
print(GetIssueCount2XXResponse.to_json())

# convert the object into a dict
get_issue_count2_xx_response_dict = get_issue_count2_xx_response_instance.to_dict()
# create an instance of GetIssueCount2XXResponse from a dict
get_issue_count2_xx_response_form_dict = get_issue_count2_xx_response.from_dict(get_issue_count2_xx_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


