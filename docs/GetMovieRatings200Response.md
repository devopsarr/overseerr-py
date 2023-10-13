# GetMovieRatings200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**year** | **float** |  | [optional] 
**url** | **str** |  | [optional] 
**critics_score** | **float** |  | [optional] 
**critics_rating** | **str** |  | [optional] 
**audience_score** | **float** |  | [optional] 
**audience_rating** | **str** |  | [optional] 

## Example

```python
from overseerr.models.get_movie_ratings200_response import GetMovieRatings200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetMovieRatings200Response from a JSON string
get_movie_ratings200_response_instance = GetMovieRatings200Response.from_json(json)
# print the JSON string representation of the object
print GetMovieRatings200Response.to_json()

# convert the object into a dict
get_movie_ratings200_response_dict = get_movie_ratings200_response_instance.to_dict()
# create an instance of GetMovieRatings200Response from a dict
get_movie_ratings200_response_form_dict = get_movie_ratings200_response.from_dict(get_movie_ratings200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


