# GetCache2XXResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image_cache** | [**GetCache2XXResponseImageCache**](GetCache2XXResponseImageCache.md) |  | [optional] 
**api_caches** | [**List[GetCache2XXResponseApiCachesInner]**](GetCache2XXResponseApiCachesInner.md) |  | [optional] 

## Example

```python
from overseerr.models.get_cache2_xx_response import GetCache2XXResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetCache2XXResponse from a JSON string
get_cache2_xx_response_instance = GetCache2XXResponse.from_json(json)
# print the JSON string representation of the object
print(GetCache2XXResponse.to_json())

# convert the object into a dict
get_cache2_xx_response_dict = get_cache2_xx_response_instance.to_dict()
# create an instance of GetCache2XXResponse from a dict
get_cache2_xx_response_form_dict = get_cache2_xx_response.from_dict(get_cache2_xx_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


