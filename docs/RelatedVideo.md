# RelatedVideo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**url** | **str** |  | [optional] 
**key** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**size** | **float** |  | [optional] 
**type** | **str** |  | [optional] 
**site** | **str** |  | [optional] 

## Example

```python
from overseerr.models.related_video import RelatedVideo

# TODO update the JSON string below
json = "{}"
# create an instance of RelatedVideo from a JSON string
related_video_instance = RelatedVideo.from_json(json)
# print the JSON string representation of the object
print(RelatedVideo.to_json())

# convert the object into a dict
related_video_dict = related_video_instance.to_dict()
# create an instance of RelatedVideo from a dict
related_video_from_dict = RelatedVideo.from_dict(related_video_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


