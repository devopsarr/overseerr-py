# MovieDetailsCredits


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cast** | [**List[Cast]**](Cast.md) |  | [optional] 
**crew** | [**List[Crew]**](Crew.md) |  | [optional] 

## Example

```python
from overseerr.models.movie_details_credits import MovieDetailsCredits

# TODO update the JSON string below
json = "{}"
# create an instance of MovieDetailsCredits from a JSON string
movie_details_credits_instance = MovieDetailsCredits.from_json(json)
# print the JSON string representation of the object
print(MovieDetailsCredits.to_json())

# convert the object into a dict
movie_details_credits_dict = movie_details_credits_instance.to_dict()
# create an instance of MovieDetailsCredits from a dict
movie_details_credits_form_dict = movie_details_credits.from_dict(movie_details_credits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


