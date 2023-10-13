# CreateAuthLocalRequest


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email** | **str** |  | 
**password** | **str** |  | 

## Example

```python
from overseerr.models.create_auth_local_request import CreateAuthLocalRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAuthLocalRequest from a JSON string
create_auth_local_request_instance = CreateAuthLocalRequest.from_json(json)
# print the JSON string representation of the object
print CreateAuthLocalRequest.to_json()

# convert the object into a dict
create_auth_local_request_dict = create_auth_local_request_instance.to_dict()
# create an instance of CreateAuthLocalRequest from a dict
create_auth_local_request_form_dict = create_auth_local_request.from_dict(create_auth_local_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


