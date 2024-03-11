# PushoverSettingsOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** |  | [optional] 
**user_token** | **str** |  | [optional] 

## Example

```python
from overseerr.models.pushover_settings_options import PushoverSettingsOptions

# TODO update the JSON string below
json = "{}"
# create an instance of PushoverSettingsOptions from a JSON string
pushover_settings_options_instance = PushoverSettingsOptions.from_json(json)
# print the JSON string representation of the object
print(PushoverSettingsOptions.to_json())

# convert the object into a dict
pushover_settings_options_dict = pushover_settings_options_instance.to_dict()
# create an instance of PushoverSettingsOptions from a dict
pushover_settings_options_form_dict = pushover_settings_options.from_dict(pushover_settings_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


