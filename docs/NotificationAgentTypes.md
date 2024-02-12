# NotificationAgentTypes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**discord** | **float** |  | [optional] 
**email** | **float** |  | [optional] 
**pushbullet** | **float** |  | [optional] 
**pushover** | **float** |  | [optional] 
**slack** | **float** |  | [optional] 
**telegram** | **float** |  | [optional] 
**webhook** | **float** |  | [optional] 
**webpush** | **float** |  | [optional] 

## Example

```python
from overseerr.models.notification_agent_types import NotificationAgentTypes

# TODO update the JSON string below
json = "{}"
# create an instance of NotificationAgentTypes from a JSON string
notification_agent_types_instance = NotificationAgentTypes.from_json(json)
# print the JSON string representation of the object
print NotificationAgentTypes.to_json()

# convert the object into a dict
notification_agent_types_dict = notification_agent_types_instance.to_dict()
# create an instance of NotificationAgentTypes from a dict
notification_agent_types_form_dict = notification_agent_types.from_dict(notification_agent_types_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


