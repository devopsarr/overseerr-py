# ListPlexUsers2XXResponseInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**title** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**thumb** | **str** |  | [optional] 

## Example

```python
from overseerr.models.list_plex_users2_xx_response_inner import ListPlexUsers2XXResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListPlexUsers2XXResponseInner from a JSON string
list_plex_users2_xx_response_inner_instance = ListPlexUsers2XXResponseInner.from_json(json)
# print the JSON string representation of the object
print(ListPlexUsers2XXResponseInner.to_json())

# convert the object into a dict
list_plex_users2_xx_response_inner_dict = list_plex_users2_xx_response_inner_instance.to_dict()
# create an instance of ListPlexUsers2XXResponseInner from a dict
list_plex_users2_xx_response_inner_from_dict = ListPlexUsers2XXResponseInner.from_dict(list_plex_users2_xx_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


