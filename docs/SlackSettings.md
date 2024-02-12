# SlackSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] 
**types** | **float** |  | [optional] 
**options** | [**SlackSettingsOptions**](SlackSettingsOptions.md) |  | [optional] 

## Example

```python
from overseerr.models.slack_settings import SlackSettings

# TODO update the JSON string below
json = "{}"
# create an instance of SlackSettings from a JSON string
slack_settings_instance = SlackSettings.from_json(json)
# print the JSON string representation of the object
print SlackSettings.to_json()

# convert the object into a dict
slack_settings_dict = slack_settings_instance.to_dict()
# create an instance of SlackSettings from a dict
slack_settings_form_dict = slack_settings.from_dict(slack_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


