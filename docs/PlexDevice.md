# PlexDevice


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**product** | **str** |  | 
**product_version** | **str** |  | 
**platform** | **str** |  | 
**platform_version** | **str** |  | [optional] 
**device** | **str** |  | 
**client_identifier** | **str** |  | 
**created_at** | **str** |  | 
**last_seen_at** | **str** |  | 
**provides** | **List[str]** |  | 
**owned** | **bool** |  | 
**owner_id** | **str** |  | [optional] 
**home** | **bool** |  | [optional] 
**source_title** | **str** |  | [optional] 
**access_token** | **str** |  | [optional] 
**public_address** | **str** |  | [optional] 
**https_required** | **bool** |  | [optional] 
**synced** | **bool** |  | [optional] 
**relay** | **bool** |  | [optional] 
**dns_rebinding_protection** | **bool** |  | [optional] 
**nat_loopback_supported** | **bool** |  | [optional] 
**public_address_matches** | **bool** |  | [optional] 
**presence** | **bool** |  | [optional] 
**connection** | [**List[PlexConnection]**](PlexConnection.md) |  | 

## Example

```python
from overseerr.models.plex_device import PlexDevice

# TODO update the JSON string below
json = "{}"
# create an instance of PlexDevice from a JSON string
plex_device_instance = PlexDevice.from_json(json)
# print the JSON string representation of the object
print(PlexDevice.to_json())

# convert the object into a dict
plex_device_dict = plex_device_instance.to_dict()
# create an instance of PlexDevice from a dict
plex_device_form_dict = plex_device.from_dict(plex_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


