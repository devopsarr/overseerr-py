# SonarrSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** |  | [optional] [readonly] 
**name** | **str** |  | 
**hostname** | **str** |  | 
**port** | **float** |  | 
**api_key** | **str** |  | 
**use_ssl** | **bool** |  | 
**base_url** | **str** |  | [optional] 
**active_profile_id** | **float** |  | 
**active_profile_name** | **str** |  | 
**active_directory** | **str** |  | 
**active_language_profile_id** | **float** |  | [optional] 
**active_anime_profile_id** | **float** |  | [optional] 
**active_anime_language_profile_id** | **float** |  | [optional] 
**active_anime_profile_name** | **str** |  | [optional] 
**active_anime_directory** | **str** |  | [optional] 
**is4k** | **bool** |  | 
**enable_season_folders** | **bool** |  | 
**is_default** | **bool** |  | 
**external_url** | **str** |  | [optional] 
**sync_enabled** | **bool** |  | [optional] 
**prevent_search** | **bool** |  | [optional] 

## Example

```python
from overseerr.models.sonarr_settings import SonarrSettings

# TODO update the JSON string below
json = "{}"
# create an instance of SonarrSettings from a JSON string
sonarr_settings_instance = SonarrSettings.from_json(json)
# print the JSON string representation of the object
print(SonarrSettings.to_json())

# convert the object into a dict
sonarr_settings_dict = sonarr_settings_instance.to_dict()
# create an instance of SonarrSettings from a dict
sonarr_settings_form_dict = sonarr_settings.from_dict(sonarr_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


