# overseerr.CollectionApi

All URIs are relative to *http://localhost:5055/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_collection_by_collection_id**](CollectionApi.md#get_collection_by_collection_id) | **GET** /collection/{collectionId} | Get collection details


# **get_collection_by_collection_id**
> Collection get_collection_by_collection_id(collection_id, language=language)

Get collection details

Returns full collection details in a JSON object.

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
    api_instance = overseerr.CollectionApi(api_client)
    collection_id = 537982 # float | 
    language = 'en' # str |  (optional)

    try:
        # Get collection details
        api_response = api_instance.get_collection_by_collection_id(collection_id, language=language)
        print("The response of CollectionApi->get_collection_by_collection_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionApi->get_collection_by_collection_id: %s\n" % e)
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
    api_instance = overseerr.CollectionApi(api_client)
    collection_id = 537982 # float | 
    language = 'en' # str |  (optional)

    try:
        # Get collection details
        api_response = api_instance.get_collection_by_collection_id(collection_id, language=language)
        print("The response of CollectionApi->get_collection_by_collection_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionApi->get_collection_by_collection_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | **float**|  | 
 **language** | **str**|  | [optional] 

### Return type

[**Collection**](Collection.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details
| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Collection details |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

