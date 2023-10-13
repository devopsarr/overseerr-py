# MediaRequestModifiedBy


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [readonly] 
**email** | **str** |  | [readonly] 
**username** | **str** |  | [optional] 
**plex_token** | **str** |  | [optional] [readonly] 
**plex_username** | **str** |  | [optional] [readonly] 
**user_type** | **int** |  | [optional] [readonly] 
**permissions** | **float** |  | [optional] 
**avatar** | **str** |  | [optional] [readonly] 
**created_at** | **str** |  | [readonly] 
**updated_at** | **str** |  | [readonly] 
**request_count** | **float** |  | [optional] [readonly] 

## Example

```python
from overseerr.models.media_request_modified_by import MediaRequestModifiedBy

# TODO update the JSON string below
json = "{}"
# create an instance of MediaRequestModifiedBy from a JSON string
media_request_modified_by_instance = MediaRequestModifiedBy.from_json(json)
# print the JSON string representation of the object
print MediaRequestModifiedBy.to_json()

# convert the object into a dict
media_request_modified_by_dict = media_request_modified_by_instance.to_dict()
# create an instance of MediaRequestModifiedBy from a dict
media_request_modified_by_form_dict = media_request_modified_by.from_dict(media_request_modified_by_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


