# WatchProviderRegion


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iso_3166_1** | **str** |  | [optional] 
**english_name** | **str** |  | [optional] 
**native_name** | **str** |  | [optional] 

## Example

```python
from overseerr.models.watch_provider_region import WatchProviderRegion

# TODO update the JSON string below
json = "{}"
# create an instance of WatchProviderRegion from a JSON string
watch_provider_region_instance = WatchProviderRegion.from_json(json)
# print the JSON string representation of the object
print WatchProviderRegion.to_json()

# convert the object into a dict
watch_provider_region_dict = watch_provider_region_instance.to_dict()
# create an instance of WatchProviderRegion from a dict
watch_provider_region_form_dict = watch_provider_region.from_dict(watch_provider_region_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


