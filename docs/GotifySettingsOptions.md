# GotifySettingsOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 
**token** | **str** |  | [optional] 

## Example

```python
from overseerr.models.gotify_settings_options import GotifySettingsOptions

# TODO update the JSON string below
json = "{}"
# create an instance of GotifySettingsOptions from a JSON string
gotify_settings_options_instance = GotifySettingsOptions.from_json(json)
# print the JSON string representation of the object
print(GotifySettingsOptions.to_json())

# convert the object into a dict
gotify_settings_options_dict = gotify_settings_options_instance.to_dict()
# create an instance of GotifySettingsOptions from a dict
gotify_settings_options_form_dict = gotify_settings_options.from_dict(gotify_settings_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


