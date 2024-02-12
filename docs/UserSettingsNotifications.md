# UserSettingsNotifications


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**notification_types** | [**NotificationAgentTypes**](NotificationAgentTypes.md) |  | [optional] 
**email_enabled** | **bool** |  | [optional] 
**pgp_key** | **str** |  | [optional] 
**discord_enabled** | **bool** |  | [optional] 
**discord_enabled_types** | **float** |  | [optional] 
**discord_id** | **str** |  | [optional] 
**pushbullet_access_token** | **str** |  | [optional] 
**pushover_application_token** | **str** |  | [optional] 
**pushover_user_key** | **str** |  | [optional] 
**telegram_enabled** | **bool** |  | [optional] 
**telegram_bot_username** | **str** |  | [optional] 
**telegram_chat_id** | **str** |  | [optional] 
**telegram_send_silently** | **bool** |  | [optional] 

## Example

```python
from overseerr.models.user_settings_notifications import UserSettingsNotifications

# TODO update the JSON string below
json = "{}"
# create an instance of UserSettingsNotifications from a JSON string
user_settings_notifications_instance = UserSettingsNotifications.from_json(json)
# print the JSON string representation of the object
print UserSettingsNotifications.to_json()

# convert the object into a dict
user_settings_notifications_dict = user_settings_notifications_instance.to_dict()
# create an instance of UserSettingsNotifications from a dict
user_settings_notifications_form_dict = user_settings_notifications.from_dict(user_settings_notifications_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


