# GetRequestCount2XXResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **float** |  | [optional] 
**movie** | **float** |  | [optional] 
**tv** | **float** |  | [optional] 
**pending** | **float** |  | [optional] 
**approved** | **float** |  | [optional] 
**declined** | **float** |  | [optional] 
**processing** | **float** |  | [optional] 
**available** | **float** |  | [optional] 

## Example

```python
from overseerr.models.get_request_count2_xx_response import GetRequestCount2XXResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetRequestCount2XXResponse from a JSON string
get_request_count2_xx_response_instance = GetRequestCount2XXResponse.from_json(json)
# print the JSON string representation of the object
print(GetRequestCount2XXResponse.to_json())

# convert the object into a dict
get_request_count2_xx_response_dict = get_request_count2_xx_response_instance.to_dict()
# create an instance of GetRequestCount2XXResponse from a dict
get_request_count2_xx_response_form_dict = get_request_count2_xx_response.from_dict(get_request_count2_xx_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


