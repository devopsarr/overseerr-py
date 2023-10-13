# GetUserRequests200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_info** | [**PageInfo**](PageInfo.md) |  | [optional] 
**results** | [**List[MediaRequest]**](MediaRequest.md) |  | [optional] 

## Example

```python
from overseerr.models.get_user_requests200_response import GetUserRequests200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserRequests200Response from a JSON string
get_user_requests200_response_instance = GetUserRequests200Response.from_json(json)
# print the JSON string representation of the object
print GetUserRequests200Response.to_json()

# convert the object into a dict
get_user_requests200_response_dict = get_user_requests200_response_instance.to_dict()
# create an instance of GetUserRequests200Response from a dict
get_user_requests200_response_form_dict = get_user_requests200_response.from_dict(get_user_requests200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


