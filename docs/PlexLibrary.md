# PlexLibrary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 
**enabled** | **bool** |  | 

## Example

```python
from overseerr.models.plex_library import PlexLibrary

# TODO update the JSON string below
json = "{}"
# create an instance of PlexLibrary from a JSON string
plex_library_instance = PlexLibrary.from_json(json)
# print the JSON string representation of the object
print PlexLibrary.to_json()

# convert the object into a dict
plex_library_dict = plex_library_instance.to_dict()
# create an instance of PlexLibrary from a dict
plex_library_form_dict = plex_library.from_dict(plex_library_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


