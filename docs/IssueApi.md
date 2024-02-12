# overseerr.IssueApi

All URIs are relative to *http://localhost:5055/api/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_issue**](IssueApi.md#create_issue) | **POST** /issue | Create new issue
[**create_issue_by_status**](IssueApi.md#create_issue_by_status) | **POST** /issue/{issueId}/{status} | Update an issue&#39;s status
[**create_issue_comment**](IssueApi.md#create_issue_comment) | **POST** /issue/{issueId}/comment | Create a comment
[**delete_issue**](IssueApi.md#delete_issue) | **DELETE** /issue/{issueId} | Delete issue
[**delete_issue_comment**](IssueApi.md#delete_issue_comment) | **DELETE** /issueComment/{commentId} | Delete issue comment
[**get_issue**](IssueApi.md#get_issue) | **GET** /issue | Get all issues
[**get_issue_by_issue_id**](IssueApi.md#get_issue_by_issue_id) | **GET** /issue/{issueId} | Get issue
[**get_issue_comment_by_comment_id**](IssueApi.md#get_issue_comment_by_comment_id) | **GET** /issueComment/{commentId} | Get issue comment
[**get_issue_count**](IssueApi.md#get_issue_count) | **GET** /issue/count | Gets issue counts
[**update_issue_comment**](IssueApi.md#update_issue_comment) | **PUT** /issueComment/{commentId} | Update issue comment


# **create_issue**
> Issue create_issue(create_issue_request)

Create new issue

Creates a new issue 

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):

```python
import overseerr
from overseerr.models.create_issue_request import CreateIssueRequest
from overseerr.models.issue import Issue
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
    api_instance = overseerr.IssueApi(api_client)
    create_issue_request = overseerr.CreateIssueRequest() # CreateIssueRequest | 

    try:
        # Create new issue
        api_response = api_instance.create_issue(create_issue_request)
        print("The response of IssueApi->create_issue:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IssueApi->create_issue: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **create_issue_request** | [**CreateIssueRequest**](CreateIssueRequest.md)|  | 

### Return type

[**Issue**](Issue.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**201** | Succesfully created the issue |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_issue_by_status**
> Issue create_issue_by_status(issue_id, status)

Update an issue's status

Updates an issue's status to approved or declined. Also returns the issue in a JSON object.  Requires the `MANAGE_ISSUES` permission or `ADMIN`. 

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):

```python
import overseerr
from overseerr.models.issue import Issue
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
    api_instance = overseerr.IssueApi(api_client)
    issue_id = '1' # str | Issue ID
    status = 'status_example' # str | New status

    try:
        # Update an issue's status
        api_response = api_instance.create_issue_by_status(issue_id, status)
        print("The response of IssueApi->create_issue_by_status:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IssueApi->create_issue_by_status: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issue_id** | **str**| Issue ID | 
 **status** | **str**| New status | 

### Return type

[**Issue**](Issue.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Issue status changed |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_issue_comment**
> Issue create_issue_comment(issue_id, create_issue_comment_request)

Create a comment

Creates a comment and returns associated issue in JSON format. 

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):

```python
import overseerr
from overseerr.models.create_issue_comment_request import CreateIssueCommentRequest
from overseerr.models.issue import Issue
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
    api_instance = overseerr.IssueApi(api_client)
    issue_id = 1 # float | 
    create_issue_comment_request = overseerr.CreateIssueCommentRequest() # CreateIssueCommentRequest | 

    try:
        # Create a comment
        api_response = api_instance.create_issue_comment(issue_id, create_issue_comment_request)
        print("The response of IssueApi->create_issue_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IssueApi->create_issue_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issue_id** | **float**|  | 
 **create_issue_comment_request** | [**CreateIssueCommentRequest**](CreateIssueCommentRequest.md)|  | 

### Return type

[**Issue**](Issue.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Issue returned with new comment |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_issue**
> delete_issue(issue_id)

Delete issue

Removes an issue. If the user has the `MANAGE_ISSUES` permission, any issue can be removed. Otherwise, only a users own issues can be removed.

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
    api_instance = overseerr.IssueApi(api_client)
    issue_id = '1' # str | Issue ID

    try:
        # Delete issue
        api_instance.delete_issue(issue_id)
    except Exception as e:
        print("Exception when calling IssueApi->delete_issue: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issue_id** | **str**| Issue ID | 

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
**204** | Succesfully removed issue |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_issue_comment**
> delete_issue_comment(comment_id)

Delete issue comment

Deletes an issue comment. Only users with `MANAGE_ISSUES` or the user who created the comment can perform this action. 

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
    api_instance = overseerr.IssueApi(api_client)
    comment_id = '1' # str | Issue Comment ID

    try:
        # Delete issue comment
        api_instance.delete_issue_comment(comment_id)
    except Exception as e:
        print("Exception when calling IssueApi->delete_issue_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment_id** | **str**| Issue Comment ID | 

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
**204** | Succesfully removed issue comment |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_issue**
> GetIssue2XXResponse get_issue(take=take, skip=skip, sort=sort, filter=filter, requested_by=requested_by)

Get all issues

Returns a list of issues in JSON format. 

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):

```python
import overseerr
from overseerr.models.get_issue2_xx_response import GetIssue2XXResponse
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
    api_instance = overseerr.IssueApi(api_client)
    take = 20 # float |  (optional)
    skip = 0 # float |  (optional)
    sort = 'added' # str |  (optional) (default to 'added')
    filter = 'open' # str |  (optional) (default to 'open')
    requested_by = 1 # float |  (optional)

    try:
        # Get all issues
        api_response = api_instance.get_issue(take=take, skip=skip, sort=sort, filter=filter, requested_by=requested_by)
        print("The response of IssueApi->get_issue:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IssueApi->get_issue: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **take** | **float**|  | [optional] 
 **skip** | **float**|  | [optional] 
 **sort** | **str**|  | [optional] [default to &#39;added&#39;]
 **filter** | **str**|  | [optional] [default to &#39;open&#39;]
 **requested_by** | **float**|  | [optional] 

### Return type

[**GetIssue2XXResponse**](GetIssue2XXResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Issues returned |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_issue_by_issue_id**
> Issue get_issue_by_issue_id(issue_id)

Get issue

Returns a single issue in JSON format. 

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):

```python
import overseerr
from overseerr.models.issue import Issue
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
    api_instance = overseerr.IssueApi(api_client)
    issue_id = 1 # float | 

    try:
        # Get issue
        api_response = api_instance.get_issue_by_issue_id(issue_id)
        print("The response of IssueApi->get_issue_by_issue_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IssueApi->get_issue_by_issue_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **issue_id** | **float**|  | 

### Return type

[**Issue**](Issue.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Issues returned |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_issue_comment_by_comment_id**
> IssueComment get_issue_comment_by_comment_id(comment_id)

Get issue comment

Returns a single issue comment in JSON format. 

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):

```python
import overseerr
from overseerr.models.issue_comment import IssueComment
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
    api_instance = overseerr.IssueApi(api_client)
    comment_id = '1' # str | 

    try:
        # Get issue comment
        api_response = api_instance.get_issue_comment_by_comment_id(comment_id)
        print("The response of IssueApi->get_issue_comment_by_comment_id:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IssueApi->get_issue_comment_by_comment_id: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment_id** | **str**|  | 

### Return type

[**IssueComment**](IssueComment.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Comment returned |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_issue_count**
> GetIssueCount2XXResponse get_issue_count()

Gets issue counts

Returns the number of open and closed issues, as well as the number of issues of each type. 

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):

```python
import overseerr
from overseerr.models.get_issue_count2_xx_response import GetIssueCount2XXResponse
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
    api_instance = overseerr.IssueApi(api_client)

    try:
        # Gets issue counts
        api_response = api_instance.get_issue_count()
        print("The response of IssueApi->get_issue_count:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IssueApi->get_issue_count: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetIssueCount2XXResponse**](GetIssueCount2XXResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Issue counts returned |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_issue_comment**
> IssueComment update_issue_comment(comment_id, update_issue_comment_request)

Update issue comment

Updates and returns a single issue comment in JSON format. 

### Example

* Api Key Authentication (apiKey):
* Api Key Authentication (cookieAuth):

```python
import overseerr
from overseerr.models.issue_comment import IssueComment
from overseerr.models.update_issue_comment_request import UpdateIssueCommentRequest
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
    api_instance = overseerr.IssueApi(api_client)
    comment_id = '1' # str | 
    update_issue_comment_request = overseerr.UpdateIssueCommentRequest() # UpdateIssueCommentRequest | 

    try:
        # Update issue comment
        api_response = api_instance.update_issue_comment(comment_id, update_issue_comment_request)
        print("The response of IssueApi->update_issue_comment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IssueApi->update_issue_comment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comment_id** | **str**|  | 
 **update_issue_comment_request** | [**UpdateIssueCommentRequest**](UpdateIssueCommentRequest.md)|  | 

### Return type

[**IssueComment**](IssueComment.md)

### Authorization

[apiKey](../README.md#apiKey), [cookieAuth](../README.md#cookieAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**2XX** | Comment updated |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

