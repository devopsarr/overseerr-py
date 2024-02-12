# overseerr.SearchApi

All URIs are relative to *http://localhost:5055/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_discover_keyword_movies**](SearchApi.md#get_discover_keyword_movies) | **GET** /discover/keyword/{keywordId}/movies | Get movies from keyword
[**get_discover_movies**](SearchApi.md#get_discover_movies) | **GET** /discover/movies | Discover movies
[**get_discover_movies_genre_by_genre_id**](SearchApi.md#get_discover_movies_genre_by_genre_id) | **GET** /discover/movies/genre/{genreId} | Discover movies by genre
[**get_discover_movies_language_by_language**](SearchApi.md#get_discover_movies_language_by_language) | **GET** /discover/movies/language/{language} | Discover movies by original language
[**get_discover_movies_studio_by_studio_id**](SearchApi.md#get_discover_movies_studio_by_studio_id) | **GET** /discover/movies/studio/{studioId} | Discover movies by studio
[**get_discover_movies_upcoming**](SearchApi.md#get_discover_movies_upcoming) | **GET** /discover/movies/upcoming | Upcoming movies
[**get_discover_trending**](SearchApi.md#get_discover_trending) | **GET** /discover/trending | Trending movies and TV
[**get_discover_tv**](SearchApi.md#get_discover_tv) | **GET** /discover/tv | Discover TV shows
[**get_discover_tv_genre_by_genre_id**](SearchApi.md#get_discover_tv_genre_by_genre_id) | **GET** /discover/tv/genre/{genreId} | Discover TV shows by genre
[**get_discover_tv_language_by_language**](SearchApi.md#get_discover_tv_language_by_language) | **GET** /discover/tv/language/{language} | Discover TV shows by original language
[**get_discover_tv_network_by_network_id**](SearchApi.md#get_discover_tv_network_by_network_id) | **GET** /discover/tv/network/{networkId} | Discover TV shows by network
[**get_discover_tv_upcoming**](SearchApi.md#get_discover_tv_upcoming) | **GET** /discover/tv/upcoming | Discover Upcoming TV shows
[**get_discover_watchlist**](SearchApi.md#get_discover_watchlist) | **GET** /discover/watchlist | Get the Plex watchlist.
[**get_search**](SearchApi.md#get_search) | **GET** /search | Search for movies, TV shows, or people
[**get_search_company**](SearchApi.md#get_search_company) | **GET** /search/company | Search for companies
[**get_search_keyword**](SearchApi.md#get_search_keyword) | **GET** /search/keyword | Search for keywords
[**list_discover_genreslider_movie**](SearchApi.md#list_discover_genreslider_movie) | **GET** /discover/genreslider/movie | Get genre slider data for movies
[**list_discover_genreslider_tv**](SearchApi.md#list_discover_genreslider_tv) | **GET** /discover/genreslider/tv | Get genre slider data for TV series


# **get_discover_keyword_movies**
> GetDiscoverMovies2XXResponse get_discover_keyword_movies(keyword_id, page=page, language=language)

Get movies from keyword

Returns list of movies based on the provided keyword ID a JSON object.

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
    api_instance = overseerr.SearchApi(api_client)
    keyword_id = 207317 # float | 
    page = 1 # float |  (optional) (default to 1)
    language = 'en' # str |  (optional)

    try:
        # Get movies from keyword
        api_response = api_instance.get_discover_keyword_movies(keyword_id, page=page, language=language)
        print("The response of SearchApi->get_discover_keyword_movies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->get_discover_keyword_movies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **keyword_id** | **float**|  | 
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

# **get_discover_movies**
> GetDiscoverMovies2XXResponse get_discover_movies(page=page, language=language, genre=genre, studio=studio, keywords=keywords, sort_by=sort_by, primary_release_date_gte=primary_release_date_gte, primary_release_date_lte=primary_release_date_lte, with_runtime_gte=with_runtime_gte, with_runtime_lte=with_runtime_lte, vote_average_gte=vote_average_gte, vote_average_lte=vote_average_lte, vote_count_gte=vote_count_gte, vote_count_lte=vote_count_lte, watch_region=watch_region, watch_providers=watch_providers)

Discover movies

Returns a list of movies in a JSON object.

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
    api_instance = overseerr.SearchApi(api_client)
    page = 1 # float |  (optional) (default to 1)
    language = 'en' # str |  (optional)
    genre = '18' # str |  (optional)
    studio = 1 # float |  (optional)
    keywords = '1,2' # str |  (optional)
    sort_by = 'popularity.desc' # str |  (optional)
    primary_release_date_gte = '2022-01-01T00:00:00Z' # str |  (optional)
    primary_release_date_lte = '2023-01-01T00:00:00Z' # str |  (optional)
    with_runtime_gte = 60 # float |  (optional)
    with_runtime_lte = 120 # float |  (optional)
    vote_average_gte = 7 # float |  (optional)
    vote_average_lte = 10 # float |  (optional)
    vote_count_gte = 7 # float |  (optional)
    vote_count_lte = 10 # float |  (optional)
    watch_region = 'US' # str |  (optional)
    watch_providers = '8|9' # str |  (optional)

    try:
        # Discover movies
        api_response = api_instance.get_discover_movies(page=page, language=language, genre=genre, studio=studio, keywords=keywords, sort_by=sort_by, primary_release_date_gte=primary_release_date_gte, primary_release_date_lte=primary_release_date_lte, with_runtime_gte=with_runtime_gte, with_runtime_lte=with_runtime_lte, vote_average_gte=vote_average_gte, vote_average_lte=vote_average_lte, vote_count_gte=vote_count_gte, vote_count_lte=vote_count_lte, watch_region=watch_region, watch_providers=watch_providers)
        print("The response of SearchApi->get_discover_movies:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->get_discover_movies: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **float**|  | [optional] [default to 1]
 **language** | **str**|  | [optional] 
 **genre** | **str**|  | [optional] 
 **studio** | **float**|  | [optional] 
 **keywords** | **str**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **primary_release_date_gte** | **str**|  | [optional] 
 **primary_release_date_lte** | **str**|  | [optional] 
 **with_runtime_gte** | **float**|  | [optional] 
 **with_runtime_lte** | **float**|  | [optional] 
 **vote_average_gte** | **float**|  | [optional] 
 **vote_average_lte** | **float**|  | [optional] 
 **vote_count_gte** | **float**|  | [optional] 
 **vote_count_lte** | **float**|  | [optional] 
 **watch_region** | **str**|  | [optional] 
 **watch_providers** | **str**|  | [optional] 

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
**2XX** | Results |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_discover_movies_genre_by_genre_id**
> GetDiscoverMoviesGenreByGenreId2XXResponse get_discover_movies_genre_by_genre_id(genre_id, page=page, language=language)

Discover movies by genre

Returns a list of movies based on the provided genre ID in a JSON object.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):

```python
import overseerr
from overseerr.models.get_discover_movies_genre_by_genre_id2_xx_response import GetDiscoverMoviesGenreByGenreId2XXResponse
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
    api_instance = overseerr.SearchApi(api_client)
    genre_id = '1' # str | 
    page = 1 # float |  (optional) (default to 1)
    language = 'en' # str |  (optional)

    try:
        # Discover movies by genre
        api_response = api_instance.get_discover_movies_genre_by_genre_id(genre_id, page=page, language=language)
        print("The response of SearchApi->get_discover_movies_genre_by_genre_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->get_discover_movies_genre_by_genre_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **genre_id** | **str**|  | 
 **page** | **float**|  | [optional] [default to 1]
 **language** | **str**|  | [optional] 

### Return type

[**GetDiscoverMoviesGenreByGenreId2XXResponse**](GetDiscoverMoviesGenreByGenreId2XXResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Results |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_discover_movies_language_by_language**
> GetDiscoverMoviesLanguageByLanguage2XXResponse get_discover_movies_language_by_language(language, page=page, language2=language2)

Discover movies by original language

Returns a list of movies based on the provided ISO 639-1 language code in a JSON object.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):

```python
import overseerr
from overseerr.models.get_discover_movies_language_by_language2_xx_response import GetDiscoverMoviesLanguageByLanguage2XXResponse
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
    api_instance = overseerr.SearchApi(api_client)
    language = 'en' # str | 
    page = 1 # float |  (optional) (default to 1)
    language2 = 'en' # str |  (optional)

    try:
        # Discover movies by original language
        api_response = api_instance.get_discover_movies_language_by_language(language, page=page, language2=language2)
        print("The response of SearchApi->get_discover_movies_language_by_language:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->get_discover_movies_language_by_language: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**|  | 
 **page** | **float**|  | [optional] [default to 1]
 **language2** | **str**|  | [optional] 

### Return type

[**GetDiscoverMoviesLanguageByLanguage2XXResponse**](GetDiscoverMoviesLanguageByLanguage2XXResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Results |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_discover_movies_studio_by_studio_id**
> GetDiscoverMoviesStudioByStudioId2XXResponse get_discover_movies_studio_by_studio_id(studio_id, page=page, language=language)

Discover movies by studio

Returns a list of movies based on the provided studio ID in a JSON object.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):

```python
import overseerr
from overseerr.models.get_discover_movies_studio_by_studio_id2_xx_response import GetDiscoverMoviesStudioByStudioId2XXResponse
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
    api_instance = overseerr.SearchApi(api_client)
    studio_id = '1' # str | 
    page = 1 # float |  (optional) (default to 1)
    language = 'en' # str |  (optional)

    try:
        # Discover movies by studio
        api_response = api_instance.get_discover_movies_studio_by_studio_id(studio_id, page=page, language=language)
        print("The response of SearchApi->get_discover_movies_studio_by_studio_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->get_discover_movies_studio_by_studio_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **studio_id** | **str**|  | 
 **page** | **float**|  | [optional] [default to 1]
 **language** | **str**|  | [optional] 

### Return type

[**GetDiscoverMoviesStudioByStudioId2XXResponse**](GetDiscoverMoviesStudioByStudioId2XXResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Results |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_discover_movies_upcoming**
> GetDiscoverMovies2XXResponse get_discover_movies_upcoming(page=page, language=language)

Upcoming movies

Returns a list of movies in a JSON object.

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
    api_instance = overseerr.SearchApi(api_client)
    page = 1 # float |  (optional) (default to 1)
    language = 'en' # str |  (optional)

    try:
        # Upcoming movies
        api_response = api_instance.get_discover_movies_upcoming(page=page, language=language)
        print("The response of SearchApi->get_discover_movies_upcoming:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->get_discover_movies_upcoming: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
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
**2XX** | Results |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_discover_trending**
> GetSearch2XXResponse get_discover_trending(page=page, language=language)

Trending movies and TV

Returns a list of movies and TV shows in a JSON object.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):

```python
import overseerr
from overseerr.models.get_search2_xx_response import GetSearch2XXResponse
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
    api_instance = overseerr.SearchApi(api_client)
    page = 1 # float |  (optional) (default to 1)
    language = 'en' # str |  (optional)

    try:
        # Trending movies and TV
        api_response = api_instance.get_discover_trending(page=page, language=language)
        print("The response of SearchApi->get_discover_trending:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->get_discover_trending: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **float**|  | [optional] [default to 1]
 **language** | **str**|  | [optional] 

### Return type

[**GetSearch2XXResponse**](GetSearch2XXResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Results |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_discover_tv**
> GetDiscoverTv2XXResponse get_discover_tv(page=page, language=language, genre=genre, network=network, keywords=keywords, sort_by=sort_by, first_air_date_gte=first_air_date_gte, first_air_date_lte=first_air_date_lte, with_runtime_gte=with_runtime_gte, with_runtime_lte=with_runtime_lte, vote_average_gte=vote_average_gte, vote_average_lte=vote_average_lte, vote_count_gte=vote_count_gte, vote_count_lte=vote_count_lte, watch_region=watch_region, watch_providers=watch_providers)

Discover TV shows

Returns a list of TV shows in a JSON object.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):

```python
import overseerr
from overseerr.models.get_discover_tv2_xx_response import GetDiscoverTv2XXResponse
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
    api_instance = overseerr.SearchApi(api_client)
    page = 1 # float |  (optional) (default to 1)
    language = 'en' # str |  (optional)
    genre = '18' # str |  (optional)
    network = 1 # float |  (optional)
    keywords = '1,2' # str |  (optional)
    sort_by = 'popularity.desc' # str |  (optional)
    first_air_date_gte = '2022-01-01T00:00:00Z' # str |  (optional)
    first_air_date_lte = '2023-01-01T00:00:00Z' # str |  (optional)
    with_runtime_gte = 60 # float |  (optional)
    with_runtime_lte = 120 # float |  (optional)
    vote_average_gte = 7 # float |  (optional)
    vote_average_lte = 10 # float |  (optional)
    vote_count_gte = 7 # float |  (optional)
    vote_count_lte = 10 # float |  (optional)
    watch_region = 'US' # str |  (optional)
    watch_providers = '8|9' # str |  (optional)

    try:
        # Discover TV shows
        api_response = api_instance.get_discover_tv(page=page, language=language, genre=genre, network=network, keywords=keywords, sort_by=sort_by, first_air_date_gte=first_air_date_gte, first_air_date_lte=first_air_date_lte, with_runtime_gte=with_runtime_gte, with_runtime_lte=with_runtime_lte, vote_average_gte=vote_average_gte, vote_average_lte=vote_average_lte, vote_count_gte=vote_count_gte, vote_count_lte=vote_count_lte, watch_region=watch_region, watch_providers=watch_providers)
        print("The response of SearchApi->get_discover_tv:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->get_discover_tv: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **float**|  | [optional] [default to 1]
 **language** | **str**|  | [optional] 
 **genre** | **str**|  | [optional] 
 **network** | **float**|  | [optional] 
 **keywords** | **str**|  | [optional] 
 **sort_by** | **str**|  | [optional] 
 **first_air_date_gte** | **str**|  | [optional] 
 **first_air_date_lte** | **str**|  | [optional] 
 **with_runtime_gte** | **float**|  | [optional] 
 **with_runtime_lte** | **float**|  | [optional] 
 **vote_average_gte** | **float**|  | [optional] 
 **vote_average_lte** | **float**|  | [optional] 
 **vote_count_gte** | **float**|  | [optional] 
 **vote_count_lte** | **float**|  | [optional] 
 **watch_region** | **str**|  | [optional] 
 **watch_providers** | **str**|  | [optional] 

### Return type

[**GetDiscoverTv2XXResponse**](GetDiscoverTv2XXResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Results |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_discover_tv_genre_by_genre_id**
> GetDiscoverTvGenreByGenreId2XXResponse get_discover_tv_genre_by_genre_id(genre_id, page=page, language=language)

Discover TV shows by genre

Returns a list of TV shows based on the provided genre ID in a JSON object.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):

```python
import overseerr
from overseerr.models.get_discover_tv_genre_by_genre_id2_xx_response import GetDiscoverTvGenreByGenreId2XXResponse
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
    api_instance = overseerr.SearchApi(api_client)
    genre_id = '1' # str | 
    page = 1 # float |  (optional) (default to 1)
    language = 'en' # str |  (optional)

    try:
        # Discover TV shows by genre
        api_response = api_instance.get_discover_tv_genre_by_genre_id(genre_id, page=page, language=language)
        print("The response of SearchApi->get_discover_tv_genre_by_genre_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->get_discover_tv_genre_by_genre_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **genre_id** | **str**|  | 
 **page** | **float**|  | [optional] [default to 1]
 **language** | **str**|  | [optional] 

### Return type

[**GetDiscoverTvGenreByGenreId2XXResponse**](GetDiscoverTvGenreByGenreId2XXResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Results |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_discover_tv_language_by_language**
> GetDiscoverTvLanguageByLanguage2XXResponse get_discover_tv_language_by_language(language, page=page, language2=language2)

Discover TV shows by original language

Returns a list of TV shows based on the provided ISO 639-1 language code in a JSON object.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):

```python
import overseerr
from overseerr.models.get_discover_tv_language_by_language2_xx_response import GetDiscoverTvLanguageByLanguage2XXResponse
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
    api_instance = overseerr.SearchApi(api_client)
    language = 'en' # str | 
    page = 1 # float |  (optional) (default to 1)
    language2 = 'en' # str |  (optional)

    try:
        # Discover TV shows by original language
        api_response = api_instance.get_discover_tv_language_by_language(language, page=page, language2=language2)
        print("The response of SearchApi->get_discover_tv_language_by_language:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->get_discover_tv_language_by_language: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**|  | 
 **page** | **float**|  | [optional] [default to 1]
 **language2** | **str**|  | [optional] 

### Return type

[**GetDiscoverTvLanguageByLanguage2XXResponse**](GetDiscoverTvLanguageByLanguage2XXResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Results |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_discover_tv_network_by_network_id**
> GetDiscoverTvNetworkByNetworkId2XXResponse get_discover_tv_network_by_network_id(network_id, page=page, language=language)

Discover TV shows by network

Returns a list of TV shows based on the provided network ID in a JSON object.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):

```python
import overseerr
from overseerr.models.get_discover_tv_network_by_network_id2_xx_response import GetDiscoverTvNetworkByNetworkId2XXResponse
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
    api_instance = overseerr.SearchApi(api_client)
    network_id = '1' # str | 
    page = 1 # float |  (optional) (default to 1)
    language = 'en' # str |  (optional)

    try:
        # Discover TV shows by network
        api_response = api_instance.get_discover_tv_network_by_network_id(network_id, page=page, language=language)
        print("The response of SearchApi->get_discover_tv_network_by_network_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->get_discover_tv_network_by_network_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **network_id** | **str**|  | 
 **page** | **float**|  | [optional] [default to 1]
 **language** | **str**|  | [optional] 

### Return type

[**GetDiscoverTvNetworkByNetworkId2XXResponse**](GetDiscoverTvNetworkByNetworkId2XXResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Results |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_discover_tv_upcoming**
> GetDiscoverTv2XXResponse get_discover_tv_upcoming(page=page, language=language)

Discover Upcoming TV shows

Returns a list of upcoming TV shows in a JSON object.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):

```python
import overseerr
from overseerr.models.get_discover_tv2_xx_response import GetDiscoverTv2XXResponse
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
    api_instance = overseerr.SearchApi(api_client)
    page = 1 # float |  (optional) (default to 1)
    language = 'en' # str |  (optional)

    try:
        # Discover Upcoming TV shows
        api_response = api_instance.get_discover_tv_upcoming(page=page, language=language)
        print("The response of SearchApi->get_discover_tv_upcoming:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->get_discover_tv_upcoming: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **float**|  | [optional] [default to 1]
 **language** | **str**|  | [optional] 

### Return type

[**GetDiscoverTv2XXResponse**](GetDiscoverTv2XXResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Results |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_discover_watchlist**
> GetUserWatchlist2XXResponse get_discover_watchlist(page=page)

Get the Plex watchlist.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):

```python
import overseerr
from overseerr.models.get_user_watchlist2_xx_response import GetUserWatchlist2XXResponse
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
    api_instance = overseerr.SearchApi(api_client)
    page = 1 # float |  (optional) (default to 1)

    try:
        # Get the Plex watchlist.
        api_response = api_instance.get_discover_watchlist(page=page)
        print("The response of SearchApi->get_discover_watchlist:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->get_discover_watchlist: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **page** | **float**|  | [optional] [default to 1]

### Return type

[**GetUserWatchlist2XXResponse**](GetUserWatchlist2XXResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Watchlist data returned |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_search**
> GetSearch2XXResponse get_search(query, page=page, language=language)

Search for movies, TV shows, or people

Returns a list of movies, TV shows, or people a JSON object.

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):

```python
import overseerr
from overseerr.models.get_search2_xx_response import GetSearch2XXResponse
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
    api_instance = overseerr.SearchApi(api_client)
    query = 'Mulan' # str | 
    page = 1 # float |  (optional) (default to 1)
    language = 'en' # str |  (optional)

    try:
        # Search for movies, TV shows, or people
        api_response = api_instance.get_search(query, page=page, language=language)
        print("The response of SearchApi->get_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->get_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**|  | 
 **page** | **float**|  | [optional] [default to 1]
 **language** | **str**|  | [optional] 

### Return type

[**GetSearch2XXResponse**](GetSearch2XXResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Results |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_search_company**
> GetSearchCompany2XXResponse get_search_company(query, page=page)

Search for companies

Returns a list of TMDB companies matching the search query. (Will not return origin country)

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):

```python
import overseerr
from overseerr.models.get_search_company2_xx_response import GetSearchCompany2XXResponse
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
    api_instance = overseerr.SearchApi(api_client)
    query = 'Disney' # str | 
    page = 1 # float |  (optional) (default to 1)

    try:
        # Search for companies
        api_response = api_instance.get_search_company(query, page=page)
        print("The response of SearchApi->get_search_company:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->get_search_company: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**|  | 
 **page** | **float**|  | [optional] [default to 1]

### Return type

[**GetSearchCompany2XXResponse**](GetSearchCompany2XXResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Results |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_search_keyword**
> GetSearchKeyword2XXResponse get_search_keyword(query, page=page)

Search for keywords

Returns a list of TMDB keywords matching the search query

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):

```python
import overseerr
from overseerr.models.get_search_keyword2_xx_response import GetSearchKeyword2XXResponse
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
    api_instance = overseerr.SearchApi(api_client)
    query = 'christmas' # str | 
    page = 1 # float |  (optional) (default to 1)

    try:
        # Search for keywords
        api_response = api_instance.get_search_keyword(query, page=page)
        print("The response of SearchApi->get_search_keyword:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->get_search_keyword: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **query** | **str**|  | 
 **page** | **float**|  | [optional] [default to 1]

### Return type

[**GetSearchKeyword2XXResponse**](GetSearchKeyword2XXResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Results |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_discover_genreslider_movie**
> List[ListDiscoverGenresliderMovie2XXResponseInner] list_discover_genreslider_movie(language=language)

Get genre slider data for movies

Returns a list of genres with backdrops attached

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):

```python
import overseerr
from overseerr.models.list_discover_genreslider_movie2_xx_response_inner import ListDiscoverGenresliderMovie2XXResponseInner
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
    api_instance = overseerr.SearchApi(api_client)
    language = 'en' # str |  (optional)

    try:
        # Get genre slider data for movies
        api_response = api_instance.list_discover_genreslider_movie(language=language)
        print("The response of SearchApi->list_discover_genreslider_movie:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->list_discover_genreslider_movie: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**|  | [optional] 

### Return type

[**List[ListDiscoverGenresliderMovie2XXResponseInner]**](ListDiscoverGenresliderMovie2XXResponseInner.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Genre slider data returned |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_discover_genreslider_tv**
> List[ListDiscoverGenresliderMovie2XXResponseInner] list_discover_genreslider_tv(language=language)

Get genre slider data for TV series

Returns a list of genres with backdrops attached

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):

```python
import overseerr
from overseerr.models.list_discover_genreslider_movie2_xx_response_inner import ListDiscoverGenresliderMovie2XXResponseInner
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
    api_instance = overseerr.SearchApi(api_client)
    language = 'en' # str |  (optional)

    try:
        # Get genre slider data for TV series
        api_response = api_instance.list_discover_genreslider_tv(language=language)
        print("The response of SearchApi->list_discover_genreslider_tv:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SearchApi->list_discover_genreslider_tv: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **language** | **str**|  | [optional] 

### Return type

[**List[ListDiscoverGenresliderMovie2XXResponseInner]**](ListDiscoverGenresliderMovie2XXResponseInner.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Genre slider data returned |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

