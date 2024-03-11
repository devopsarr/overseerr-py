# TestSonarrRequest


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
from overseerr.models.test_sonarr_request import TestSonarrRequest

# TODO update the JSON string below
json = "{}"
# create an instance of TestSonarrRequest from a JSON string
test_sonarr_request_instance = TestSonarrRequest.from_json(json)
# print the JSON string representation of the object
print(TestSonarrRequest.to_json())

# convert the object into a dict
test_sonarr_request_dict = test_sonarr_request_instance.to_dict()
# create an instance of TestSonarrRequest from a dict
test_sonarr_request_form_dict = test_sonarr_request.from_dict(test_sonarr_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


