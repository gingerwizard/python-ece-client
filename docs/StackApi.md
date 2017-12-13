# swagger_client.StackApi

All URIs are relative to *http://localhost/api/v1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_version_stack**](StackApi.md#delete_version_stack) | **DELETE** /stack/versions/{version} | Mark an Elastic Stack version for deletion
[**get_version_stack**](StackApi.md#get_version_stack) | **GET** /stack/versions/{version} | Get an Elastic Stack version
[**get_version_stacks**](StackApi.md#get_version_stacks) | **GET** /stack/versions | Get all available Elastic Stack versions
[**update_stack_packs**](StackApi.md#update_stack_packs) | **POST** /stack/versions | Submit Elastic Stack packs
[**update_version_stack**](StackApi.md#update_version_stack) | **PUT** /stack/versions/{version} | Update an Elastic Stack version


# **delete_version_stack**
> EmptyResponse delete_version_stack(version)

Mark an Elastic Stack version for deletion

Sets a flag 'deleted' that effectively only removes the Elastic Stack Version from the list of available versions. The version can be restored later by sending an update request for the version (See PUT request)

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: basicAuth
swagger_client.configuration.username = 'YOUR_USERNAME'
swagger_client.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.StackApi()
version = 'version_example' # str | An Elastic Stack version

try: 
    # Mark an Elastic Stack version for deletion
    api_response = api_instance.delete_version_stack(version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StackApi->delete_version_stack: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| An Elastic Stack version | 

### Return type

[**EmptyResponse**](EmptyResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_version_stack**
> StackVersionConfig get_version_stack(version)

Get an Elastic Stack version

Retrieves a single Elastic Stack version with template.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: basicAuth
swagger_client.configuration.username = 'YOUR_USERNAME'
swagger_client.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.StackApi()
version = 'version_example' # str | An Elastic Stack version

try: 
    # Get an Elastic Stack version
    api_response = api_instance.get_version_stack(version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StackApi->get_version_stack: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| An Elastic Stack version | 

### Return type

[**StackVersionConfig**](StackVersionConfig.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_version_stacks**
> StackVersionConfigs get_version_stacks(show_deleted=show_deleted)

Get all available Elastic Stack versions

By default it returns only available versions. Use parameter `show_deleted` to get all versions

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: basicAuth
swagger_client.configuration.username = 'YOUR_USERNAME'
swagger_client.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.StackApi()
show_deleted = true # bool | Whether to show deleted stack versions or not (optional)

try: 
    # Get all available Elastic Stack versions
    api_response = api_instance.get_version_stacks(show_deleted=show_deleted)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StackApi->get_version_stacks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **show_deleted** | **bool**| Whether to show deleted stack versions or not | [optional] 

### Return type

[**StackVersionConfigs**](StackVersionConfigs.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_stack_packs**
> StackVersionArchiveProcessingResult update_stack_packs(file)

Submit Elastic Stack packs

Adds a new or updates existing Elastic Stack version and its template. Besides `multipart/form-data` requests, the endpoint supports `application/zip` and `application/octet-stream` requests with a binary body. Maximum size of the payload is 1Mb. If the archive contains a stack configuration that is already available through the API, then the existing configuration and its template will be overwritten.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: basicAuth
swagger_client.configuration.username = 'YOUR_USERNAME'
swagger_client.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.StackApi()
file = '/path/to/file.txt' # file | Zip file that contains one or multiple stack configurations

try: 
    # Submit Elastic Stack packs
    api_response = api_instance.update_stack_packs(file)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StackApi->update_stack_packs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | **file**| Zip file that contains one or multiple stack configurations | 

### Return type

[**StackVersionArchiveProcessingResult**](StackVersionArchiveProcessingResult.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_version_stack**
> StackVersionConfig update_version_stack(version, stack_config)

Update an Elastic Stack version

Updates the configuration of an existing Elastic Stack version.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: basicAuth
swagger_client.configuration.username = 'YOUR_USERNAME'
swagger_client.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.StackApi()
version = 'version_example' # str | An Elastic Stack version
stack_config = swagger_client.StackVersionConfigPost() # StackVersionConfigPost | Elastic Stack configuration object

try: 
    # Update an Elastic Stack version
    api_response = api_instance.update_version_stack(version, stack_config)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling StackApi->update_version_stack: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **version** | **str**| An Elastic Stack version | 
 **stack_config** | [**StackVersionConfigPost**](StackVersionConfigPost.md)| Elastic Stack configuration object | 

### Return type

[**StackVersionConfig**](StackVersionConfig.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

