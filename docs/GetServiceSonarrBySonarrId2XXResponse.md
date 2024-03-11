# GetServiceSonarrBySonarrId2XXResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**server** | [**SonarrSettings**](SonarrSettings.md) |  | [optional] 
**profiles** | [**ServiceProfile**](ServiceProfile.md) |  | [optional] 

## Example

```python
from overseerr.models.get_service_sonarr_by_sonarr_id2_xx_response import GetServiceSonarrBySonarrId2XXResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetServiceSonarrBySonarrId2XXResponse from a JSON string
get_service_sonarr_by_sonarr_id2_xx_response_instance = GetServiceSonarrBySonarrId2XXResponse.from_json(json)
# print the JSON string representation of the object
print(GetServiceSonarrBySonarrId2XXResponse.to_json())

# convert the object into a dict
get_service_sonarr_by_sonarr_id2_xx_response_dict = get_service_sonarr_by_sonarr_id2_xx_response_instance.to_dict()
# create an instance of GetServiceSonarrBySonarrId2XXResponse from a dict
get_service_sonarr_by_sonarr_id2_xx_response_form_dict = get_service_sonarr_by_sonarr_id2_xx_response.from_dict(get_service_sonarr_by_sonarr_id2_xx_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


