# User


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
from overseerr.models.user import User

# TODO update the JSON string below
json = "{}"
# create an instance of User from a JSON string
user_instance = User.from_json(json)
# print the JSON string representation of the object
print User.to_json()

# convert the object into a dict
user_dict = user_instance.to_dict()
# create an instance of User from a dict
user_form_dict = user.from_dict(user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


