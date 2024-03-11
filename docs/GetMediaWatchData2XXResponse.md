# GetMediaWatchData2XXResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**GetMediaWatchData2XXResponseData**](GetMediaWatchData2XXResponseData.md) |  | [optional] 
**data4k** | [**GetMediaWatchData2XXResponseData**](GetMediaWatchData2XXResponseData.md) |  | [optional] 

## Example

```python
from overseerr.models.get_media_watch_data2_xx_response import GetMediaWatchData2XXResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetMediaWatchData2XXResponse from a JSON string
get_media_watch_data2_xx_response_instance = GetMediaWatchData2XXResponse.from_json(json)
# print the JSON string representation of the object
print(GetMediaWatchData2XXResponse.to_json())

# convert the object into a dict
get_media_watch_data2_xx_response_dict = get_media_watch_data2_xx_response_instance.to_dict()
# create an instance of GetMediaWatchData2XXResponse from a dict
get_media_watch_data2_xx_response_form_dict = get_media_watch_data2_xx_response.from_dict(get_media_watch_data2_xx_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


