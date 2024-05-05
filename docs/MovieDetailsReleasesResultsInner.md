# MovieDetailsReleasesResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iso_3166_1** | **str** |  | [optional] 
**rating** | **str** |  | [optional] 
**release_dates** | [**List[MovieDetailsReleasesResultsInnerReleaseDatesInner]**](MovieDetailsReleasesResultsInnerReleaseDatesInner.md) |  | [optional] 

## Example

```python
from overseerr.models.movie_details_releases_results_inner import MovieDetailsReleasesResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of MovieDetailsReleasesResultsInner from a JSON string
movie_details_releases_results_inner_instance = MovieDetailsReleasesResultsInner.from_json(json)
# print the JSON string representation of the object
print(MovieDetailsReleasesResultsInner.to_json())

# convert the object into a dict
movie_details_releases_results_inner_dict = movie_details_releases_results_inner_instance.to_dict()
# create an instance of MovieDetailsReleasesResultsInner from a dict
movie_details_releases_results_inner_from_dict = MovieDetailsReleasesResultsInner.from_dict(movie_details_releases_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


