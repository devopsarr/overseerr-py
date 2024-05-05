# Episode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** |  | [optional] 
**name** | **str** |  | [optional] 
**air_date** | **str** |  | [optional] 
**episode_number** | **float** |  | [optional] 
**overview** | **str** |  | [optional] 
**production_code** | **str** |  | [optional] 
**season_number** | **float** |  | [optional] 
**show_id** | **float** |  | [optional] 
**still_path** | **str** |  | [optional] 
**vote_average** | **float** |  | [optional] 
**vote_count** | **float** |  | [optional] 

## Example

```python
from overseerr.models.episode import Episode

# TODO update the JSON string below
json = "{}"
# create an instance of Episode from a JSON string
episode_instance = Episode.from_json(json)
# print the JSON string representation of the object
print(Episode.to_json())

# convert the object into a dict
episode_dict = episode_instance.to_dict()
# create an instance of Episode from a dict
episode_from_dict = Episode.from_dict(episode_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


