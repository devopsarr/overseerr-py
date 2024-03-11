# TvDetailsContentRatings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**results** | [**List[TvDetailsContentRatingsResultsInner]**](TvDetailsContentRatingsResultsInner.md) |  | [optional] 

## Example

```python
from overseerr.models.tv_details_content_ratings import TvDetailsContentRatings

# TODO update the JSON string below
json = "{}"
# create an instance of TvDetailsContentRatings from a JSON string
tv_details_content_ratings_instance = TvDetailsContentRatings.from_json(json)
# print the JSON string representation of the object
print(TvDetailsContentRatings.to_json())

# convert the object into a dict
tv_details_content_ratings_dict = tv_details_content_ratings_instance.to_dict()
# create an instance of TvDetailsContentRatings from a dict
tv_details_content_ratings_form_dict = tv_details_content_ratings.from_dict(tv_details_content_ratings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


