# PushbulletSettingsOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**access_token** | **str** |  | [optional] 
**channel_tag** | **str** |  | [optional] 

## Example

```python
from overseerr.models.pushbullet_settings_options import PushbulletSettingsOptions

# TODO update the JSON string below
json = "{}"
# create an instance of PushbulletSettingsOptions from a JSON string
pushbullet_settings_options_instance = PushbulletSettingsOptions.from_json(json)
# print the JSON string representation of the object
print(PushbulletSettingsOptions.to_json())

# convert the object into a dict
pushbullet_settings_options_dict = pushbullet_settings_options_instance.to_dict()
# create an instance of PushbulletSettingsOptions from a dict
pushbullet_settings_options_from_dict = PushbulletSettingsOptions.from_dict(pushbullet_settings_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


