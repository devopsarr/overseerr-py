# CreateUserSettingsMainRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | [optional] 

## Example

```python
from overseerr.models.create_user_settings_main_request import CreateUserSettingsMainRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUserSettingsMainRequest from a JSON string
create_user_settings_main_request_instance = CreateUserSettingsMainRequest.from_json(json)
# print the JSON string representation of the object
print(CreateUserSettingsMainRequest.to_json())

# convert the object into a dict
create_user_settings_main_request_dict = create_user_settings_main_request_instance.to_dict()
# create an instance of CreateUserSettingsMainRequest from a dict
create_user_settings_main_request_from_dict = CreateUserSettingsMainRequest.from_dict(create_user_settings_main_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


