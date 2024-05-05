# GetPlexSync2XXResponse


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
from overseerr.models.get_plex_sync2_xx_response import GetPlexSync2XXResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetPlexSync2XXResponse from a JSON string
get_plex_sync2_xx_response_instance = GetPlexSync2XXResponse.from_json(json)
# print the JSON string representation of the object
print(GetPlexSync2XXResponse.to_json())

# convert the object into a dict
get_plex_sync2_xx_response_dict = get_plex_sync2_xx_response_instance.to_dict()
# create an instance of GetPlexSync2XXResponse from a dict
get_plex_sync2_xx_response_from_dict = GetPlexSync2XXResponse.from_dict(get_plex_sync2_xx_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


