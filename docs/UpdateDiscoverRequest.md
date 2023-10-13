# UpdateDiscoverRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**type** | **float** |  | [optional] 
**data** | **str** |  | [optional] 

## Example

```python
from overseerr.models.update_discover_request import UpdateDiscoverRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDiscoverRequest from a JSON string
update_discover_request_instance = UpdateDiscoverRequest.from_json(json)
# print the JSON string representation of the object
print UpdateDiscoverRequest.to_json()

# convert the object into a dict
update_discover_request_dict = update_discover_request_instance.to_dict()
# create an instance of UpdateDiscoverRequest from a dict
update_discover_request_form_dict = update_discover_request.from_dict(update_discover_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


