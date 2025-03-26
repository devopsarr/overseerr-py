# GetUserPushSubscriptions2XXResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint** | **str** |  | [optional] 
**p256dh** | **str** |  | [optional] 
**auth** | **str** |  | [optional] 
**user_agent** | **str** |  | [optional] 

## Example

```python
from overseerr.models.get_user_push_subscriptions2_xx_response import GetUserPushSubscriptions2XXResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserPushSubscriptions2XXResponse from a JSON string
get_user_push_subscriptions2_xx_response_instance = GetUserPushSubscriptions2XXResponse.from_json(json)
# print the JSON string representation of the object
print(GetUserPushSubscriptions2XXResponse.to_json())

# convert the object into a dict
get_user_push_subscriptions2_xx_response_dict = get_user_push_subscriptions2_xx_response_instance.to_dict()
# create an instance of GetUserPushSubscriptions2XXResponse from a dict
get_user_push_subscriptions2_xx_response_from_dict = GetUserPushSubscriptions2XXResponse.from_dict(get_user_push_subscriptions2_xx_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


