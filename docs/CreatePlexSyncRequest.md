# CreatePlexSyncRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cancel** | **bool** |  | [optional] 
**start** | **bool** |  | [optional] 

## Example

```python
from overseerr.models.create_plex_sync_request import CreatePlexSyncRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePlexSyncRequest from a JSON string
create_plex_sync_request_instance = CreatePlexSyncRequest.from_json(json)
# print the JSON string representation of the object
print(CreatePlexSyncRequest.to_json())

# convert the object into a dict
create_plex_sync_request_dict = create_plex_sync_request_instance.to_dict()
# create an instance of CreatePlexSyncRequest from a dict
create_plex_sync_request_from_dict = CreatePlexSyncRequest.from_dict(create_plex_sync_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


