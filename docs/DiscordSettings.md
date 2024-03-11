# DiscordSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] 
**types** | **float** |  | [optional] 
**options** | [**DiscordSettingsOptions**](DiscordSettingsOptions.md) |  | [optional] 

## Example

```python
from overseerr.models.discord_settings import DiscordSettings

# TODO update the JSON string below
json = "{}"
# create an instance of DiscordSettings from a JSON string
discord_settings_instance = DiscordSettings.from_json(json)
# print the JSON string representation of the object
print(DiscordSettings.to_json())

# convert the object into a dict
discord_settings_dict = discord_settings_instance.to_dict()
# create an instance of DiscordSettings from a dict
discord_settings_form_dict = discord_settings.from_dict(discord_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


