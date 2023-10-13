# GetMovieRatingscombined200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rt** | [**GetMovieRatings200Response**](GetMovieRatings200Response.md) |  | [optional] 
**imdb** | [**GetMovieRatingscombined200ResponseImdb**](GetMovieRatingscombined200ResponseImdb.md) |  | [optional] 

## Example

```python
from overseerr.models.get_movie_ratingscombined200_response import GetMovieRatingscombined200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetMovieRatingscombined200Response from a JSON string
get_movie_ratingscombined200_response_instance = GetMovieRatingscombined200Response.from_json(json)
# print the JSON string representation of the object
print GetMovieRatingscombined200Response.to_json()

# convert the object into a dict
get_movie_ratingscombined200_response_dict = get_movie_ratingscombined200_response_instance.to_dict()
# create an instance of GetMovieRatingscombined200Response from a dict
get_movie_ratingscombined200_response_form_dict = get_movie_ratingscombined200_response.from_dict(get_movie_ratingscombined200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


