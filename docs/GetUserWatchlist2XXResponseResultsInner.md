# GetUserWatchlist2XXResponseResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tmdb_id** | **float** |  | [optional] 
**rating_key** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**title** | **str** |  | [optional] 

## Example

```python
from overseerr.models.get_user_watchlist2_xx_response_results_inner import GetUserWatchlist2XXResponseResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserWatchlist2XXResponseResultsInner from a JSON string
get_user_watchlist2_xx_response_results_inner_instance = GetUserWatchlist2XXResponseResultsInner.from_json(json)
# print the JSON string representation of the object
print(GetUserWatchlist2XXResponseResultsInner.to_json())

# convert the object into a dict
get_user_watchlist2_xx_response_results_inner_dict = get_user_watchlist2_xx_response_results_inner_instance.to_dict()
# create an instance of GetUserWatchlist2XXResponseResultsInner from a dict
get_user_watchlist2_xx_response_results_inner_from_dict = GetUserWatchlist2XXResponseResultsInner.from_dict(get_user_watchlist2_xx_response_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


