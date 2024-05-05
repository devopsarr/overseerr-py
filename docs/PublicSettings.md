# PublicSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**initialized** | **bool** |  | [optional] 

## Example

```python
from overseerr.models.public_settings import PublicSettings

# TODO update the JSON string below
json = "{}"
# create an instance of PublicSettings from a JSON string
public_settings_instance = PublicSettings.from_json(json)
# print the JSON string representation of the object
print(PublicSettings.to_json())

# convert the object into a dict
public_settings_dict = public_settings_instance.to_dict()
# create an instance of PublicSettings from a dict
public_settings_from_dict = PublicSettings.from_dict(public_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


