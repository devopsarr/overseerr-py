# GetDiscoverTv2XXResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **float** |  | [optional] 
**total_pages** | **float** |  | [optional] 
**total_results** | **float** |  | [optional] 
**results** | [**List[TvResult]**](TvResult.md) |  | [optional] 

## Example

```python
from overseerr.models.get_discover_tv2_xx_response import GetDiscoverTv2XXResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetDiscoverTv2XXResponse from a JSON string
get_discover_tv2_xx_response_instance = GetDiscoverTv2XXResponse.from_json(json)
# print the JSON string representation of the object
print(GetDiscoverTv2XXResponse.to_json())

# convert the object into a dict
get_discover_tv2_xx_response_dict = get_discover_tv2_xx_response_instance.to_dict()
# create an instance of GetDiscoverTv2XXResponse from a dict
get_discover_tv2_xx_response_from_dict = GetDiscoverTv2XXResponse.from_dict(get_discover_tv2_xx_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


