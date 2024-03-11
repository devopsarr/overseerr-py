# CreateUserSettingsPermissionsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**permissions** | **float** |  | 

## Example

```python
from overseerr.models.create_user_settings_permissions_request import CreateUserSettingsPermissionsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUserSettingsPermissionsRequest from a JSON string
create_user_settings_permissions_request_instance = CreateUserSettingsPermissionsRequest.from_json(json)
# print the JSON string representation of the object
print(CreateUserSettingsPermissionsRequest.to_json())

# convert the object into a dict
create_user_settings_permissions_request_dict = create_user_settings_permissions_request_instance.to_dict()
# create an instance of CreateUserSettingsPermissionsRequest from a dict
create_user_settings_permissions_request_form_dict = create_user_settings_permissions_request.from_dict(create_user_settings_permissions_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


