# PlexConnection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**protocol** | **str** |  | 
**address** | **str** |  | 
**port** | **float** |  | 
**uri** | **str** |  | 
**local** | **bool** |  | 
**status** | **float** |  | [optional] 
**message** | **str** |  | [optional] 

## Example

```python
from overseerr.models.plex_connection import PlexConnection

# TODO update the JSON string below
json = "{}"
# create an instance of PlexConnection from a JSON string
plex_connection_instance = PlexConnection.from_json(json)
# print the JSON string representation of the object
print PlexConnection.to_json()

# convert the object into a dict
plex_connection_dict = plex_connection_instance.to_dict()
# create an instance of PlexConnection from a dict
plex_connection_form_dict = plex_connection.from_dict(plex_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


