# CreateUserSettingsPasswordRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_password** | **str** |  | [optional] 
**new_password** | **str** |  | 

## Example

```python
from overseerr.models.create_user_settings_password_request import CreateUserSettingsPasswordRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUserSettingsPasswordRequest from a JSON string
create_user_settings_password_request_instance = CreateUserSettingsPasswordRequest.from_json(json)
# print the JSON string representation of the object
print CreateUserSettingsPasswordRequest.to_json()

# convert the object into a dict
create_user_settings_password_request_dict = create_user_settings_password_request_instance.to_dict()
# create an instance of CreateUserSettingsPasswordRequest from a dict
create_user_settings_password_request_form_dict = create_user_settings_password_request.from_dict(create_user_settings_password_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


