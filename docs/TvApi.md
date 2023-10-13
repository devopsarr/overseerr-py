# overseerr.TvApi

All URIs are relative to *http://localhost:5055/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_tv_by_tv_id**](TvApi.md#get_tv_by_tv_id) | **GET** /tv/{tvId} | Get TV details
[**get_tv_ratings**](TvApi.md#get_tv_ratings) | **GET** /tv/{tvId}/ratings | Get TV ratings
[**get_tv_recommendations**](TvApi.md#get_tv_recommendations) | **GET** /tv/{tvId}/recommendations | Get recommended TV series
[**get_tv_season_by_season_id**](TvApi.md#get_tv_season_by_season_id) | **GET** /tv/{tvId}/season/{seasonId} | Get season details and episode list
[**get_tv_similar**](TvApi.md#get_tv_similar) | **GET** /tv/{tvId}/similar | Get similar TV series


# **get_tv_by_tv_id**
> TvDetails get_tv_by_tv_id(tv_id, language=language)

Get TV details

Returns full TV details in a JSON object.

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
    api_instance = overseerr.TvApi(api_client)
    tv_id = 76479 # float | 
    language = 'en' # str |  (optional)

    try:
        # Get TV details
        api_response = api_instance.get_tv_by_tv_id(tv_id, language=language)
        print("The response of TvApi->get_tv_by_tv_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TvApi->get_tv_by_tv_id: %s\n" % e)
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
    api_instance = overseerr.TvApi(api_client)
    tv_id = 76479 # float | 
    language = 'en' # str |  (optional)

    try:
        # Get TV details
        api_response = api_instance.get_tv_by_tv_id(tv_id, language=language)
        print("The response of TvApi->get_tv_by_tv_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TvApi->get_tv_by_tv_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tv_id** | **float**|  | 
 **language** | **str**|  | [optional] 

### Return type

[**TvDetails**](TvDetails.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TV details |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tv_ratings**
> GetTvRatings200Response get_tv_ratings(tv_id)

Get TV ratings

Returns ratings based on provided tvId in a JSON object.

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
    api_instance = overseerr.TvApi(api_client)
    tv_id = 76479 # float | 

    try:
        # Get TV ratings
        api_response = api_instance.get_tv_ratings(tv_id)
        print("The response of TvApi->get_tv_ratings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TvApi->get_tv_ratings: %s\n" % e)
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
    api_instance = overseerr.TvApi(api_client)
    tv_id = 76479 # float | 

    try:
        # Get TV ratings
        api_response = api_instance.get_tv_ratings(tv_id)
        print("The response of TvApi->get_tv_ratings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TvApi->get_tv_ratings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tv_id** | **float**|  | 

### Return type

[**GetTvRatings200Response**](GetTvRatings200Response.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Ratings returned |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tv_recommendations**
> GetDiscoverTv200Response get_tv_recommendations(tv_id, page=page, language=language)

Get recommended TV series

Returns list of recommended TV series based on the provided tvId in a JSON object.

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
    api_instance = overseerr.TvApi(api_client)
    tv_id = 76479 # float | 
    page = 1 # float |  (optional) (default to 1)
    language = 'en' # str |  (optional)

    try:
        # Get recommended TV series
        api_response = api_instance.get_tv_recommendations(tv_id, page=page, language=language)
        print("The response of TvApi->get_tv_recommendations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TvApi->get_tv_recommendations: %s\n" % e)
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
    api_instance = overseerr.TvApi(api_client)
    tv_id = 76479 # float | 
    page = 1 # float |  (optional) (default to 1)
    language = 'en' # str |  (optional)

    try:
        # Get recommended TV series
        api_response = api_instance.get_tv_recommendations(tv_id, page=page, language=language)
        print("The response of TvApi->get_tv_recommendations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TvApi->get_tv_recommendations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tv_id** | **float**|  | 
 **page** | **float**|  | [optional] [default to 1]
 **language** | **str**|  | [optional] 

### Return type

[**GetDiscoverTv200Response**](GetDiscoverTv200Response.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of TV series |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tv_season_by_season_id**
> Season get_tv_season_by_season_id(tv_id, season_id, language=language)

Get season details and episode list

Returns season details with a list of episodes in a JSON object.

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
    api_instance = overseerr.TvApi(api_client)
    tv_id = 76479 # float | 
    season_id = 1 # float | 
    language = 'en' # str |  (optional)

    try:
        # Get season details and episode list
        api_response = api_instance.get_tv_season_by_season_id(tv_id, season_id, language=language)
        print("The response of TvApi->get_tv_season_by_season_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TvApi->get_tv_season_by_season_id: %s\n" % e)
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
    api_instance = overseerr.TvApi(api_client)
    tv_id = 76479 # float | 
    season_id = 1 # float | 
    language = 'en' # str |  (optional)

    try:
        # Get season details and episode list
        api_response = api_instance.get_tv_season_by_season_id(tv_id, season_id, language=language)
        print("The response of TvApi->get_tv_season_by_season_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TvApi->get_tv_season_by_season_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tv_id** | **float**|  | 
 **season_id** | **float**|  | 
 **language** | **str**|  | [optional] 

### Return type

[**Season**](Season.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | TV details |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tv_similar**
> GetDiscoverTv200Response get_tv_similar(tv_id, page=page, language=language)

Get similar TV series

Returns list of similar TV series based on the provided tvId in a JSON object.

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
    api_instance = overseerr.TvApi(api_client)
    tv_id = 76479 # float | 
    page = 1 # float |  (optional) (default to 1)
    language = 'en' # str |  (optional)

    try:
        # Get similar TV series
        api_response = api_instance.get_tv_similar(tv_id, page=page, language=language)
        print("The response of TvApi->get_tv_similar:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TvApi->get_tv_similar: %s\n" % e)
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
    api_instance = overseerr.TvApi(api_client)
    tv_id = 76479 # float | 
    page = 1 # float |  (optional) (default to 1)
    language = 'en' # str |  (optional)

    try:
        # Get similar TV series
        api_response = api_instance.get_tv_similar(tv_id, page=page, language=language)
        print("The response of TvApi->get_tv_similar:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TvApi->get_tv_similar: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **tv_id** | **float**|  | 
 **page** | **float**|  | [optional] [default to 1]
 **language** | **str**|  | [optional] 

### Return type

[**GetDiscoverTv200Response**](GetDiscoverTv200Response.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | List of TV series |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

