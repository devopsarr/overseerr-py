# GetCache2XXResponseApiCachesInnerStats


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hits** | **float** |  | [optional] 
**misses** | **float** |  | [optional] 
**keys** | **float** |  | [optional] 
**ksize** | **float** |  | [optional] 
**vsize** | **float** |  | [optional] 

## Example

```python
from overseerr.models.get_cache2_xx_response_api_caches_inner_stats import GetCache2XXResponseApiCachesInnerStats

# TODO update the JSON string below
json = "{}"
# create an instance of GetCache2XXResponseApiCachesInnerStats from a JSON string
get_cache2_xx_response_api_caches_inner_stats_instance = GetCache2XXResponseApiCachesInnerStats.from_json(json)
# print the JSON string representation of the object
print(GetCache2XXResponseApiCachesInnerStats.to_json())

# convert the object into a dict
get_cache2_xx_response_api_caches_inner_stats_dict = get_cache2_xx_response_api_caches_inner_stats_instance.to_dict()
# create an instance of GetCache2XXResponseApiCachesInnerStats from a dict
get_cache2_xx_response_api_caches_inner_stats_form_dict = get_cache2_xx_response_api_caches_inner_stats.from_dict(get_cache2_xx_response_api_caches_inner_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


