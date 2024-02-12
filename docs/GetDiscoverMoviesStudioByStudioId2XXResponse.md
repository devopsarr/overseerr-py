# GetDiscoverMoviesStudioByStudioId2XXResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **float** |  | [optional] 
**total_pages** | **float** |  | [optional] 
**total_results** | **float** |  | [optional] 
**studio** | [**ProductionCompany**](ProductionCompany.md) |  | [optional] 
**results** | [**List[MovieResult]**](MovieResult.md) |  | [optional] 

## Example

```python
from overseerr.models.get_discover_movies_studio_by_studio_id2_xx_response import GetDiscoverMoviesStudioByStudioId2XXResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetDiscoverMoviesStudioByStudioId2XXResponse from a JSON string
get_discover_movies_studio_by_studio_id2_xx_response_instance = GetDiscoverMoviesStudioByStudioId2XXResponse.from_json(json)
# print the JSON string representation of the object
print GetDiscoverMoviesStudioByStudioId2XXResponse.to_json()

# convert the object into a dict
get_discover_movies_studio_by_studio_id2_xx_response_dict = get_discover_movies_studio_by_studio_id2_xx_response_instance.to_dict()
# create an instance of GetDiscoverMoviesStudioByStudioId2XXResponse from a dict
get_discover_movies_studio_by_studio_id2_xx_response_form_dict = get_discover_movies_studio_by_studio_id2_xx_response.from_dict(get_discover_movies_studio_by_studio_id2_xx_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


