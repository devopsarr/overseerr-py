# ListPlexUsers200ResponseInner


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
from overseerr.models.list_plex_users200_response_inner import ListPlexUsers200ResponseInner

# TODO update the JSON string below
json = "{}"
# create an instance of ListPlexUsers200ResponseInner from a JSON string
list_plex_users200_response_inner_instance = ListPlexUsers200ResponseInner.from_json(json)
# print the JSON string representation of the object
print ListPlexUsers200ResponseInner.to_json()

# convert the object into a dict
list_plex_users200_response_inner_dict = list_plex_users200_response_inner_instance.to_dict()
# create an instance of ListPlexUsers200ResponseInner from a dict
list_plex_users200_response_inner_form_dict = list_plex_users200_response_inner.from_dict(list_plex_users200_response_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


