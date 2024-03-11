# PutUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ids** | **List[int]** |  | [optional] 
**permissions** | **int** |  | [optional] 

## Example

```python
from overseerr.models.put_user_request import PutUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PutUserRequest from a JSON string
put_user_request_instance = PutUserRequest.from_json(json)
# print the JSON string representation of the object
print(PutUserRequest.to_json())

# convert the object into a dict
put_user_request_dict = put_user_request_instance.to_dict()
# create an instance of PutUserRequest from a dict
put_user_request_form_dict = put_user_request.from_dict(put_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


