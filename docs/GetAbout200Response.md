# GetAbout200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** |  | [optional] 
**total_requests** | **float** |  | [optional] 
**total_media_items** | **float** |  | [optional] 
**tz** | **str** |  | [optional] 
**app_data_path** | **str** |  | [optional] 

## Example

```python
from overseerr.models.get_about200_response import GetAbout200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetAbout200Response from a JSON string
get_about200_response_instance = GetAbout200Response.from_json(json)
# print the JSON string representation of the object
print GetAbout200Response.to_json()

# convert the object into a dict
get_about200_response_dict = get_about200_response_instance.to_dict()
# create an instance of GetAbout200Response from a dict
get_about200_response_form_dict = get_about200_response.from_dict(get_about200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


