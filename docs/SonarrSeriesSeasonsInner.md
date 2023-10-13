# SonarrSeriesSeasonsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**season_number** | **float** |  | [optional] 
**monitored** | **bool** |  | [optional] 

## Example

```python
from overseerr.models.sonarr_series_seasons_inner import SonarrSeriesSeasonsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SonarrSeriesSeasonsInner from a JSON string
sonarr_series_seasons_inner_instance = SonarrSeriesSeasonsInner.from_json(json)
# print the JSON string representation of the object
print SonarrSeriesSeasonsInner.to_json()

# convert the object into a dict
sonarr_series_seasons_inner_dict = sonarr_series_seasons_inner_instance.to_dict()
# create an instance of SonarrSeriesSeasonsInner from a dict
sonarr_series_seasons_inner_form_dict = sonarr_series_seasons_inner.from_dict(sonarr_series_seasons_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


