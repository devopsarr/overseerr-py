# CreateRequestRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**media_type** | **str** |  | 
**media_id** | **float** |  | 
**tvdb_id** | **float** |  | [optional] 
**seasons** | [**CreateRequestRequestSeasons**](CreateRequestRequestSeasons.md) |  | [optional] 
**is4k** | **bool** |  | [optional] 
**server_id** | **float** |  | [optional] 
**profile_id** | **float** |  | [optional] 
**root_folder** | **str** |  | [optional] 
**language_profile_id** | **float** |  | [optional] 
**user_id** | **float** |  | [optional] 

## Example

```python
from overseerr.models.create_request_request import CreateRequestRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateRequestRequest from a JSON string
create_request_request_instance = CreateRequestRequest.from_json(json)
# print the JSON string representation of the object
print(CreateRequestRequest.to_json())

# convert the object into a dict
create_request_request_dict = create_request_request_instance.to_dict()
# create an instance of CreateRequestRequest from a dict
create_request_request_from_dict = CreateRequestRequest.from_dict(create_request_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


