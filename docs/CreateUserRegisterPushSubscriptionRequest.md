# CreateUserRegisterPushSubscriptionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endpoint** | **str** |  | 
**auth** | **str** |  | 
**p256dh** | **str** |  | 
**user_agent** | **str** |  | [optional] 

## Example

```python
from overseerr.models.create_user_register_push_subscription_request import CreateUserRegisterPushSubscriptionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateUserRegisterPushSubscriptionRequest from a JSON string
create_user_register_push_subscription_request_instance = CreateUserRegisterPushSubscriptionRequest.from_json(json)
# print the JSON string representation of the object
print(CreateUserRegisterPushSubscriptionRequest.to_json())

# convert the object into a dict
create_user_register_push_subscription_request_dict = create_user_register_push_subscription_request_instance.to_dict()
# create an instance of CreateUserRegisterPushSubscriptionRequest from a dict
create_user_register_push_subscription_request_from_dict = CreateUserRegisterPushSubscriptionRequest.from_dict(create_user_register_push_subscription_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


