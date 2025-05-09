# overseerr.MoviesApi

All URIs are relative to *http://localhost:5055/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_movie_by_movie_id**](MoviesApi.md#get_movie_by_movie_id) | **GET** /movie/{movieId} | Get movie details
[**get_movie_ratings**](MoviesApi.md#get_movie_ratings) | **GET** /movie/{movieId}/ratings | Get movie ratings
[**get_movie_ratingscombined**](MoviesApi.md#get_movie_ratingscombined) | **GET** /movie/{movieId}/ratingscombined | Get RT and IMDB movie ratings combined
[**get_movie_recommendations**](MoviesApi.md#get_movie_recommendations) | **GET** /movie/{movieId}/recommendations | Get recommended movies
[**get_movie_similar**](MoviesApi.md#get_movie_similar) | **GET** /movie/{movieId}/similar | Get similar movies


# **get_movie_by_movie_id**
> MovieDetails get_movie_by_movie_id(movie_id, language=language)

Get movie details

Returns full movie details in a JSON object.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):

```python
import overseerr
from overseerr.models.movie_details import MovieDetails
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
    api_instance = overseerr.MoviesApi(api_client)
    movie_id = 337401 # float | 
    language = 'en' # str |  (optional)

    try:
        # Get movie details
        api_response = api_instance.get_movie_by_movie_id(movie_id, language=language)
        print("The response of MoviesApi->get_movie_by_movie_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MoviesApi->get_movie_by_movie_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **movie_id** | **float**|  | 
 **language** | **str**|  | [optional] 

### Return type

[**MovieDetails**](MovieDetails.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Movie details |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_movie_ratings**
> GetMovieRatings2XXResponse get_movie_ratings(movie_id)

Get movie ratings

Returns ratings based on the provided movieId in a JSON object.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):

```python
import overseerr
from overseerr.models.get_movie_ratings2_xx_response import GetMovieRatings2XXResponse
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
    api_instance = overseerr.MoviesApi(api_client)
    movie_id = 337401 # float | 

    try:
        # Get movie ratings
        api_response = api_instance.get_movie_ratings(movie_id)
        print("The response of MoviesApi->get_movie_ratings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MoviesApi->get_movie_ratings: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **movie_id** | **float**|  | 

### Return type

[**GetMovieRatings2XXResponse**](GetMovieRatings2XXResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Ratings returned |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_movie_ratingscombined**
> GetMovieRatingscombined2XXResponse get_movie_ratingscombined(movie_id)

Get RT and IMDB movie ratings combined

Returns ratings from RottenTomatoes and IMDB based on the provided movieId in a JSON object.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):

```python
import overseerr
from overseerr.models.get_movie_ratingscombined2_xx_response import GetMovieRatingscombined2XXResponse
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
    api_instance = overseerr.MoviesApi(api_client)
    movie_id = 337401 # float | 

    try:
        # Get RT and IMDB movie ratings combined
        api_response = api_instance.get_movie_ratingscombined(movie_id)
        print("The response of MoviesApi->get_movie_ratingscombined:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MoviesApi->get_movie_ratingscombined: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **movie_id** | **float**|  | 

### Return type

[**GetMovieRatingscombined2XXResponse**](GetMovieRatingscombined2XXResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Ratings returned |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_movie_recommendations**
> GetDiscoverMovies2XXResponse get_movie_recommendations(movie_id, page=page, language=language)

Get recommended movies

Returns list of recommended movies based on provided movie ID in a JSON object.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):

```python
import overseerr
from overseerr.models.get_discover_movies2_xx_response import GetDiscoverMovies2XXResponse
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
    api_instance = overseerr.MoviesApi(api_client)
    movie_id = 337401 # float | 
    page = 1 # float |  (optional) (default to 1)
    language = 'en' # str |  (optional)

    try:
        # Get recommended movies
        api_response = api_instance.get_movie_recommendations(movie_id, page=page, language=language)
        print("The response of MoviesApi->get_movie_recommendations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MoviesApi->get_movie_recommendations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **movie_id** | **float**|  | 
 **page** | **float**|  | [optional] [default to 1]
 **language** | **str**|  | [optional] 

### Return type

[**GetDiscoverMovies2XXResponse**](GetDiscoverMovies2XXResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | List of movies |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_movie_similar**
> GetDiscoverMovies2XXResponse get_movie_similar(movie_id, page=page, language=language)

Get similar movies

Returns list of similar movies based on the provided movieId in a JSON object.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):

```python
import overseerr
from overseerr.models.get_discover_movies2_xx_response import GetDiscoverMovies2XXResponse
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
    api_instance = overseerr.MoviesApi(api_client)
    movie_id = 337401 # float | 
    page = 1 # float |  (optional) (default to 1)
    language = 'en' # str |  (optional)

    try:
        # Get similar movies
        api_response = api_instance.get_movie_similar(movie_id, page=page, language=language)
        print("The response of MoviesApi->get_movie_similar:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MoviesApi->get_movie_similar: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **movie_id** | **float**|  | 
 **page** | **float**|  | [optional] [default to 1]
 **language** | **str**|  | [optional] 

### Return type

[**GetDiscoverMovies2XXResponse**](GetDiscoverMovies2XXResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | List of movies |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

