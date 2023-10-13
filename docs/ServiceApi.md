# overseerr.ServiceApi

All URIs are relative to *http://localhost:5055/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_service_radarr_by_radarr_id**](ServiceApi.md#get_service_radarr_by_radarr_id) | **GET** /service/radarr/{radarrId} | Get Radarr server quality profiles and root folders
[**get_service_sonarr_by_sonarr_id**](ServiceApi.md#get_service_sonarr_by_sonarr_id) | **GET** /service/sonarr/{sonarrId} | Get Sonarr server quality profiles and root folders
[**list_service_radarr**](ServiceApi.md#list_service_radarr) | **GET** /service/radarr | Get non-sensitive Radarr server list
[**list_service_sonarr**](ServiceApi.md#list_service_sonarr) | **GET** /service/sonarr | Get non-sensitive Sonarr server list
[**list_service_sonarr_lookup_by_tmdb_id**](ServiceApi.md#list_service_sonarr_lookup_by_tmdb_id) | **GET** /service/sonarr/lookup/{tmdbId} | Get series from Sonarr


# **get_service_radarr_by_radarr_id**
> GetServiceRadarrByRadarrId200Response get_service_radarr_by_radarr_id(radarr_id)

Get Radarr server quality profiles and root folders

Returns a Radarr server's quality profile and root folder details in a JSON object.

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
    api_instance = overseerr.ServiceApi(api_client)
    radarr_id = 0 # float | 

    try:
        # Get Radarr server quality profiles and root folders
        api_response = api_instance.get_service_radarr_by_radarr_id(radarr_id)
        print("The response of ServiceApi->get_service_radarr_by_radarr_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceApi->get_service_radarr_by_radarr_id: %s\n" % e)
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
    api_instance = overseerr.ServiceApi(api_client)
    radarr_id = 0 # float | 

    try:
        # Get Radarr server quality profiles and root folders
        api_response = api_instance.get_service_radarr_by_radarr_id(radarr_id)
        print("The response of ServiceApi->get_service_radarr_by_radarr_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceApi->get_service_radarr_by_radarr_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **radarr_id** | **float**|  | 

### Return type

[**GetServiceRadarrByRadarrId200Response**](GetServiceRadarrByRadarrId200Response.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_service_sonarr_by_sonarr_id**
> GetServiceSonarrBySonarrId200Response get_service_sonarr_by_sonarr_id(sonarr_id)

Get Sonarr server quality profiles and root folders

Returns a Sonarr server's quality profile and root folder details in a JSON object.

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
    api_instance = overseerr.ServiceApi(api_client)
    sonarr_id = 0 # float | 

    try:
        # Get Sonarr server quality profiles and root folders
        api_response = api_instance.get_service_sonarr_by_sonarr_id(sonarr_id)
        print("The response of ServiceApi->get_service_sonarr_by_sonarr_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceApi->get_service_sonarr_by_sonarr_id: %s\n" % e)
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
    api_instance = overseerr.ServiceApi(api_client)
    sonarr_id = 0 # float | 

    try:
        # Get Sonarr server quality profiles and root folders
        api_response = api_instance.get_service_sonarr_by_sonarr_id(sonarr_id)
        print("The response of ServiceApi->get_service_sonarr_by_sonarr_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceApi->get_service_sonarr_by_sonarr_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **sonarr_id** | **float**|  | 

### Return type

[**GetServiceSonarrBySonarrId200Response**](GetServiceSonarrBySonarrId200Response.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_service_radarr**
> List[RadarrSettings] list_service_radarr()

Get non-sensitive Radarr server list

Returns a list of Radarr server IDs and names in a JSON object.

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
    api_instance = overseerr.ServiceApi(api_client)

    try:
        # Get non-sensitive Radarr server list
        api_response = api_instance.list_service_radarr()
        print("The response of ServiceApi->list_service_radarr:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceApi->list_service_radarr: %s\n" % e)
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
    api_instance = overseerr.ServiceApi(api_client)

    try:
        # Get non-sensitive Radarr server list
        api_response = api_instance.list_service_radarr()
        print("The response of ServiceApi->list_service_radarr:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceApi->list_service_radarr: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List[RadarrSettings]**](RadarrSettings.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_service_sonarr**
> List[SonarrSettings] list_service_sonarr()

Get non-sensitive Sonarr server list

Returns a list of Sonarr server IDs and names in a JSON object.

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
    api_instance = overseerr.ServiceApi(api_client)

    try:
        # Get non-sensitive Sonarr server list
        api_response = api_instance.list_service_sonarr()
        print("The response of ServiceApi->list_service_sonarr:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceApi->list_service_sonarr: %s\n" % e)
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
    api_instance = overseerr.ServiceApi(api_client)

    try:
        # Get non-sensitive Sonarr server list
        api_response = api_instance.list_service_sonarr()
        print("The response of ServiceApi->list_service_sonarr:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceApi->list_service_sonarr: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**List[SonarrSettings]**](SonarrSettings.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_service_sonarr_lookup_by_tmdb_id**
> List[SonarrSeries] list_service_sonarr_lookup_by_tmdb_id(tmdb_id)

Get series from Sonarr

Returns a list of series returned by searching for the name in Sonarr.

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
    api_instance = overseerr.ServiceApi(api_client)
    tmdb_id = 0 # float | 

    try:
        # Get series from Sonarr
        api_response = api_instance.list_service_sonarr_lookup_by_tmdb_id(tmdb_id)
        print("The response of ServiceApi->list_service_sonarr_lookup_by_tmdb_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceApi->list_service_sonarr_lookup_by_tmdb_id: %s\n" % e)
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
    api_instance = overseerr.ServiceApi(api_client)
    tmdb_id = 0 # float | 

    try:
        # Get series from Sonarr
        api_response = api_instance.list_service_sonarr_lookup_by_tmdb_id(tmdb_id)
        print("The response of ServiceApi->list_service_sonarr_lookup_by_tmdb_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServiceApi->list_service_sonarr_lookup_by_tmdb_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tmdb_id** | **float**|  | 

### Return type

[**List[SonarrSeries]**](SonarrSeries.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Request successful |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

