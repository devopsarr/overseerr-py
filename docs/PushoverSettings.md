# PushoverSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] 
**types** | **float** |  | [optional] 
**options** | [**PushoverSettingsOptions**](PushoverSettingsOptions.md) |  | [optional] 

## Example

```python
from overseerr.models.pushover_settings import PushoverSettings

# TODO update the JSON string below
json = "{}"
# create an instance of PushoverSettings from a JSON string
pushover_settings_instance = PushoverSettings.from_json(json)
# print the JSON string representation of the object
print PushoverSettings.to_json()

# convert the object into a dict
pushover_settings_dict = pushover_settings_instance.to_dict()
# create an instance of PushoverSettings from a dict
pushover_settings_form_dict = pushover_settings.from_dict(pushover_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


