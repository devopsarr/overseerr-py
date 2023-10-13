# GetCache200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image_cache** | [**GetCache200ResponseImageCache**](GetCache200ResponseImageCache.md) |  | [optional] 
**api_caches** | [**List[GetCache200ResponseApiCachesInner]**](GetCache200ResponseApiCachesInner.md) |  | [optional] 

## Example

```python
from overseerr.models.get_cache200_response import GetCache200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetCache200Response from a JSON string
get_cache200_response_instance = GetCache200Response.from_json(json)
# print the JSON string representation of the object
print GetCache200Response.to_json()

# convert the object into a dict
get_cache200_response_dict = get_cache200_response_instance.to_dict()
# create an instance of GetCache200Response from a dict
get_cache200_response_form_dict = get_cache200_response.from_dict(get_cache200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


