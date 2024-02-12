# overseerr.PublicApi

All URIs are relative to *http://localhost:5055/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_status**](PublicApi.md#get_status) | **GET** /status | Get Overseerr status
[**get_status_appdata**](PublicApi.md#get_status_appdata) | **GET** /status/appdata | Get application data volume status


# **get_status**
> GetStatus2XXResponse get_status()

Get Overseerr status

Returns the current Overseerr status in a JSON object.

### Example


```python
import overseerr
from overseerr.models.get_status2_xx_response import GetStatus2XXResponse
from overseerr.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:5055/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = overseerr.Configuration(
    host = "http://localhost:5055/api/v1"
)


# Enter a context with an instance of the API client
with overseerr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = overseerr.PublicApi(api_client)

    try:
        # Get Overseerr status
        api_response = api_instance.get_status()
        print("The response of PublicApi->get_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->get_status: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetStatus2XXResponse**](GetStatus2XXResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Returned status |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_status_appdata**
> GetStatusAppdata2XXResponse get_status_appdata()

Get application data volume status

For Docker installs, returns whether or not the volume mount was configured properly. Always returns true for non-Docker installs.

### Example


```python
import overseerr
from overseerr.models.get_status_appdata2_xx_response import GetStatusAppdata2XXResponse
from overseerr.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost:5055/api/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = overseerr.Configuration(
    host = "http://localhost:5055/api/v1"
)


# Enter a context with an instance of the API client
with overseerr.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = overseerr.PublicApi(api_client)

    try:
        # Get application data volume status
        api_response = api_instance.get_status_appdata()
        print("The response of PublicApi->get_status_appdata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling PublicApi->get_status_appdata: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetStatusAppdata2XXResponse**](GetStatusAppdata2XXResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Application data volume status and path |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

