# GetUser2XXResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page_info** | [**PageInfo**](PageInfo.md) |  | [optional] 
**results** | [**User[User]**](User.md) |  | [optional] 

## Example

```python
from overseerr.models.get_user2_xx_response import GetUser2XXResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetUser2XXResponse from a JSON string
get_user2_xx_response_instance = GetUser2XXResponse.from_json(json)
# print the JSON string representation of the object
print(GetUser2XXResponse.to_json())

# convert the object into a dict
get_user2_xx_response_dict = get_user2_xx_response_instance.to_dict()
# create an instance of GetUser2XXResponse from a dict
get_user2_xx_response_form_dict = get_user2_xx_response.from_dict(get_user2_xx_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


