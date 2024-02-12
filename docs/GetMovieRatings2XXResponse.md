# GetMovieRatings2XXResponse


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
from overseerr.models.get_movie_ratings2_xx_response import GetMovieRatings2XXResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetMovieRatings2XXResponse from a JSON string
get_movie_ratings2_xx_response_instance = GetMovieRatings2XXResponse.from_json(json)
# print the JSON string representation of the object
print GetMovieRatings2XXResponse.to_json()

# convert the object into a dict
get_movie_ratings2_xx_response_dict = get_movie_ratings2_xx_response_instance.to_dict()
# create an instance of GetMovieRatings2XXResponse from a dict
get_movie_ratings2_xx_response_form_dict = get_movie_ratings2_xx_response.from_dict(get_movie_ratings2_xx_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


