# GotifySettings


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] 
**types** | **float** |  | [optional] 
**options** | [**GotifySettingsOptions**](GotifySettingsOptions.md) |  | [optional] 

## Example

```python
from overseerr.models.gotify_settings import GotifySettings

# TODO update the JSON string below
json = "{}"
# create an instance of GotifySettings from a JSON string
gotify_settings_instance = GotifySettings.from_json(json)
# print the JSON string representation of the object
print GotifySettings.to_json()

# convert the object into a dict
gotify_settings_dict = gotify_settings_instance.to_dict()
# create an instance of GotifySettings from a dict
gotify_settings_form_dict = gotify_settings.from_dict(gotify_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


