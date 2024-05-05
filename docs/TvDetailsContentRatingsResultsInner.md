# TvDetailsContentRatingsResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iso_3166_1** | **str** |  | [optional] 
**rating** | **str** |  | [optional] 

## Example

```python
from overseerr.models.tv_details_content_ratings_results_inner import TvDetailsContentRatingsResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of TvDetailsContentRatingsResultsInner from a JSON string
tv_details_content_ratings_results_inner_instance = TvDetailsContentRatingsResultsInner.from_json(json)
# print the JSON string representation of the object
print(TvDetailsContentRatingsResultsInner.to_json())

# convert the object into a dict
tv_details_content_ratings_results_inner_dict = tv_details_content_ratings_results_inner_instance.to_dict()
# create an instance of TvDetailsContentRatingsResultsInner from a dict
tv_details_content_ratings_results_inner_from_dict = TvDetailsContentRatingsResultsInner.from_dict(tv_details_content_ratings_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


