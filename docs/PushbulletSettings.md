# PushbulletSettings


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] 
**types** | **float** |  | [optional] 
**options** | [**PushbulletSettingsOptions**](PushbulletSettingsOptions.md) |  | [optional] 

## Example

```python
from overseerr.models.pushbullet_settings import PushbulletSettings

# TODO update the JSON string below
json = "{}"
# create an instance of PushbulletSettings from a JSON string
pushbullet_settings_instance = PushbulletSettings.from_json(json)
# print the JSON string representation of the object
print PushbulletSettings.to_json()

# convert the object into a dict
pushbullet_settings_dict = pushbullet_settings_instance.to_dict()
# create an instance of PushbulletSettings from a dict
pushbullet_settings_form_dict = pushbullet_settings.from_dict(pushbullet_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


