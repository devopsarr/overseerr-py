# MainSettings


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**api_key** | **str** |  | [optional] [readonly] 
**app_language** | **str** |  | [optional] 
**application_title** | **str** |  | [optional] 
**application_url** | **str** |  | [optional] 
**trust_proxy** | **bool** |  | [optional] 
**csrf_protection** | **bool** |  | [optional] 
**hide_available** | **bool** |  | [optional] 
**partial_requests_enabled** | **bool** |  | [optional] 
**local_login** | **bool** |  | [optional] 
**new_plex_login** | **bool** |  | [optional] 
**default_permissions** | **float** |  | [optional] 

## Example

```python
from overseerr.models.main_settings import MainSettings

# TODO update the JSON string below
json = "{}"
# create an instance of MainSettings from a JSON string
main_settings_instance = MainSettings.from_json(json)
# print the JSON string representation of the object
print MainSettings.to_json()

# convert the object into a dict
main_settings_dict = main_settings_instance.to_dict()
# create an instance of MainSettings from a dict
main_settings_form_dict = main_settings.from_dict(main_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


