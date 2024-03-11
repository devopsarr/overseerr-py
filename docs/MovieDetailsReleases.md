# MovieDetailsReleases


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[MovieDetailsReleasesResultsInner]**](MovieDetailsReleasesResultsInner.md) |  | [optional] 

## Example

```python
from overseerr.models.movie_details_releases import MovieDetailsReleases

# TODO update the JSON string below
json = "{}"
# create an instance of MovieDetailsReleases from a JSON string
movie_details_releases_instance = MovieDetailsReleases.from_json(json)
# print the JSON string representation of the object
print(MovieDetailsReleases.to_json())

# convert the object into a dict
movie_details_releases_dict = movie_details_releases_instance.to_dict()
# create an instance of MovieDetailsReleases from a dict
movie_details_releases_form_dict = movie_details_releases.from_dict(movie_details_releases_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


