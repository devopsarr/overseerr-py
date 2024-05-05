# GetStatus2XXResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** |  | [optional] 
**commit_tag** | **str** |  | [optional] 
**update_available** | **bool** |  | [optional] 
**commits_behind** | **float** |  | [optional] 
**restart_required** | **bool** |  | [optional] 

## Example

```python
from overseerr.models.get_status2_xx_response import GetStatus2XXResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetStatus2XXResponse from a JSON string
get_status2_xx_response_instance = GetStatus2XXResponse.from_json(json)
# print the JSON string representation of the object
print(GetStatus2XXResponse.to_json())

# convert the object into a dict
get_status2_xx_response_dict = get_status2_xx_response_instance.to_dict()
# create an instance of GetStatus2XXResponse from a dict
get_status2_xx_response_from_dict = GetStatus2XXResponse.from_dict(get_status2_xx_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


