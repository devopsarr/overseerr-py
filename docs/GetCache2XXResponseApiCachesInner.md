# GetCache2XXResponseApiCachesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**stats** | [**GetCache2XXResponseApiCachesInnerStats**](GetCache2XXResponseApiCachesInnerStats.md) |  | [optional] 

## Example

```python
from overseerr.models.get_cache2_xx_response_api_caches_inner import GetCache2XXResponseApiCachesInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetCache2XXResponseApiCachesInner from a JSON string
get_cache2_xx_response_api_caches_inner_instance = GetCache2XXResponseApiCachesInner.from_json(json)
# print the JSON string representation of the object
print(GetCache2XXResponseApiCachesInner.to_json())

# convert the object into a dict
get_cache2_xx_response_api_caches_inner_dict = get_cache2_xx_response_api_caches_inner_instance.to_dict()
# create an instance of GetCache2XXResponseApiCachesInner from a dict
get_cache2_xx_response_api_caches_inner_form_dict = get_cache2_xx_response_api_caches_inner.from_dict(get_cache2_xx_response_api_caches_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


