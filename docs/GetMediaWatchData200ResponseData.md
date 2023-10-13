# GetMediaWatchData200ResponseData


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**play_count7_days** | **float** |  | [optional] 
**play_count30_days** | **float** |  | [optional] 
**play_count** | **float** |  | [optional] 
**users** | [**List[User]**](User.md) |  | [optional] 

## Example

```python
from overseerr.models.get_media_watch_data200_response_data import GetMediaWatchData200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GetMediaWatchData200ResponseData from a JSON string
get_media_watch_data200_response_data_instance = GetMediaWatchData200ResponseData.from_json(json)
# print the JSON string representation of the object
print GetMediaWatchData200ResponseData.to_json()

# convert the object into a dict
get_media_watch_data200_response_data_dict = get_media_watch_data200_response_data_instance.to_dict()
# create an instance of GetMediaWatchData200ResponseData from a dict
get_media_watch_data200_response_data_form_dict = get_media_watch_data200_response_data.from_dict(get_media_watch_data200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


