# PersonResultKnownForInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** |  | 
**media_type** | **str** |  | 
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

## Example

```python
from overseerr.models.person_result_known_for_inner import PersonResultKnownForInner

# TODO update the JSON string below
json = "{}"
# create an instance of PersonResultKnownForInner from a JSON string
person_result_known_for_inner_instance = PersonResultKnownForInner.from_json(json)
# print the JSON string representation of the object
print PersonResultKnownForInner.to_json()

# convert the object into a dict
person_result_known_for_inner_dict = person_result_known_for_inner_instance.to_dict()
# create an instance of PersonResultKnownForInner from a dict
person_result_known_for_inner_form_dict = person_result_known_for_inner.from_dict(person_result_known_for_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


