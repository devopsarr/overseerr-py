# TelegramSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] 
**types** | **float** |  | [optional] 
**options** | [**TelegramSettingsOptions**](TelegramSettingsOptions.md) |  | [optional] 

## Example

```python
from overseerr.models.telegram_settings import TelegramSettings

# TODO update the JSON string below
json = "{}"
# create an instance of TelegramSettings from a JSON string
telegram_settings_instance = TelegramSettings.from_json(json)
# print the JSON string representation of the object
print(TelegramSettings.to_json())

# convert the object into a dict
telegram_settings_dict = telegram_settings_instance.to_dict()
# create an instance of TelegramSettings from a dict
telegram_settings_form_dict = telegram_settings.from_dict(telegram_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


