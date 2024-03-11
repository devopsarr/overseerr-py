# WatchProvidersInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iso_3166_1** | **str** |  | [optional] 
**link** | **str** |  | [optional] 
**buy** | [**List[WatchProviderDetails]**](WatchProviderDetails.md) |  | [optional] 
**flatrate** | [**List[WatchProviderDetails]**](WatchProviderDetails.md) |  | [optional] 

## Example

```python
from overseerr.models.watch_providers_inner import WatchProvidersInner

# TODO update the JSON string below
json = "{}"
# create an instance of WatchProvidersInner from a JSON string
watch_providers_inner_instance = WatchProvidersInner.from_json(json)
# print the JSON string representation of the object
print(WatchProvidersInner.to_json())

# convert the object into a dict
watch_providers_inner_dict = watch_providers_inner_instance.to_dict()
# create an instance of WatchProvidersInner from a dict
watch_providers_inner_form_dict = watch_providers_inner.from_dict(watch_providers_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


