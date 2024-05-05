# CreateDiscoverAddRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**type** | **float** |  | [optional] 
**data** | **str** |  | [optional] 

## Example

```python
from overseerr.models.create_discover_add_request import CreateDiscoverAddRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDiscoverAddRequest from a JSON string
create_discover_add_request_instance = CreateDiscoverAddRequest.from_json(json)
# print the JSON string representation of the object
print(CreateDiscoverAddRequest.to_json())

# convert the object into a dict
create_discover_add_request_dict = create_discover_add_request_instance.to_dict()
# create an instance of CreateDiscoverAddRequest from a dict
create_discover_add_request_from_dict = CreateDiscoverAddRequest.from_dict(create_discover_add_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


