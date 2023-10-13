# GetServiceSonarrBySonarrId200Response


## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**server** | [**SonarrSettings**](SonarrSettings.md) |  | [optional] 
**profiles** | [**ServiceProfile**](ServiceProfile.md) |  | [optional] 

## Example

```python
from overseerr.models.get_service_sonarr_by_sonarr_id200_response import GetServiceSonarrBySonarrId200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GetServiceSonarrBySonarrId200Response from a JSON string
get_service_sonarr_by_sonarr_id200_response_instance = GetServiceSonarrBySonarrId200Response.from_json(json)
# print the JSON string representation of the object
print GetServiceSonarrBySonarrId200Response.to_json()

# convert the object into a dict
get_service_sonarr_by_sonarr_id200_response_dict = get_service_sonarr_by_sonarr_id200_response_instance.to_dict()
# create an instance of GetServiceSonarrBySonarrId200Response from a dict
get_service_sonarr_by_sonarr_id200_response_form_dict = get_service_sonarr_by_sonarr_id200_response.from_dict(get_service_sonarr_by_sonarr_id200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


