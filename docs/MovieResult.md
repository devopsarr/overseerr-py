# MovieResult


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** |  | 
**media_type** | **str** |  | 
**popularity** | **float** |  | [optional] 
**poster_path** | **str** |  | [optional] 
**backdrop_path** | **str** |  | [optional] 
**vote_count** | **float** |  | [optional] 
**vote_average** | **float** |  | [optional] 
**genre_ids** | **List[float]** |  | [optional] 
**overview** | **str** |  | [optional] 
**original_language** | **str** |  | [optional] 
**title** | **str** |  | 
**original_title** | **str** |  | [optional] 
**release_date** | **str** |  | [optional] 
**adult** | **bool** |  | [optional] 
**video** | **bool** |  | [optional] 
**media_info** | [**MediaInfo**](MediaInfo.md) |  | [optional] 

## Example

```python
from overseerr.models.movie_result import MovieResult

# TODO update the JSON string below
json = "{}"
# create an instance of MovieResult from a JSON string
movie_result_instance = MovieResult.from_json(json)
# print the JSON string representation of the object
print(MovieResult.to_json())

# convert the object into a dict
movie_result_dict = movie_result_instance.to_dict()
# create an instance of MovieResult from a dict
movie_result_from_dict = MovieResult.from_dict(movie_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


