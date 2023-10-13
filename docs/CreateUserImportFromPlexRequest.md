# CreateUserImportFromPlexRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plex_ids** | **List[str]** |  | [optional] 

## Example

```python
from overseerr.models.create_user_import_from_plex_request import CreateUserImportFromPlexRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUserImportFromPlexRequest from a JSON string
create_user_import_from_plex_request_instance = CreateUserImportFromPlexRequest.from_json(json)
# print the JSON string representation of the object
print CreateUserImportFromPlexRequest.to_json()

# convert the object into a dict
create_user_import_from_plex_request_dict = create_user_import_from_plex_request_instance.to_dict()
# create an instance of CreateUserImportFromPlexRequest from a dict
create_user_import_from_plex_request_form_dict = create_user_import_from_plex_request.from_dict(create_user_import_from_plex_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


