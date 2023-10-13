# GetUserWatchlist200ResponseResultsInner


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tmdb_id** | **float** |  | [optional] 
**rating_key** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from overseerr.models.get_user_watchlist200_response_results_inner import GetUserWatchlist200ResponseResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserWatchlist200ResponseResultsInner from a JSON string
get_user_watchlist200_response_results_inner_instance = GetUserWatchlist200ResponseResultsInner.from_json(json)
# print the JSON string representation of the object
print GetUserWatchlist200ResponseResultsInner.to_json()

# convert the object into a dict
get_user_watchlist200_response_results_inner_dict = get_user_watchlist200_response_results_inner_instance.to_dict()
# create an instance of GetUserWatchlist200ResponseResultsInner from a dict
get_user_watchlist200_response_results_inner_form_dict = get_user_watchlist200_response_results_inner.from_dict(get_user_watchlist200_response_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


