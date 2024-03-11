# TestRadarrRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hostname** | **str** |  | 
**port** | **float** |  | 
**api_key** | **str** |  | 
**use_ssl** | **bool** |  | 
**base_url** | **str** |  | [optional] 

## Example

```python
from overseerr.models.test_radarr_request import TestRadarrRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TestRadarrRequest from a JSON string
test_radarr_request_instance = TestRadarrRequest.from_json(json)
# print the JSON string representation of the object
print(TestRadarrRequest.to_json())

# convert the object into a dict
test_radarr_request_dict = test_radarr_request_instance.to_dict()
# create an instance of TestRadarrRequest from a dict
test_radarr_request_form_dict = test_radarr_request.from_dict(test_radarr_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


