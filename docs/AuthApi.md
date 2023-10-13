# overseerr.AuthApi

All URIs are relative to *http://localhost:5055/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_auth_local**](AuthApi.md#create_auth_local) | **POST** /auth/local | Sign in using a local account
[**create_auth_logout**](AuthApi.md#create_auth_logout) | **POST** /auth/logout | Sign out and clear session cookie
[**create_auth_plex**](AuthApi.md#create_auth_plex) | **POST** /auth/plex | Sign in using a Plex token
[**get_auth_me**](AuthApi.md#get_auth_me) | **GET** /auth/me | Get logged-in user


# **create_auth_local**
> User create_auth_local(create_auth_local_request)

Sign in using a local account

Takes an `email` and a `password` to log the user in. Generates a session cookie for use in further requests.

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
    api_instance = overseerr.AuthApi(api_client)
    create_auth_local_request = overseerr.CreateAuthLocalRequest() # CreateAuthLocalRequest | 

    try:
        # Sign in using a local account
        api_response = api_instance.create_auth_local(create_auth_local_request)
        print("The response of AuthApi->create_auth_local:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->create_auth_local: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_auth_local_request** | [**CreateAuthLocalRequest**](CreateAuthLocalRequest.md)|  | 

### Return type

[**User**](User.md)

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

# **create_auth_logout**
> CreateAuthLogout200Response create_auth_logout()

Sign out and clear session cookie

Completely clear the session cookie and associated values, effectively signing the user out.

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
    api_instance = overseerr.AuthApi(api_client)

    try:
        # Sign out and clear session cookie
        api_response = api_instance.create_auth_logout()
        print("The response of AuthApi->create_auth_logout:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->create_auth_logout: %s\n" % e)
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
    api_instance = overseerr.AuthApi(api_client)

    try:
        # Sign out and clear session cookie
        api_response = api_instance.create_auth_logout()
        print("The response of AuthApi->create_auth_logout:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->create_auth_logout: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CreateAuthLogout200Response**](CreateAuthLogout200Response.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_auth_plex**
> User create_auth_plex(create_auth_plex_request)

Sign in using a Plex token

Takes an `authToken` (Plex token) to log the user in. Generates a session cookie for use in further requests. If the user does not exist, and there are no other users, then a user will be created with full admin privileges. If a user logs in with access to the main Plex server, they will also have an account created, but without any permissions.

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
    api_instance = overseerr.AuthApi(api_client)
    create_auth_plex_request = overseerr.CreateAuthPlexRequest() # CreateAuthPlexRequest | 

    try:
        # Sign in using a Plex token
        api_response = api_instance.create_auth_plex(create_auth_plex_request)
        print("The response of AuthApi->create_auth_plex:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->create_auth_plex: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_auth_plex_request** | [**CreateAuthPlexRequest**](CreateAuthPlexRequest.md)|  | 

### Return type

[**User**](User.md)

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
    api_instance = overseerr.AuthApi(api_client)

    try:
        # Get logged-in user
        api_response = api_instance.get_auth_me()
        print("The response of AuthApi->get_auth_me:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->get_auth_me: %s\n" % e)
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
    api_instance = overseerr.AuthApi(api_client)

    try:
        # Get logged-in user
        api_response = api_instance.get_auth_me()
        print("The response of AuthApi->get_auth_me:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->get_auth_me: %s\n" % e)
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

