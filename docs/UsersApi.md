# overseerr.UsersApi

All URIs are relative to *http://localhost:5055/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_auth_reset_password**](UsersApi.md#create_auth_reset_password) | **POST** /auth/reset-password | Send a reset password email
[**create_auth_reset_password_by_guid**](UsersApi.md#create_auth_reset_password_by_guid) | **POST** /auth/reset-password/{guid} | Reset the password for a user
[**create_user**](UsersApi.md#create_user) | **POST** /user | Create new user
[**create_user_import_from_plex**](UsersApi.md#create_user_import_from_plex) | **POST** /user/import-from-plex | Import all users from Plex
[**create_user_register_push_subscription**](UsersApi.md#create_user_register_push_subscription) | **POST** /user/registerPushSubscription | Register a web push /user/registerPushSubscription
[**create_user_settings_main**](UsersApi.md#create_user_settings_main) | **POST** /user/{userId}/settings/main | Update general settings for a user
[**create_user_settings_notifications**](UsersApi.md#create_user_settings_notifications) | **POST** /user/{userId}/settings/notifications | Update notification settings for a user
[**create_user_settings_password**](UsersApi.md#create_user_settings_password) | **POST** /user/{userId}/settings/password | Update password for a user
[**create_user_settings_permissions**](UsersApi.md#create_user_settings_permissions) | **POST** /user/{userId}/settings/permissions | Update permission settings for a user
[**delete_user**](UsersApi.md#delete_user) | **DELETE** /user/{userId} | Delete user by ID
[**get_auth_me**](UsersApi.md#get_auth_me) | **GET** /auth/me | Get logged-in user
[**get_user**](UsersApi.md#get_user) | **GET** /user | Get all users
[**get_user_by_user_id**](UsersApi.md#get_user_by_user_id) | **GET** /user/{userId} | Get user by ID
[**get_user_quota**](UsersApi.md#get_user_quota) | **GET** /user/{userId}/quota | Get quotas for a specific user
[**get_user_requests**](UsersApi.md#get_user_requests) | **GET** /user/{userId}/requests | Get requests for a specific user
[**get_user_settings_main**](UsersApi.md#get_user_settings_main) | **GET** /user/{userId}/settings/main | Get general settings for a user
[**get_user_settings_notifications**](UsersApi.md#get_user_settings_notifications) | **GET** /user/{userId}/settings/notifications | Get notification settings for a user
[**get_user_settings_password**](UsersApi.md#get_user_settings_password) | **GET** /user/{userId}/settings/password | Get password page informatiom
[**get_user_settings_permissions**](UsersApi.md#get_user_settings_permissions) | **GET** /user/{userId}/settings/permissions | Get permission settings for a user
[**get_user_watch_data**](UsersApi.md#get_user_watch_data) | **GET** /user/{userId}/watch_data | Get watch data
[**get_user_watchlist**](UsersApi.md#get_user_watchlist) | **GET** /user/{userId}/watchlist | Get the Plex watchlist for a specific user
[**list_plex_users**](UsersApi.md#list_plex_users) | **GET** /settings/plex/users | Get Plex users
[**put_user**](UsersApi.md#put_user) | **PUT** /user | Update batch of users
[**update_user**](UsersApi.md#update_user) | **PUT** /user/{userId} | Update a user by user ID


# **create_auth_reset_password**
> CreateAuthLogout200Response create_auth_reset_password(create_auth_reset_password_request)

Send a reset password email

Sends a reset password email to the email if the user exists

### Example

```python
from __future__ import print_function
import time
import os
import overseerr
from overseerr.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5055/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = overseerr.Configuration(
    host = "http://localhost:5055/api/v1"
)


# Enter a context with an instance of the API client
with overseerr.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = overseerr.UsersApi(api_client)
    create_auth_reset_password_request = overseerr.CreateAuthResetPasswordRequest() # CreateAuthResetPasswordRequest | 

    try:
        # Send a reset password email
        api_response = api_instance.create_auth_reset_password(create_auth_reset_password_request)
        print("The response of UsersApi->create_auth_reset_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->create_auth_reset_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_auth_reset_password_request** | [**CreateAuthResetPasswordRequest**](CreateAuthResetPasswordRequest.md)|  | 

### Return type

[**CreateAuthLogout200Response**](CreateAuthLogout200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_auth_reset_password_by_guid**
> CreateAuthLogout200Response create_auth_reset_password_by_guid(guid, create_auth_reset_password_by_guid_request)

Reset the password for a user

Resets the password for a user if the given guid is connected to a user

### Example

```python
from __future__ import print_function
import time
import os
import overseerr
from overseerr.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5055/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = overseerr.Configuration(
    host = "http://localhost:5055/api/v1"
)


# Enter a context with an instance of the API client
with overseerr.ApiClient() as api_client:
    # Create an instance of the API class
    api_instance = overseerr.UsersApi(api_client)
    guid = '9afef5a7-ec89-4d5f-9397-261e96970b50' # str | 
    create_auth_reset_password_by_guid_request = overseerr.CreateAuthResetPasswordByGuidRequest() # CreateAuthResetPasswordByGuidRequest | 

    try:
        # Reset the password for a user
        api_response = api_instance.create_auth_reset_password_by_guid(guid, create_auth_reset_password_by_guid_request)
        print("The response of UsersApi->create_auth_reset_password_by_guid:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->create_auth_reset_password_by_guid: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**|  | 
 **create_auth_reset_password_by_guid_request** | [**CreateAuthResetPasswordByGuidRequest**](CreateAuthResetPasswordByGuidRequest.md)|  | 

### Return type

[**CreateAuthLogout200Response**](CreateAuthLogout200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user**
> User create_user(create_user_request)

Create new user

Creates a new user. Requires the `MANAGE_USERS` permission. 

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import os
import overseerr
from overseerr.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5055/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = overseerr.Configuration(
    host = "http://localhost:5055/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with overseerr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = overseerr.UsersApi(api_client)
    create_user_request = overseerr.CreateUserRequest() # CreateUserRequest | 

    try:
        # Create new user
        api_response = api_instance.create_user(create_user_request)
        print("The response of UsersApi->create_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->create_user: %s\n" % e)
```

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import os
import overseerr
from overseerr.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5055/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = overseerr.Configuration(
    host = "http://localhost:5055/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with overseerr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = overseerr.UsersApi(api_client)
    create_user_request = overseerr.CreateUserRequest() # CreateUserRequest | 

    try:
        # Create new user
        api_response = api_instance.create_user(create_user_request)
        print("The response of UsersApi->create_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->create_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_user_request** | [**CreateUserRequest**](CreateUserRequest.md)|  | 

### Return type

[**User**](User.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | The created user |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user_import_from_plex**
> List[User] create_user_import_from_plex(create_user_import_from_plex_request=create_user_import_from_plex_request)

Import all users from Plex

Fetches and imports users from the Plex server. If a list of Plex IDs is provided in the request body, only the specified users will be imported. Otherwise, all users will be imported.  Requires the `MANAGE_USERS` permission. 

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import os
import overseerr
from overseerr.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5055/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = overseerr.Configuration(
    host = "http://localhost:5055/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with overseerr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = overseerr.UsersApi(api_client)
    create_user_import_from_plex_request = overseerr.CreateUserImportFromPlexRequest() # CreateUserImportFromPlexRequest |  (optional)

    try:
        # Import all users from Plex
        api_response = api_instance.create_user_import_from_plex(create_user_import_from_plex_request=create_user_import_from_plex_request)
        print("The response of UsersApi->create_user_import_from_plex:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->create_user_import_from_plex: %s\n" % e)
```

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import os
import overseerr
from overseerr.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5055/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = overseerr.Configuration(
    host = "http://localhost:5055/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with overseerr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = overseerr.UsersApi(api_client)
    create_user_import_from_plex_request = overseerr.CreateUserImportFromPlexRequest() # CreateUserImportFromPlexRequest |  (optional)

    try:
        # Import all users from Plex
        api_response = api_instance.create_user_import_from_plex(create_user_import_from_plex_request=create_user_import_from_plex_request)
        print("The response of UsersApi->create_user_import_from_plex:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->create_user_import_from_plex: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_user_import_from_plex_request** | [**CreateUserImportFromPlexRequest**](CreateUserImportFromPlexRequest.md)|  | [optional] 

### Return type

[**List[User]**](User.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | A list of the newly created users |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user_register_push_subscription**
> create_user_register_push_subscription(create_user_register_push_subscription_request)

Register a web push /user/registerPushSubscription

Registers a web push subscription for the logged-in user

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import os
import overseerr
from overseerr.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5055/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = overseerr.Configuration(
    host = "http://localhost:5055/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with overseerr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = overseerr.UsersApi(api_client)
    create_user_register_push_subscription_request = overseerr.CreateUserRegisterPushSubscriptionRequest() # CreateUserRegisterPushSubscriptionRequest | 

    try:
        # Register a web push /user/registerPushSubscription
        api_instance.create_user_register_push_subscription(create_user_register_push_subscription_request)
    except Exception as e:
        print("Exception when calling UsersApi->create_user_register_push_subscription: %s\n" % e)
```

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import os
import overseerr
from overseerr.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5055/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = overseerr.Configuration(
    host = "http://localhost:5055/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with overseerr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = overseerr.UsersApi(api_client)
    create_user_register_push_subscription_request = overseerr.CreateUserRegisterPushSubscriptionRequest() # CreateUserRegisterPushSubscriptionRequest | 

    try:
        # Register a web push /user/registerPushSubscription
        api_instance.create_user_register_push_subscription(create_user_register_push_subscription_request)
    except Exception as e:
        print("Exception when calling UsersApi->create_user_register_push_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_user_register_push_subscription_request** | [**CreateUserRegisterPushSubscriptionRequest**](CreateUserRegisterPushSubscriptionRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Successfully registered push subscription |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user_settings_main**
> GetUserSettingsMain200Response create_user_settings_main(user_id, create_user_settings_main_request)

Update general settings for a user

Updates and returns general settings for a specific user. Requires `MANAGE_USERS` permission if editing other users.

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import os
import overseerr
from overseerr.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5055/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = overseerr.Configuration(
    host = "http://localhost:5055/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with overseerr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = overseerr.UsersApi(api_client)
    user_id = 3.4 # float | 
    create_user_settings_main_request = overseerr.CreateUserSettingsMainRequest() # CreateUserSettingsMainRequest | 

    try:
        # Update general settings for a user
        api_response = api_instance.create_user_settings_main(user_id, create_user_settings_main_request)
        print("The response of UsersApi->create_user_settings_main:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->create_user_settings_main: %s\n" % e)
```

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import os
import overseerr
from overseerr.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5055/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = overseerr.Configuration(
    host = "http://localhost:5055/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with overseerr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = overseerr.UsersApi(api_client)
    user_id = 3.4 # float | 
    create_user_settings_main_request = overseerr.CreateUserSettingsMainRequest() # CreateUserSettingsMainRequest | 

    try:
        # Update general settings for a user
        api_response = api_instance.create_user_settings_main(user_id, create_user_settings_main_request)
        print("The response of UsersApi->create_user_settings_main:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->create_user_settings_main: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **float**|  | 
 **create_user_settings_main_request** | [**CreateUserSettingsMainRequest**](CreateUserSettingsMainRequest.md)|  | 

### Return type

[**GetUserSettingsMain200Response**](GetUserSettingsMain200Response.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated user general settings returned |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user_settings_notifications**
> UserSettingsNotifications create_user_settings_notifications(user_id, user_settings_notifications)

Update notification settings for a user

Updates and returns notification settings for a specific user. Requires `MANAGE_USERS` permission if editing other users.

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import os
import overseerr
from overseerr.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5055/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = overseerr.Configuration(
    host = "http://localhost:5055/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with overseerr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = overseerr.UsersApi(api_client)
    user_id = 3.4 # float | 
    user_settings_notifications = overseerr.UserSettingsNotifications() # UserSettingsNotifications | 

    try:
        # Update notification settings for a user
        api_response = api_instance.create_user_settings_notifications(user_id, user_settings_notifications)
        print("The response of UsersApi->create_user_settings_notifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->create_user_settings_notifications: %s\n" % e)
```

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import os
import overseerr
from overseerr.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5055/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = overseerr.Configuration(
    host = "http://localhost:5055/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with overseerr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = overseerr.UsersApi(api_client)
    user_id = 3.4 # float | 
    user_settings_notifications = overseerr.UserSettingsNotifications() # UserSettingsNotifications | 

    try:
        # Update notification settings for a user
        api_response = api_instance.create_user_settings_notifications(user_id, user_settings_notifications)
        print("The response of UsersApi->create_user_settings_notifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->create_user_settings_notifications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **float**|  | 
 **user_settings_notifications** | [**UserSettingsNotifications**](UserSettingsNotifications.md)|  | 

### Return type

[**UserSettingsNotifications**](UserSettingsNotifications.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated user notification settings returned |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user_settings_password**
> create_user_settings_password(user_id, create_user_settings_password_request)

Update password for a user

Updates a user's password. Requires `MANAGE_USERS` permission if editing other users.

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import os
import overseerr
from overseerr.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5055/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = overseerr.Configuration(
    host = "http://localhost:5055/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with overseerr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = overseerr.UsersApi(api_client)
    user_id = 3.4 # float | 
    create_user_settings_password_request = overseerr.CreateUserSettingsPasswordRequest() # CreateUserSettingsPasswordRequest | 

    try:
        # Update password for a user
        api_instance.create_user_settings_password(user_id, create_user_settings_password_request)
    except Exception as e:
        print("Exception when calling UsersApi->create_user_settings_password: %s\n" % e)
```

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import os
import overseerr
from overseerr.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5055/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = overseerr.Configuration(
    host = "http://localhost:5055/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with overseerr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = overseerr.UsersApi(api_client)
    user_id = 3.4 # float | 
    create_user_settings_password_request = overseerr.CreateUserSettingsPasswordRequest() # CreateUserSettingsPasswordRequest | 

    try:
        # Update password for a user
        api_instance.create_user_settings_password(user_id, create_user_settings_password_request)
    except Exception as e:
        print("Exception when calling UsersApi->create_user_settings_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **float**|  | 
 **create_user_settings_password_request** | [**CreateUserSettingsPasswordRequest**](CreateUserSettingsPasswordRequest.md)|  | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | User password updated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_user_settings_permissions**
> GetUserSettingsPermissions200Response create_user_settings_permissions(user_id, create_user_settings_permissions_request)

Update permission settings for a user

Updates and returns permission settings for a specific user. Requires `MANAGE_USERS` permission if editing other users.

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import os
import overseerr
from overseerr.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5055/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = overseerr.Configuration(
    host = "http://localhost:5055/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with overseerr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = overseerr.UsersApi(api_client)
    user_id = 3.4 # float | 
    create_user_settings_permissions_request = overseerr.CreateUserSettingsPermissionsRequest() # CreateUserSettingsPermissionsRequest | 

    try:
        # Update permission settings for a user
        api_response = api_instance.create_user_settings_permissions(user_id, create_user_settings_permissions_request)
        print("The response of UsersApi->create_user_settings_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->create_user_settings_permissions: %s\n" % e)
```

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import os
import overseerr
from overseerr.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5055/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = overseerr.Configuration(
    host = "http://localhost:5055/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with overseerr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = overseerr.UsersApi(api_client)
    user_id = 3.4 # float | 
    create_user_settings_permissions_request = overseerr.CreateUserSettingsPermissionsRequest() # CreateUserSettingsPermissionsRequest | 

    try:
        # Update permission settings for a user
        api_response = api_instance.create_user_settings_permissions(user_id, create_user_settings_permissions_request)
        print("The response of UsersApi->create_user_settings_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->create_user_settings_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **float**|  | 
 **create_user_settings_permissions_request** | [**CreateUserSettingsPermissionsRequest**](CreateUserSettingsPermissionsRequest.md)|  | 

### Return type

[**GetUserSettingsPermissions200Response**](GetUserSettingsPermissions200Response.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Updated user general settings returned |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_user**
> User delete_user(user_id)

Delete user by ID

Deletes the user with the provided userId. Requires the `MANAGE_USERS` permission.

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import os
import overseerr
from overseerr.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5055/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = overseerr.Configuration(
    host = "http://localhost:5055/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with overseerr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = overseerr.UsersApi(api_client)
    user_id = 3.4 # float | 

    try:
        # Delete user by ID
        api_response = api_instance.delete_user(user_id)
        print("The response of UsersApi->delete_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->delete_user: %s\n" % e)
```

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import os
import overseerr
from overseerr.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5055/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = overseerr.Configuration(
    host = "http://localhost:5055/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with overseerr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = overseerr.UsersApi(api_client)
    user_id = 3.4 # float | 

    try:
        # Delete user by ID
        api_response = api_instance.delete_user(user_id)
        print("The response of UsersApi->delete_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->delete_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **float**|  | 

### Return type

[**User**](User.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User successfully deleted |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_auth_me**
> User get_auth_me()

Get logged-in user

Returns the currently logged-in user.

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import os
import overseerr
from overseerr.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5055/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = overseerr.Configuration(
    host = "http://localhost:5055/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with overseerr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = overseerr.UsersApi(api_client)

    try:
        # Get logged-in user
        api_response = api_instance.get_auth_me()
        print("The response of UsersApi->get_auth_me:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_auth_me: %s\n" % e)
```

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import os
import overseerr
from overseerr.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5055/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = overseerr.Configuration(
    host = "http://localhost:5055/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with overseerr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = overseerr.UsersApi(api_client)

    try:
        # Get logged-in user
        api_response = api_instance.get_auth_me()
        print("The response of UsersApi->get_auth_me:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_auth_me: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**User**](User.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Object containing the logged-in user in JSON |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user**
> GetUser200Response get_user(take=take, skip=skip, sort=sort)

Get all users

Returns all users in a JSON object.

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import os
import overseerr
from overseerr.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5055/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = overseerr.Configuration(
    host = "http://localhost:5055/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with overseerr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = overseerr.UsersApi(api_client)
    take = 20 # float |  (optional)
    skip = 0 # float |  (optional)
    sort = 'created' # str |  (optional) (default to 'created')

    try:
        # Get all users
        api_response = api_instance.get_user(take=take, skip=skip, sort=sort)
        print("The response of UsersApi->get_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_user: %s\n" % e)
```

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import os
import overseerr
from overseerr.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5055/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = overseerr.Configuration(
    host = "http://localhost:5055/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with overseerr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = overseerr.UsersApi(api_client)
    take = 20 # float |  (optional)
    skip = 0 # float |  (optional)
    sort = 'created' # str |  (optional) (default to 'created')

    try:
        # Get all users
        api_response = api_instance.get_user(take=take, skip=skip, sort=sort)
        print("The response of UsersApi->get_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **take** | **float**|  | [optional] 
 **skip** | **float**|  | [optional] 
 **sort** | **str**|  | [optional] [default to &#39;created&#39;]

### Return type

[**GetUser200Response**](GetUser200Response.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A JSON array of all users |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_by_user_id**
> User get_user_by_user_id(user_id)

Get user by ID

Retrieves user details in a JSON object. Requires the `MANAGE_USERS` permission. 

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import os
import overseerr
from overseerr.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5055/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = overseerr.Configuration(
    host = "http://localhost:5055/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with overseerr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = overseerr.UsersApi(api_client)
    user_id = 3.4 # float | 

    try:
        # Get user by ID
        api_response = api_instance.get_user_by_user_id(user_id)
        print("The response of UsersApi->get_user_by_user_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_user_by_user_id: %s\n" % e)
```

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import os
import overseerr
from overseerr.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5055/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = overseerr.Configuration(
    host = "http://localhost:5055/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with overseerr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = overseerr.UsersApi(api_client)
    user_id = 3.4 # float | 

    try:
        # Get user by ID
        api_response = api_instance.get_user_by_user_id(user_id)
        print("The response of UsersApi->get_user_by_user_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_user_by_user_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **float**|  | 

### Return type

[**User**](User.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Users details in JSON |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_quota**
> GetUserQuota200Response get_user_quota(user_id)

Get quotas for a specific user

Returns quota details for a user in a JSON object. Requires `MANAGE_USERS` permission if viewing other users. 

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import os
import overseerr
from overseerr.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5055/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = overseerr.Configuration(
    host = "http://localhost:5055/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with overseerr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = overseerr.UsersApi(api_client)
    user_id = 3.4 # float | 

    try:
        # Get quotas for a specific user
        api_response = api_instance.get_user_quota(user_id)
        print("The response of UsersApi->get_user_quota:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_user_quota: %s\n" % e)
```

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import os
import overseerr
from overseerr.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5055/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = overseerr.Configuration(
    host = "http://localhost:5055/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with overseerr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = overseerr.UsersApi(api_client)
    user_id = 3.4 # float | 

    try:
        # Get quotas for a specific user
        api_response = api_instance.get_user_quota(user_id)
        print("The response of UsersApi->get_user_quota:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_user_quota: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **float**|  | 

### Return type

[**GetUserQuota200Response**](GetUserQuota200Response.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User quota details in JSON |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_requests**
> GetUserRequests200Response get_user_requests(user_id, take=take, skip=skip)

Get requests for a specific user

Retrieves a user's requests in a JSON object. 

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import os
import overseerr
from overseerr.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5055/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = overseerr.Configuration(
    host = "http://localhost:5055/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with overseerr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = overseerr.UsersApi(api_client)
    user_id = 3.4 # float | 
    take = 20 # float |  (optional)
    skip = 0 # float |  (optional)

    try:
        # Get requests for a specific user
        api_response = api_instance.get_user_requests(user_id, take=take, skip=skip)
        print("The response of UsersApi->get_user_requests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_user_requests: %s\n" % e)
```

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import os
import overseerr
from overseerr.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5055/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = overseerr.Configuration(
    host = "http://localhost:5055/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with overseerr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = overseerr.UsersApi(api_client)
    user_id = 3.4 # float | 
    take = 20 # float |  (optional)
    skip = 0 # float |  (optional)

    try:
        # Get requests for a specific user
        api_response = api_instance.get_user_requests(user_id, take=take, skip=skip)
        print("The response of UsersApi->get_user_requests:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_user_requests: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **float**|  | 
 **take** | **float**|  | [optional] 
 **skip** | **float**|  | [optional] 

### Return type

[**GetUserRequests200Response**](GetUserRequests200Response.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User&#39;s requests returned |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_settings_main**
> GetUserSettingsMain200Response get_user_settings_main(user_id)

Get general settings for a user

Returns general settings for a specific user. Requires `MANAGE_USERS` permission if viewing other users.

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import os
import overseerr
from overseerr.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5055/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = overseerr.Configuration(
    host = "http://localhost:5055/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with overseerr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = overseerr.UsersApi(api_client)
    user_id = 3.4 # float | 

    try:
        # Get general settings for a user
        api_response = api_instance.get_user_settings_main(user_id)
        print("The response of UsersApi->get_user_settings_main:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_user_settings_main: %s\n" % e)
```

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import os
import overseerr
from overseerr.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5055/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = overseerr.Configuration(
    host = "http://localhost:5055/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with overseerr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = overseerr.UsersApi(api_client)
    user_id = 3.4 # float | 

    try:
        # Get general settings for a user
        api_response = api_instance.get_user_settings_main(user_id)
        print("The response of UsersApi->get_user_settings_main:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_user_settings_main: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **float**|  | 

### Return type

[**GetUserSettingsMain200Response**](GetUserSettingsMain200Response.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User general settings returned |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_settings_notifications**
> UserSettingsNotifications get_user_settings_notifications(user_id)

Get notification settings for a user

Returns notification settings for a specific user. Requires `MANAGE_USERS` permission if viewing other users.

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import os
import overseerr
from overseerr.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5055/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = overseerr.Configuration(
    host = "http://localhost:5055/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with overseerr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = overseerr.UsersApi(api_client)
    user_id = 3.4 # float | 

    try:
        # Get notification settings for a user
        api_response = api_instance.get_user_settings_notifications(user_id)
        print("The response of UsersApi->get_user_settings_notifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_user_settings_notifications: %s\n" % e)
```

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import os
import overseerr
from overseerr.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5055/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = overseerr.Configuration(
    host = "http://localhost:5055/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with overseerr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = overseerr.UsersApi(api_client)
    user_id = 3.4 # float | 

    try:
        # Get notification settings for a user
        api_response = api_instance.get_user_settings_notifications(user_id)
        print("The response of UsersApi->get_user_settings_notifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_user_settings_notifications: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **float**|  | 

### Return type

[**UserSettingsNotifications**](UserSettingsNotifications.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User notification settings returned |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_settings_password**
> GetUserSettingsPassword200Response get_user_settings_password(user_id)

Get password page informatiom

Returns important data for the password page to function correctly. Requires `MANAGE_USERS` permission if viewing other users.

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import os
import overseerr
from overseerr.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5055/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = overseerr.Configuration(
    host = "http://localhost:5055/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with overseerr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = overseerr.UsersApi(api_client)
    user_id = 3.4 # float | 

    try:
        # Get password page informatiom
        api_response = api_instance.get_user_settings_password(user_id)
        print("The response of UsersApi->get_user_settings_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_user_settings_password: %s\n" % e)
```

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import os
import overseerr
from overseerr.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5055/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = overseerr.Configuration(
    host = "http://localhost:5055/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with overseerr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = overseerr.UsersApi(api_client)
    user_id = 3.4 # float | 

    try:
        # Get password page informatiom
        api_response = api_instance.get_user_settings_password(user_id)
        print("The response of UsersApi->get_user_settings_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_user_settings_password: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **float**|  | 

### Return type

[**GetUserSettingsPassword200Response**](GetUserSettingsPassword200Response.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User password page information returned |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_settings_permissions**
> GetUserSettingsPermissions200Response get_user_settings_permissions(user_id)

Get permission settings for a user

Returns permission settings for a specific user. Requires `MANAGE_USERS` permission if viewing other users.

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import os
import overseerr
from overseerr.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5055/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = overseerr.Configuration(
    host = "http://localhost:5055/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with overseerr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = overseerr.UsersApi(api_client)
    user_id = 3.4 # float | 

    try:
        # Get permission settings for a user
        api_response = api_instance.get_user_settings_permissions(user_id)
        print("The response of UsersApi->get_user_settings_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_user_settings_permissions: %s\n" % e)
```

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import os
import overseerr
from overseerr.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5055/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = overseerr.Configuration(
    host = "http://localhost:5055/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with overseerr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = overseerr.UsersApi(api_client)
    user_id = 3.4 # float | 

    try:
        # Get permission settings for a user
        api_response = api_instance.get_user_settings_permissions(user_id)
        print("The response of UsersApi->get_user_settings_permissions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_user_settings_permissions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **float**|  | 

### Return type

[**GetUserSettingsPermissions200Response**](GetUserSettingsPermissions200Response.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | User permission settings returned |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_watch_data**
> GetUserWatchData200Response get_user_watch_data(user_id)

Get watch data

Returns play count, play duration, and recently watched media.  Requires the `ADMIN` permission to fetch results for other users. 

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import os
import overseerr
from overseerr.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5055/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = overseerr.Configuration(
    host = "http://localhost:5055/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with overseerr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = overseerr.UsersApi(api_client)
    user_id = 3.4 # float | 

    try:
        # Get watch data
        api_response = api_instance.get_user_watch_data(user_id)
        print("The response of UsersApi->get_user_watch_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_user_watch_data: %s\n" % e)
```

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import os
import overseerr
from overseerr.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5055/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = overseerr.Configuration(
    host = "http://localhost:5055/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with overseerr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = overseerr.UsersApi(api_client)
    user_id = 3.4 # float | 

    try:
        # Get watch data
        api_response = api_instance.get_user_watch_data(user_id)
        print("The response of UsersApi->get_user_watch_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_user_watch_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **float**|  | 

### Return type

[**GetUserWatchData200Response**](GetUserWatchData200Response.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Users |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_user_watchlist**
> GetUserWatchlist200Response get_user_watchlist(user_id, page=page)

Get the Plex watchlist for a specific user

Retrieves a user's Plex Watchlist in a JSON object. 

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import os
import overseerr
from overseerr.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5055/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = overseerr.Configuration(
    host = "http://localhost:5055/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with overseerr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = overseerr.UsersApi(api_client)
    user_id = 3.4 # float | 
    page = 1 # float |  (optional) (default to 1)

    try:
        # Get the Plex watchlist for a specific user
        api_response = api_instance.get_user_watchlist(user_id, page=page)
        print("The response of UsersApi->get_user_watchlist:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_user_watchlist: %s\n" % e)
```

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import os
import overseerr
from overseerr.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5055/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = overseerr.Configuration(
    host = "http://localhost:5055/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with overseerr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = overseerr.UsersApi(api_client)
    user_id = 3.4 # float | 
    page = 1 # float |  (optional) (default to 1)

    try:
        # Get the Plex watchlist for a specific user
        api_response = api_instance.get_user_watchlist(user_id, page=page)
        print("The response of UsersApi->get_user_watchlist:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->get_user_watchlist: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **float**|  | 
 **page** | **float**|  | [optional] [default to 1]

### Return type

[**GetUserWatchlist200Response**](GetUserWatchlist200Response.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Watchlist data returned |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_plex_users**
> List[ListPlexUsers200ResponseInner] list_plex_users()

Get Plex users

Returns a list of Plex users in a JSON array.  Requires the `MANAGE_USERS` permission. 

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import os
import overseerr
from overseerr.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5055/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = overseerr.Configuration(
    host = "http://localhost:5055/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with overseerr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = overseerr.UsersApi(api_client)

    try:
        # Get Plex users
        api_response = api_instance.list_plex_users()
        print("The response of UsersApi->list_plex_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->list_plex_users: %s\n" % e)
```

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import os
import overseerr
from overseerr.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5055/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = overseerr.Configuration(
    host = "http://localhost:5055/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with overseerr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = overseerr.UsersApi(api_client)

    try:
        # Get Plex users
        api_response = api_instance.list_plex_users()
        print("The response of UsersApi->list_plex_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->list_plex_users: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List[ListPlexUsers200ResponseInner]**](ListPlexUsers200ResponseInner.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Plex users |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **put_user**
> List[User] put_user(put_user_request)

Update batch of users

Update users with given IDs with provided values in request `body.settings`. You cannot update users' Plex tokens through this request.  Requires the `MANAGE_USERS` permission. 

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import os
import overseerr
from overseerr.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5055/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = overseerr.Configuration(
    host = "http://localhost:5055/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with overseerr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = overseerr.UsersApi(api_client)
    put_user_request = overseerr.PutUserRequest() # PutUserRequest | 

    try:
        # Update batch of users
        api_response = api_instance.put_user(put_user_request)
        print("The response of UsersApi->put_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->put_user: %s\n" % e)
```

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import os
import overseerr
from overseerr.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5055/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = overseerr.Configuration(
    host = "http://localhost:5055/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with overseerr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = overseerr.UsersApi(api_client)
    put_user_request = overseerr.PutUserRequest() # PutUserRequest | 

    try:
        # Update batch of users
        api_response = api_instance.put_user(put_user_request)
        print("The response of UsersApi->put_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->put_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **put_user_request** | [**PutUserRequest**](PutUserRequest.md)|  | 

### Return type

[**List[User]**](User.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated user details |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_user**
> User update_user(user_id, user)

Update a user by user ID

Update a user with the provided values. You cannot update a user's Plex token through this request.  Requires the `MANAGE_USERS` permission. 

### Example

* Api Key Authentication (apiKey):
```python
from __future__ import print_function
import time
import os
import overseerr
from overseerr.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5055/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = overseerr.Configuration(
    host = "http://localhost:5055/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with overseerr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = overseerr.UsersApi(api_client)
    user_id = 3.4 # float | 
    user = overseerr.User() # User | 

    try:
        # Update a user by user ID
        api_response = api_instance.update_user(user_id, user)
        print("The response of UsersApi->update_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->update_user: %s\n" % e)
```

* Api Key Authentication (cookieAuth):
```python
from __future__ import print_function
import time
import os
import overseerr
from overseerr.rest import ApiException
from pprint import pprint
# Defining the host is optional and defaults to http://localhost:5055/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = overseerr.Configuration(
    host = "http://localhost:5055/api/v1"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: apiKey
configuration.api_key['apiKey'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['apiKey'] = 'Bearer'

# Configure API key authorization: cookieAuth
configuration.api_key['cookieAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['cookieAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with overseerr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = overseerr.UsersApi(api_client)
    user_id = 3.4 # float | 
    user = overseerr.User() # User | 

    try:
        # Update a user by user ID
        api_response = api_instance.update_user(user_id, user)
        print("The response of UsersApi->update_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->update_user: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user_id** | **float**|  | 
 **user** | [**User**](User.md)|  | 

### Return type

[**User**](User.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successfully updated user details |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

