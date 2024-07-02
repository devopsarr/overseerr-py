# overseerr.MediaApi

All URIs are relative to *http://localhost:5055/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_media_by_status**](MediaApi.md#create_media_by_status) | **POST** /media/{mediaId}/{status} | Update media status
[**delete_media**](MediaApi.md#delete_media) | **DELETE** /media/{mediaId} | Delete media item
[**get_media**](MediaApi.md#get_media) | **GET** /media | Get media
[**get_media_watch_data**](MediaApi.md#get_media_watch_data) | **GET** /media/{mediaId}/watch_data | Get watch data


# **create_media_by_status**
> MediaInfo create_media_by_status(media_id, status, create_media_by_status_request=create_media_by_status_request)

Update media status

Updates a media item's status and returns the media in JSON format

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):

```python
import overseerr
from overseerr.models.create_media_by_status_request import CreateMediaByStatusRequest
from overseerr.models.media_info import MediaInfo
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
    api_instance = overseerr.MediaApi(api_client)
    media_id = '1' # str | Media ID
    status = 'available' # str | New status
    create_media_by_status_request = overseerr.CreateMediaByStatusRequest() # CreateMediaByStatusRequest |  (optional)

    try:
        # Update media status
        api_response = api_instance.create_media_by_status(media_id, status, create_media_by_status_request=create_media_by_status_request)
        print("The response of MediaApi->create_media_by_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaApi->create_media_by_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **media_id** | **str**| Media ID | 
 **status** | **str**| New status | 
 **create_media_by_status_request** | [**CreateMediaByStatusRequest**](CreateMediaByStatusRequest.md)|  | [optional] 

### Return type

[**MediaInfo**](MediaInfo.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returned media |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_media**
> delete_media(media_id)

Delete media item

Removes a media item. The `MANAGE_REQUESTS` permission is required to perform this action.

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
    api_instance = overseerr.MediaApi(api_client)
    media_id = '1' # str | Media ID

    try:
        # Delete media item
        api_instance.delete_media(media_id)
    except Exception as e:
        print("Exception when calling MediaApi->delete_media: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **media_id** | **str**| Media ID | 

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
**204** | Succesfully removed media item |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_media**
> GetMedia2XXResponse get_media(take=take, skip=skip, filter=filter, sort=sort)

Get media

Returns all media (can be filtered and limited) in a JSON object.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):

```python
import overseerr
from overseerr.models.get_media2_xx_response import GetMedia2XXResponse
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
    api_instance = overseerr.MediaApi(api_client)
    take = 20 # float |  (optional)
    skip = 0 # float |  (optional)
    filter = 'filter_example' # str |  (optional)
    sort = added # str |  (optional) (default to added)

    try:
        # Get media
        api_response = api_instance.get_media(take=take, skip=skip, filter=filter, sort=sort)
        print("The response of MediaApi->get_media:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaApi->get_media: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **take** | **float**|  | [optional] 
 **skip** | **float**|  | [optional] 
 **filter** | **str**|  | [optional] 
 **sort** | **str**|  | [optional] [default to added]

### Return type

[**GetMedia2XXResponse**](GetMedia2XXResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returned media |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_media_watch_data**
> GetMediaWatchData2XXResponse get_media_watch_data(media_id)

Get watch data

Returns play count, play duration, and users who have watched the media.  Requires the `ADMIN` permission. 

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):

```python
import overseerr
from overseerr.models.get_media_watch_data2_xx_response import GetMediaWatchData2XXResponse
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
    api_instance = overseerr.MediaApi(api_client)
    media_id = '1' # str | Media ID

    try:
        # Get watch data
        api_response = api_instance.get_media_watch_data(media_id)
        print("The response of MediaApi->get_media_watch_data:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MediaApi->get_media_watch_data: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **media_id** | **str**| Media ID | 

### Return type

[**GetMediaWatchData2XXResponse**](GetMediaWatchData2XXResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Users |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

