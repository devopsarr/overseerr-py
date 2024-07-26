# overseerr.RequestApi

All URIs are relative to *http://localhost:5055/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_request**](RequestApi.md#create_request) | **POST** /request | Create new request
[**create_request_by_status**](RequestApi.md#create_request_by_status) | **POST** /request/{requestId}/{status} | Update a request&#39;s status
[**create_request_retry**](RequestApi.md#create_request_retry) | **POST** /request/{requestId}/retry | Retry failed request
[**delete_request**](RequestApi.md#delete_request) | **DELETE** /request/{requestId} | Delete request
[**get_request**](RequestApi.md#get_request) | **GET** /request | Get all requests
[**get_request_by_request_id**](RequestApi.md#get_request_by_request_id) | **GET** /request/{requestId} | Get MediaRequest
[**get_request_count**](RequestApi.md#get_request_count) | **GET** /request/count | Gets request counts
[**update_request**](RequestApi.md#update_request) | **PUT** /request/{requestId} | Update MediaRequest


# **create_request**
> MediaRequest create_request(create_request_request)

Create new request

Creates a new request with the provided media ID and type. The `REQUEST` permission is required.  If the user has the `ADMIN` or `AUTO_APPROVE` permissions, their request will be auomatically approved. 

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):

```python
import overseerr
from overseerr.models.create_request_request import CreateRequestRequest
from overseerr.models.media_request import MediaRequest
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
    api_instance = overseerr.RequestApi(api_client)
    create_request_request = overseerr.CreateRequestRequest() # CreateRequestRequest | 

    try:
        # Create new request
        api_response = api_instance.create_request(create_request_request)
        print("The response of RequestApi->create_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RequestApi->create_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_request_request** | [**CreateRequestRequest**](CreateRequestRequest.md)|  | 

### Return type

[**MediaRequest**](MediaRequest.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Succesfully created the request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_request_by_status**
> MediaRequest create_request_by_status(request_id, status)

Update a request's status

Updates a request's status to approved or declined. Also returns the request in a JSON object.  Requires the `MANAGE_REQUESTS` permission or `ADMIN`. 

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):

```python
import overseerr
from overseerr.models.media_request import MediaRequest
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
    api_instance = overseerr.RequestApi(api_client)
    request_id = '1' # str | Request ID
    status = 'status_example' # str | New status

    try:
        # Update a request's status
        api_response = api_instance.create_request_by_status(request_id, status)
        print("The response of RequestApi->create_request_by_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RequestApi->create_request_by_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **str**| Request ID | 
 **status** | **str**| New status | 

### Return type

[**MediaRequest**](MediaRequest.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Request status changed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_request_retry**
> MediaRequest create_request_retry(request_id)

Retry failed request

Retries a request by resending requests to Sonarr or Radarr.  Requires the `MANAGE_REQUESTS` permission or `ADMIN`. 

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):

```python
import overseerr
from overseerr.models.media_request import MediaRequest
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
    api_instance = overseerr.RequestApi(api_client)
    request_id = '1' # str | Request ID

    try:
        # Retry failed request
        api_response = api_instance.create_request_retry(request_id)
        print("The response of RequestApi->create_request_retry:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RequestApi->create_request_retry: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **str**| Request ID | 

### Return type

[**MediaRequest**](MediaRequest.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Retry triggered |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_request**
> delete_request(request_id)

Delete request

Removes a request. If the user has the `MANAGE_REQUESTS` permission, any request can be removed. Otherwise, only pending requests can be removed.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):

```python
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
    api_instance = overseerr.RequestApi(api_client)
    request_id = '1' # str | Request ID

    try:
        # Delete request
        api_instance.delete_request(request_id)
    except Exception as e:
        print("Exception when calling RequestApi->delete_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **str**| Request ID | 

### Return type

void (empty response body)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**204** | Succesfully removed request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_request**
> GetUserRequests2XXResponse get_request(take=take, skip=skip, filter=filter, sort=sort, requested_by=requested_by)

Get all requests

Returns all requests if the user has the `ADMIN` or `MANAGE_REQUESTS` permissions. Otherwise, only the logged-in user's requests are returned.  If the `requestedBy` parameter is specified, only requests from that particular user ID will be returned. 

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):

```python
import overseerr
from overseerr.models.get_user_requests2_xx_response import GetUserRequests2XXResponse
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
    api_instance = overseerr.RequestApi(api_client)
    take = 20 # float |  (optional)
    skip = 0 # float |  (optional)
    filter = 'filter_example' # str |  (optional)
    sort = added # str |  (optional) (default to added)
    requested_by = 1 # float |  (optional)

    try:
        # Get all requests
        api_response = api_instance.get_request(take=take, skip=skip, filter=filter, sort=sort, requested_by=requested_by)
        print("The response of RequestApi->get_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RequestApi->get_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **take** | **float**|  | [optional] 
 **skip** | **float**|  | [optional] 
 **filter** | **str**|  | [optional] 
 **sort** | **str**|  | [optional] [default to added]
 **requested_by** | **float**|  | [optional] 

### Return type

[**GetUserRequests2XXResponse**](GetUserRequests2XXResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Requests returned |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_request_by_request_id**
> MediaRequest get_request_by_request_id(request_id)

Get MediaRequest

Returns a specific MediaRequest in a JSON object.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):

```python
import overseerr
from overseerr.models.media_request import MediaRequest
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
    api_instance = overseerr.RequestApi(api_client)
    request_id = '1' # str | Request ID

    try:
        # Get MediaRequest
        api_response = api_instance.get_request_by_request_id(request_id)
        print("The response of RequestApi->get_request_by_request_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RequestApi->get_request_by_request_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **str**| Request ID | 

### Return type

[**MediaRequest**](MediaRequest.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Succesfully returns request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_request_count**
> GetRequestCount2XXResponse get_request_count()

Gets request counts

Returns the number of pending and approved requests. 

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):

```python
import overseerr
from overseerr.models.get_request_count2_xx_response import GetRequestCount2XXResponse
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
    api_instance = overseerr.RequestApi(api_client)

    try:
        # Gets request counts
        api_response = api_instance.get_request_count()
        print("The response of RequestApi->get_request_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RequestApi->get_request_count: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetRequestCount2XXResponse**](GetRequestCount2XXResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Request counts returned |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_request**
> MediaRequest update_request(request_id, update_request_request)

Update MediaRequest

Updates a specific media request and returns the request in a JSON object. Requires the `MANAGE_REQUESTS` permission.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):

```python
import overseerr
from overseerr.models.media_request import MediaRequest
from overseerr.models.update_request_request import UpdateRequestRequest
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
    api_instance = overseerr.RequestApi(api_client)
    request_id = '1' # str | Request ID
    update_request_request = overseerr.UpdateRequestRequest() # UpdateRequestRequest | 

    try:
        # Update MediaRequest
        api_response = api_instance.update_request(request_id, update_request_request)
        print("The response of RequestApi->update_request:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RequestApi->update_request: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_id** | **str**| Request ID | 
 **update_request_request** | [**UpdateRequestRequest**](UpdateRequestRequest.md)|  | 

### Return type

[**MediaRequest**](MediaRequest.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Succesfully updated request |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

