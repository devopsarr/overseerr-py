# WebPushSettings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** |  | [optional] 
**types** | **float** |  | [optional] 

## Example

```python
from overseerr.models.web_push_settings import WebPushSettings

# TODO update the JSON string below
json = "{}"
# create an instance of WebPushSettings from a JSON string
web_push_settings_instance = WebPushSettings.from_json(json)
# print the JSON string representation of the object
print(WebPushSettings.to_json())

# convert the object into a dict
web_push_settings_dict = web_push_settings_instance.to_dict()
# create an instance of WebPushSettings from a dict
web_push_settings_from_dict = WebPushSettings.from_dict(web_push_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


