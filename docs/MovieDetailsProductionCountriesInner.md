# MovieDetailsProductionCountriesInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iso_3166_1** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from overseerr.models.movie_details_production_countries_inner import MovieDetailsProductionCountriesInner

# TODO update the JSON string below
json = "{}"
# create an instance of MovieDetailsProductionCountriesInner from a JSON string
movie_details_production_countries_inner_instance = MovieDetailsProductionCountriesInner.from_json(json)
# print the JSON string representation of the object
print(MovieDetailsProductionCountriesInner.to_json())

# convert the object into a dict
movie_details_production_countries_inner_dict = movie_details_production_countries_inner_instance.to_dict()
# create an instance of MovieDetailsProductionCountriesInner from a dict
movie_details_production_countries_inner_form_dict = movie_details_production_countries_inner.from_dict(movie_details_production_countries_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


