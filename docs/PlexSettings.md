# PlexSettings


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [readonly] 
**machine_id** | **str** |  | [readonly] 
**ip** | **str** |  | 
**port** | **float** |  | 
**use_ssl** | **bool** |  | [optional] 
**libraries** | [**List[PlexLibrary]**](PlexLibrary.md) |  | [optional] [readonly] 
**web_app_url** | **str** |  | [optional] 

## Example

```python
from overseerr.models.plex_settings import PlexSettings

# TODO update the JSON string below
json = "{}"
# create an instance of PlexSettings from a JSON string
plex_settings_instance = PlexSettings.from_json(json)
# print the JSON string representation of the object
print PlexSettings.to_json()

# convert the object into a dict
plex_settings_dict = plex_settings_instance.to_dict()
# create an instance of PlexSettings from a dict
plex_settings_form_dict = plex_settings.from_dict(plex_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


