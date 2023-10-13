# SlackSettingsOptions


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhook_url** | **str** |  | [optional] 

## Example

```python
from overseerr.models.slack_settings_options import SlackSettingsOptions

# TODO update the JSON string below
json = "{}"
# create an instance of SlackSettingsOptions from a JSON string
slack_settings_options_instance = SlackSettingsOptions.from_json(json)
# print the JSON string representation of the object
print SlackSettingsOptions.to_json()

# convert the object into a dict
slack_settings_options_dict = slack_settings_options_instance.to_dict()
# create an instance of SlackSettingsOptions from a dict
slack_settings_options_form_dict = slack_settings_options.from_dict(slack_settings_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


