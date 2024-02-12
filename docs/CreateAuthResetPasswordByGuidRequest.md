# CreateAuthResetPasswordByGuidRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** |  | 

## Example

```python
from overseerr.models.create_auth_reset_password_by_guid_request import CreateAuthResetPasswordByGuidRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateAuthResetPasswordByGuidRequest from a JSON string
create_auth_reset_password_by_guid_request_instance = CreateAuthResetPasswordByGuidRequest.from_json(json)
# print the JSON string representation of the object
print CreateAuthResetPasswordByGuidRequest.to_json()

# convert the object into a dict
create_auth_reset_password_by_guid_request_dict = create_auth_reset_password_by_guid_request_instance.to_dict()
# create an instance of CreateAuthResetPasswordByGuidRequest from a dict
create_auth_reset_password_by_guid_request_form_dict = create_auth_reset_password_by_guid_request.from_dict(create_auth_reset_password_by_guid_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


