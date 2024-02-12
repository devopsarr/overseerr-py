# SonarrSeries


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**sort_title** | **str** |  | [optional] 
**season_count** | **float** |  | [optional] 
**status** | **str** |  | [optional] 
**overview** | **str** |  | [optional] 
**network** | **str** |  | [optional] 
**air_time** | **str** |  | [optional] 
**images** | [**List[SonarrSeriesImagesInner]**](SonarrSeriesImagesInner.md) |  | [optional] 
**remote_poster** | **str** |  | [optional] 
**seasons** | [**List[SonarrSeriesSeasonsInner]**](SonarrSeriesSeasonsInner.md) |  | [optional] 
**year** | **float** |  | [optional] 
**path** | **str** |  | [optional] 
**profile_id** | **float** |  | [optional] 
**language_profile_id** | **float** |  | [optional] 
**season_folder** | **bool** |  | [optional] 
**monitored** | **bool** |  | [optional] 
**use_scene_numbering** | **bool** |  | [optional] 
**runtime** | **float** |  | [optional] 
**tvdb_id** | **float** |  | [optional] 
**tv_rage_id** | **float** |  | [optional] 
**tv_maze_id** | **float** |  | [optional] 
**first_aired** | **str** |  | [optional] 
**last_info_sync** | **str** |  | [optional] 
**series_type** | **str** |  | [optional] 
**clean_title** | **str** |  | [optional] 
**imdb_id** | **str** |  | [optional] 
**title_slug** | **str** |  | [optional] 
**certification** | **str** |  | [optional] 
**genres** | **List[str]** |  | [optional] 
**tags** | **List[str]** |  | [optional] 
**added** | **str** |  | [optional] 
**ratings** | [**List[SonarrSeriesRatingsInner]**](SonarrSeriesRatingsInner.md) |  | [optional] 
**quality_profile_id** | **float** |  | [optional] 
**id** | **float** |  | [optional] 
**root_folder_path** | **str** |  | [optional] 
**add_options** | [**List[SonarrSeriesAddOptionsInner]**](SonarrSeriesAddOptionsInner.md) |  | [optional] 

## Example

```python
from overseerr.models.sonarr_series import SonarrSeries

# TODO update the JSON string below
json = "{}"
# create an instance of SonarrSeries from a JSON string
sonarr_series_instance = SonarrSeries.from_json(json)
# print the JSON string representation of the object
print SonarrSeries.to_json()

# convert the object into a dict
sonarr_series_dict = sonarr_series_instance.to_dict()
# create an instance of SonarrSeries from a dict
sonarr_series_form_dict = sonarr_series.from_dict(sonarr_series_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


