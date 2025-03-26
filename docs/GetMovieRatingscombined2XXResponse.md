# GetMovieRatingscombined2XXResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rt** | [**GetMovieRatings2XXResponse**](GetMovieRatings2XXResponse.md) |  | [optional] 
**imdb** | [**GetMovieRatingscombined2XXResponseImdb**](GetMovieRatingscombined2XXResponseImdb.md) |  | [optional] 

## Example

```python
from overseerr.models.get_movie_ratingscombined2_xx_response import GetMovieRatingscombined2XXResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetMovieRatingscombined2XXResponse from a JSON string
get_movie_ratingscombined2_xx_response_instance = GetMovieRatingscombined2XXResponse.from_json(json)
# print the JSON string representation of the object
print(GetMovieRatingscombined2XXResponse.to_json())

# convert the object into a dict
get_movie_ratingscombined2_xx_response_dict = get_movie_ratingscombined2_xx_response_instance.to_dict()
# create an instance of GetMovieRatingscombined2XXResponse from a dict
get_movie_ratingscombined2_xx_response_from_dict = GetMovieRatingscombined2XXResponse.from_dict(get_movie_ratingscombined2_xx_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


