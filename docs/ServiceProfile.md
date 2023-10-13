# ServiceProfile


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **float** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from overseerr.models.service_profile import ServiceProfile

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceProfile from a JSON string
service_profile_instance = ServiceProfile.from_json(json)
# print the JSON string representation of the object
print ServiceProfile.to_json()

# convert the object into a dict
service_profile_dict = service_profile_instance.to_dict()
# create an instance of ServiceProfile from a dict
service_profile_form_dict = service_profile.from_dict(service_profile_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


