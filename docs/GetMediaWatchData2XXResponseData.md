# GetMediaWatchData2XXResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**play_count7_days** | **float** |  | [optional] 
**play_count30_days** | **float** |  | [optional] 
**play_count** | **float** |  | [optional] 
**users** | [**List[User]**](User.md) |  | [optional] 

## Example

```python
from overseerr.models.get_media_watch_data2_xx_response_data import GetMediaWatchData2XXResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GetMediaWatchData2XXResponseData from a JSON string
get_media_watch_data2_xx_response_data_instance = GetMediaWatchData2XXResponseData.from_json(json)
# print the JSON string representation of the object
print(GetMediaWatchData2XXResponseData.to_json())

# convert the object into a dict
get_media_watch_data2_xx_response_data_dict = get_media_watch_data2_xx_response_data_instance.to_dict()
# create an instance of GetMediaWatchData2XXResponseData from a dict
get_media_watch_data2_xx_response_data_from_dict = GetMediaWatchData2XXResponseData.from_dict(get_media_watch_data2_xx_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


