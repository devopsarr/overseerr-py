# GetStatusAppdata2XXResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_data** | **bool** |  | [optional] 
**app_data_path** | **str** |  | [optional] 

## Example

```python
from overseerr.models.get_status_appdata2_xx_response import GetStatusAppdata2XXResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetStatusAppdata2XXResponse from a JSON string
get_status_appdata2_xx_response_instance = GetStatusAppdata2XXResponse.from_json(json)
# print the JSON string representation of the object
print(GetStatusAppdata2XXResponse.to_json())

# convert the object into a dict
get_status_appdata2_xx_response_dict = get_status_appdata2_xx_response_instance.to_dict()
# create an instance of GetStatusAppdata2XXResponse from a dict
get_status_appdata2_xx_response_from_dict = GetStatusAppdata2XXResponse.from_dict(get_status_appdata2_xx_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


