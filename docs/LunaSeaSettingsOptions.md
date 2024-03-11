# LunaSeaSettingsOptions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**webhook_url** | **str** |  | [optional] 
**profile_name** | **str** |  | [optional] 

## Example

```python
from overseerr.models.luna_sea_settings_options import LunaSeaSettingsOptions

# TODO update the JSON string below
json = "{}"
# create an instance of LunaSeaSettingsOptions from a JSON string
luna_sea_settings_options_instance = LunaSeaSettingsOptions.from_json(json)
# print the JSON string representation of the object
print(LunaSeaSettingsOptions.to_json())

# convert the object into a dict
luna_sea_settings_options_dict = luna_sea_settings_options_instance.to_dict()
# create an instance of LunaSeaSettingsOptions from a dict
luna_sea_settings_options_form_dict = luna_sea_settings_options.from_dict(luna_sea_settings_options_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


