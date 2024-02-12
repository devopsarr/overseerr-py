# WatchProviderDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**display_priority** | **float** |  | [optional] 
**logo_path** | **str** |  | [optional] 
**id** | **float** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from overseerr.models.watch_provider_details import WatchProviderDetails

# TODO update the JSON string below
json = "{}"
# create an instance of WatchProviderDetails from a JSON string
watch_provider_details_instance = WatchProviderDetails.from_json(json)
# print the JSON string representation of the object
print WatchProviderDetails.to_json()

# convert the object into a dict
watch_provider_details_dict = watch_provider_details_instance.to_dict()
# create an instance of WatchProviderDetails from a dict
watch_provider_details_form_dict = watch_provider_details.from_dict(watch_provider_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


