# GetCache200ResponseApiCachesInnerStats


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
from overseerr.models.get_cache200_response_api_caches_inner_stats import GetCache200ResponseApiCachesInnerStats

# TODO update the JSON string below
json = "{}"
# create an instance of GetCache200ResponseApiCachesInnerStats from a JSON string
get_cache200_response_api_caches_inner_stats_instance = GetCache200ResponseApiCachesInnerStats.from_json(json)
# print the JSON string representation of the object
print GetCache200ResponseApiCachesInnerStats.to_json()

# convert the object into a dict
get_cache200_response_api_caches_inner_stats_dict = get_cache200_response_api_caches_inner_stats_instance.to_dict()
# create an instance of GetCache200ResponseApiCachesInnerStats from a dict
get_cache200_response_api_caches_inner_stats_form_dict = get_cache200_response_api_caches_inner_stats.from_dict(get_cache200_response_api_caches_inner_stats_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


