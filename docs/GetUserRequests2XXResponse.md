# GetUserRequests2XXResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_info** | [**PageInfo**](PageInfo.md) |  | [optional] 
**results** | [**List[MediaRequest]**](MediaRequest.md) |  | [optional] 

## Example

```python
from overseerr.models.get_user_requests2_xx_response import GetUserRequests2XXResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserRequests2XXResponse from a JSON string
get_user_requests2_xx_response_instance = GetUserRequests2XXResponse.from_json(json)
# print the JSON string representation of the object
print(GetUserRequests2XXResponse.to_json())

# convert the object into a dict
get_user_requests2_xx_response_dict = get_user_requests2_xx_response_instance.to_dict()
# create an instance of GetUserRequests2XXResponse from a dict
get_user_requests2_xx_response_from_dict = GetUserRequests2XXResponse.from_dict(get_user_requests2_xx_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


