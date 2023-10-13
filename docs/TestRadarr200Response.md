# TestRadarr200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**profiles** | [**List[ServiceProfile]**](ServiceProfile.md) |  | [optional] 

## Example

```python
from overseerr.models.test_radarr200_response import TestRadarr200Response

# TODO update the JSON string below
json = "{}"
# create an instance of TestRadarr200Response from a JSON string
test_radarr200_response_instance = TestRadarr200Response.from_json(json)
# print the JSON string representation of the object
print TestRadarr200Response.to_json()

# convert the object into a dict
test_radarr200_response_dict = test_radarr200_response_instance.to_dict()
# create an instance of TestRadarr200Response from a dict
test_radarr200_response_form_dict = test_radarr200_response.from_dict(test_radarr200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


