# TautulliSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hostname** | **str** |  | [optional] 
**port** | **float** |  | [optional] 
**use_ssl** | **bool** |  | [optional] 
**api_key** | **str** |  | [optional] 
**external_url** | **str** |  | [optional] 

## Example

```python
from overseerr.models.tautulli_settings import TautulliSettings

# TODO update the JSON string below
json = "{}"
# create an instance of TautulliSettings from a JSON string
tautulli_settings_instance = TautulliSettings.from_json(json)
# print the JSON string representation of the object
print(TautulliSettings.to_json())

# convert the object into a dict
tautulli_settings_dict = tautulli_settings_instance.to_dict()
# create an instance of TautulliSettings from a dict
tautulli_settings_form_dict = tautulli_settings.from_dict(tautulli_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


