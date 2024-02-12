# TelegramSettingsOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bot_username** | **str** |  | [optional] 
**bot_api** | **str** |  | [optional] 
**chat_id** | **str** |  | [optional] 
**send_silently** | **bool** |  | [optional] 

## Example

```python
from overseerr.models.telegram_settings_options import TelegramSettingsOptions

# TODO update the JSON string below
json = "{}"
# create an instance of TelegramSettingsOptions from a JSON string
telegram_settings_options_instance = TelegramSettingsOptions.from_json(json)
# print the JSON string representation of the object
print TelegramSettingsOptions.to_json()

# convert the object into a dict
telegram_settings_options_dict = telegram_settings_options_instance.to_dict()
# create an instance of TelegramSettingsOptions from a dict
telegram_settings_options_form_dict = telegram_settings_options.from_dict(telegram_settings_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


