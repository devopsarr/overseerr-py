# GetIssue200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_info** | [**PageInfo**](PageInfo.md) |  | [optional] 
**results** | [**List[Issue]**](Issue.md) |  | [optional] 

## Example

```python
from overseerr.models.get_issue200_response import GetIssue200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetIssue200Response from a JSON string
get_issue200_response_instance = GetIssue200Response.from_json(json)
# print the JSON string representation of the object
print GetIssue200Response.to_json()

# convert the object into a dict
get_issue200_response_dict = get_issue200_response_instance.to_dict()
# create an instance of GetIssue200Response from a dict
get_issue200_response_form_dict = get_issue200_response.from_dict(get_issue200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


