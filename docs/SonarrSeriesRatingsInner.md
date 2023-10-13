# SonarrSeriesRatingsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**votes** | **float** |  | [optional] 
**value** | **float** |  | [optional] 

## Example

```python
from overseerr.models.sonarr_series_ratings_inner import SonarrSeriesRatingsInner

# TODO update the JSON string below
json = "{}"
# create an instance of SonarrSeriesRatingsInner from a JSON string
sonarr_series_ratings_inner_instance = SonarrSeriesRatingsInner.from_json(json)
# print the JSON string representation of the object
print SonarrSeriesRatingsInner.to_json()

# convert the object into a dict
sonarr_series_ratings_inner_dict = sonarr_series_ratings_inner_instance.to_dict()
# create an instance of SonarrSeriesRatingsInner from a dict
sonarr_series_ratings_inner_form_dict = sonarr_series_ratings_inner.from_dict(sonarr_series_ratings_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


