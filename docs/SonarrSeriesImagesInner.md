# SonarrSeriesImagesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cover_type** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from overseerr.models.sonarr_series_images_inner import SonarrSeriesImagesInner

# TODO update the JSON string below
json = "{}"
# create an instance of SonarrSeriesImagesInner from a JSON string
sonarr_series_images_inner_instance = SonarrSeriesImagesInner.from_json(json)
# print the JSON string representation of the object
print(SonarrSeriesImagesInner.to_json())

# convert the object into a dict
sonarr_series_images_inner_dict = sonarr_series_images_inner_instance.to_dict()
# create an instance of SonarrSeriesImagesInner from a dict
sonarr_series_images_inner_from_dict = SonarrSeriesImagesInner.from_dict(sonarr_series_images_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


