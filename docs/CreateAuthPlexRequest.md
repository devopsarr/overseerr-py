# CreateAuthPlexRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auth_token** | **str** |  | 

## Example

```python
from overseerr.models.create_auth_plex_request import CreateAuthPlexRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAuthPlexRequest from a JSON string
create_auth_plex_request_instance = CreateAuthPlexRequest.from_json(json)
# print the JSON string representation of the object
print CreateAuthPlexRequest.to_json()

# convert the object into a dict
create_auth_plex_request_dict = create_auth_plex_request_instance.to_dict()
# create an instance of CreateAuthPlexRequest from a dict
create_auth_plex_request_form_dict = create_auth_plex_request.from_dict(create_auth_plex_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


