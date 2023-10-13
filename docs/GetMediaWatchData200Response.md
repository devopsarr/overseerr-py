# GetMediaWatchData200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**GetMediaWatchData200ResponseData**](GetMediaWatchData200ResponseData.md) |  | [optional] 
**data4k** | [**GetMediaWatchData200ResponseData**](GetMediaWatchData200ResponseData.md) |  | [optional] 

## Example

```python
from overseerr.models.get_media_watch_data200_response import GetMediaWatchData200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetMediaWatchData200Response from a JSON string
get_media_watch_data200_response_instance = GetMediaWatchData200Response.from_json(json)
# print the JSON string representation of the object
print GetMediaWatchData200Response.to_json()

# convert the object into a dict
get_media_watch_data200_response_dict = get_media_watch_data200_response_instance.to_dict()
# create an instance of GetMediaWatchData200Response from a dict
get_media_watch_data200_response_form_dict = get_media_watch_data200_response.from_dict(get_media_watch_data200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


