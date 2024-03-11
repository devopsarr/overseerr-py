# GetUserQuota2XXResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**movie** | [**GetUserQuota2XXResponseMovie**](GetUserQuota2XXResponseMovie.md) |  | [optional] 
**tv** | [**GetUserQuota2XXResponseMovie**](GetUserQuota2XXResponseMovie.md) |  | [optional] 

## Example

```python
from overseerr.models.get_user_quota2_xx_response import GetUserQuota2XXResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserQuota2XXResponse from a JSON string
get_user_quota2_xx_response_instance = GetUserQuota2XXResponse.from_json(json)
# print the JSON string representation of the object
print(GetUserQuota2XXResponse.to_json())

# convert the object into a dict
get_user_quota2_xx_response_dict = get_user_quota2_xx_response_instance.to_dict()
# create an instance of GetUserQuota2XXResponse from a dict
get_user_quota2_xx_response_form_dict = get_user_quota2_xx_response.from_dict(get_user_quota2_xx_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


