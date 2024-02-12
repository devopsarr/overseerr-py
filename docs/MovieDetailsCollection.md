# MovieDetailsCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** |  | [optional] 
**name** | **str** |  | [optional] 
**poster_path** | **str** |  | [optional] 
**backdrop_path** | **str** |  | [optional] 

## Example

```python
from overseerr.models.movie_details_collection import MovieDetailsCollection

# TODO update the JSON string below
json = "{}"
# create an instance of MovieDetailsCollection from a JSON string
movie_details_collection_instance = MovieDetailsCollection.from_json(json)
# print the JSON string representation of the object
print MovieDetailsCollection.to_json()

# convert the object into a dict
movie_details_collection_dict = movie_details_collection_instance.to_dict()
# create an instance of MovieDetailsCollection from a dict
movie_details_collection_form_dict = movie_details_collection.from_dict(movie_details_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


