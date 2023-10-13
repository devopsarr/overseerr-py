# GetPlexSync200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**running** | **bool** |  | [optional] 
**progress** | **float** |  | [optional] 
**total** | **float** |  | [optional] 
**current_library** | [**PlexLibrary**](PlexLibrary.md) |  | [optional] 
**libraries** | [**List[PlexLibrary]**](PlexLibrary.md) |  | [optional] 

## Example

```python
from overseerr.models.get_plex_sync200_response import GetPlexSync200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetPlexSync200Response from a JSON string
get_plex_sync200_response_instance = GetPlexSync200Response.from_json(json)
# print the JSON string representation of the object
print GetPlexSync200Response.to_json()

# convert the object into a dict
get_plex_sync200_response_dict = get_plex_sync200_response_instance.to_dict()
# create an instance of GetPlexSync200Response from a dict
get_plex_sync200_response_form_dict = get_plex_sync200_response.from_dict(get_plex_sync200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


