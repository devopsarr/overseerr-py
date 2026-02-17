# MediaInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** |  | [optional] [readonly] 
**tmdb_id** | **float** |  | [optional] [readonly] 
**tvdb_id** | **float** |  | [optional] [readonly] 
**status** | **float** | Availability of the media. 1 &#x3D; &#x60;UNKNOWN&#x60;, 2 &#x3D; &#x60;PENDING&#x60;, 3 &#x3D; &#x60;PROCESSING&#x60;, 4 &#x3D; &#x60;PARTIALLY_AVAILABLE&#x60;, 5 &#x3D; &#x60;AVAILABLE&#x60;, 6 &#x3D; &#x60;DELETED&#x60; | [optional] 
**requests** | [**List[MediaRequest]**](MediaRequest.md) |  | [optional] [readonly] 
**created_at** | **str** |  | [optional] [readonly] 
**updated_at** | **str** |  | [optional] [readonly] 

## Example

```python
from overseerr.models.media_info import MediaInfo

# TODO update the JSON string below
json = "{}"
# create an instance of MediaInfo from a JSON string
media_info_instance = MediaInfo.from_json(json)
# print the JSON string representation of the object
print(MediaInfo.to_json())

# convert the object into a dict
media_info_dict = media_info_instance.to_dict()
# create an instance of MediaInfo from a dict
media_info_from_dict = MediaInfo.from_dict(media_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


