# UpdateRequestRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**media_type** | **str** |  | 
**seasons** | **List[float]** |  | [optional] 
**is4k** | **bool** |  | [optional] 
**server_id** | **float** |  | [optional] 
**profile_id** | **float** |  | [optional] 
**root_folder** | **str** |  | [optional] 
**language_profile_id** | **float** |  | [optional] 
**user_id** | **float** |  | [optional] 

## Example

```python
from overseerr.models.update_request_request import UpdateRequestRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateRequestRequest from a JSON string
update_request_request_instance = UpdateRequestRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateRequestRequest.to_json())

# convert the object into a dict
update_request_request_dict = update_request_request_instance.to_dict()
# create an instance of UpdateRequestRequest from a dict
update_request_request_form_dict = update_request_request.from_dict(update_request_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


