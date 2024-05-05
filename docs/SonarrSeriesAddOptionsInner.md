# SonarrSeriesAddOptionsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ignore_episodes_with_files** | **bool** |  | [optional] 
**ignore_episodes_without_files** | **bool** |  | [optional] 
**search_for_missing_episodes** | **bool** |  | [optional] 

## Example

```python
from overseerr.models.sonarr_series_add_options_inner import SonarrSeriesAddOptionsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SonarrSeriesAddOptionsInner from a JSON string
sonarr_series_add_options_inner_instance = SonarrSeriesAddOptionsInner.from_json(json)
# print the JSON string representation of the object
print(SonarrSeriesAddOptionsInner.to_json())

# convert the object into a dict
sonarr_series_add_options_inner_dict = sonarr_series_add_options_inner_instance.to_dict()
# create an instance of SonarrSeriesAddOptionsInner from a dict
sonarr_series_add_options_inner_from_dict = SonarrSeriesAddOptionsInner.from_dict(sonarr_series_add_options_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


