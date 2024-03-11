# WebhookSettingsOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhook_url** | **str** |  | [optional] 
**auth_header** | **str** |  | [optional] 
**json_payload** | **str** |  | [optional] 

## Example

```python
from overseerr.models.webhook_settings_options import WebhookSettingsOptions

# TODO update the JSON string below
json = "{}"
# create an instance of WebhookSettingsOptions from a JSON string
webhook_settings_options_instance = WebhookSettingsOptions.from_json(json)
# print the JSON string representation of the object
print(WebhookSettingsOptions.to_json())

# convert the object into a dict
webhook_settings_options_dict = webhook_settings_options_instance.to_dict()
# create an instance of WebhookSettingsOptions from a dict
webhook_settings_options_form_dict = webhook_settings_options.from_dict(webhook_settings_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


