# GetUserQuota200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**movie** | [**GetUserQuota200ResponseMovie**](GetUserQuota200ResponseMovie.md) |  | [optional] 
**tv** | [**GetUserQuota200ResponseMovie**](GetUserQuota200ResponseMovie.md) |  | [optional] 

## Example

```python
from overseerr.models.get_user_quota200_response import GetUserQuota200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserQuota200Response from a JSON string
get_user_quota200_response_instance = GetUserQuota200Response.from_json(json)
# print the JSON string representation of the object
print GetUserQuota200Response.to_json()

# convert the object into a dict
get_user_quota200_response_dict = get_user_quota200_response_instance.to_dict()
# create an instance of GetUserQuota200Response from a dict
get_user_quota200_response_form_dict = get_user_quota200_response.from_dict(get_user_quota200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


