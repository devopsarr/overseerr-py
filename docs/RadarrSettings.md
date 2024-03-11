# RadarrSettings


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
**is4k** | **bool** |  | 
**minimum_availability** | **str** |  | 
**is_default** | **bool** |  | 
**external_url** | **str** |  | [optional] 
**sync_enabled** | **bool** |  | [optional] 
**prevent_search** | **bool** |  | [optional] 

## Example

```python
from overseerr.models.radarr_settings import RadarrSettings

# TODO update the JSON string below
json = "{}"
# create an instance of RadarrSettings from a JSON string
radarr_settings_instance = RadarrSettings.from_json(json)
# print the JSON string representation of the object
print(RadarrSettings.to_json())

# convert the object into a dict
radarr_settings_dict = radarr_settings_instance.to_dict()
# create an instance of RadarrSettings from a dict
radarr_settings_form_dict = radarr_settings.from_dict(radarr_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


