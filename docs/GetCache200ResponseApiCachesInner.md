# GetCache200ResponseApiCachesInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**stats** | [**GetCache200ResponseApiCachesInnerStats**](GetCache200ResponseApiCachesInnerStats.md) |  | [optional] 

## Example

```python
from overseerr.models.get_cache200_response_api_caches_inner import GetCache200ResponseApiCachesInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetCache200ResponseApiCachesInner from a JSON string
get_cache200_response_api_caches_inner_instance = GetCache200ResponseApiCachesInner.from_json(json)
# print the JSON string representation of the object
print GetCache200ResponseApiCachesInner.to_json()

# convert the object into a dict
get_cache200_response_api_caches_inner_dict = get_cache200_response_api_caches_inner_instance.to_dict()
# create an instance of GetCache200ResponseApiCachesInner from a dict
get_cache200_response_api_caches_inner_form_dict = get_cache200_response_api_caches_inner.from_dict(get_cache200_response_api_caches_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


