# DiscordSettingsOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bot_username** | **str** |  | [optional] 
**bot_avatar_url** | **str** |  | [optional] 
**webhook_url** | **str** |  | [optional] 
**enable_mentions** | **bool** |  | [optional] 

## Example

```python
from overseerr.models.discord_settings_options import DiscordSettingsOptions

# TODO update the JSON string below
json = "{}"
# create an instance of DiscordSettingsOptions from a JSON string
discord_settings_options_instance = DiscordSettingsOptions.from_json(json)
# print the JSON string representation of the object
print(DiscordSettingsOptions.to_json())

# convert the object into a dict
discord_settings_options_dict = discord_settings_options_instance.to_dict()
# create an instance of DiscordSettingsOptions from a dict
discord_settings_options_form_dict = discord_settings_options.from_dict(discord_settings_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


