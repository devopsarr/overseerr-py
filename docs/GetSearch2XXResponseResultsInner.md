# GetSearch2XXResponseResultsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** |  | 
**media_type** | **str** |  | [default to 'person']
**popularity** | **float** |  | [optional] 
**poster_path** | **str** |  | [optional] 
**backdrop_path** | **str** |  | [optional] 
**vote_count** | **float** |  | [optional] 
**vote_average** | **float** |  | [optional] 
**genre_ids** | **List[float]** |  | [optional] 
**overview** | **str** |  | [optional] 
**original_language** | **str** |  | [optional] 
**title** | **str** |  | 
**original_title** | **str** |  | [optional] 
**release_date** | **str** |  | [optional] 
**adult** | **bool** |  | [optional] 
**video** | **bool** |  | [optional] 
**media_info** | [**MediaInfo**](MediaInfo.md) |  | [optional] 
**name** | **str** |  | [optional] 
**original_name** | **str** |  | [optional] 
**origin_country** | **List[str]** |  | [optional] 
**first_air_date** | **str** |  | [optional] 
**profile_path** | **str** |  | [optional] 
**known_for** | [**List[PersonResultKnownForInner]**](PersonResultKnownForInner.md) |  | [optional] 

## Example

```python
from overseerr.models.get_search2_xx_response_results_inner import GetSearch2XXResponseResultsInner

# TODO update the JSON string below
json = "{}"
# create an instance of GetSearch2XXResponseResultsInner from a JSON string
get_search2_xx_response_results_inner_instance = GetSearch2XXResponseResultsInner.from_json(json)
# print the JSON string representation of the object
print(GetSearch2XXResponseResultsInner.to_json())

# convert the object into a dict
get_search2_xx_response_results_inner_dict = get_search2_xx_response_results_inner_instance.to_dict()
# create an instance of GetSearch2XXResponseResultsInner from a dict
get_search2_xx_response_results_inner_form_dict = get_search2_xx_response_results_inner.from_dict(get_search2_xx_response_results_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


