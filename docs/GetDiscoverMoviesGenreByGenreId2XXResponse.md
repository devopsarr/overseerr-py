# GetDiscoverMoviesGenreByGenreId2XXResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**page** | **float** |  | [optional] 
**total_pages** | **float** |  | [optional] 
**total_results** | **float** |  | [optional] 
**genre** | [**Genre**](Genre.md) |  | [optional] 
**results** | [**List[MovieResult]**](MovieResult.md) |  | [optional] 

## Example

```python
from overseerr.models.get_discover_movies_genre_by_genre_id2_xx_response import GetDiscoverMoviesGenreByGenreId2XXResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetDiscoverMoviesGenreByGenreId2XXResponse from a JSON string
get_discover_movies_genre_by_genre_id2_xx_response_instance = GetDiscoverMoviesGenreByGenreId2XXResponse.from_json(json)
# print the JSON string representation of the object
print(GetDiscoverMoviesGenreByGenreId2XXResponse.to_json())

# convert the object into a dict
get_discover_movies_genre_by_genre_id2_xx_response_dict = get_discover_movies_genre_by_genre_id2_xx_response_instance.to_dict()
# create an instance of GetDiscoverMoviesGenreByGenreId2XXResponse from a dict
get_discover_movies_genre_by_genre_id2_xx_response_from_dict = GetDiscoverMoviesGenreByGenreId2XXResponse.from_dict(get_discover_movies_genre_by_genre_id2_xx_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


