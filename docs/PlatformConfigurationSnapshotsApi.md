# swagger_client.PlatformConfigurationSnapshotsApi

All URIs are relative to *http://localhost/api/v1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_snapshot_repository**](PlatformConfigurationSnapshotsApi.md#delete_snapshot_repository) | **DELETE** /platform/configuration/snapshots/repositories/{repository_name} | Delete snapshot repository
[**get_snapshot_repositories**](PlatformConfigurationSnapshotsApi.md#get_snapshot_repositories) | **GET** /platform/configuration/snapshots/repositories | Get snapshot repositories
[**get_snapshot_repository**](PlatformConfigurationSnapshotsApi.md#get_snapshot_repository) | **GET** /platform/configuration/snapshots/repositories/{repository_name} | Get snapshot repository
[**set_snapshot_repository**](PlatformConfigurationSnapshotsApi.md#set_snapshot_repository) | **PUT** /platform/configuration/snapshots/repositories/{repository_name} | Set snapshot repository


# **delete_snapshot_repository**
> EmptyResponse delete_snapshot_repository(repository_name)

Delete snapshot repository

Deletes a snapshot repository configuration by name.

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
api_instance = swagger_client.PlatformConfigurationSnapshotsApi()
repository_name = 'repository_name_example' # str | Custom name of a snapshot repository configuration.

try: 
    # Delete snapshot repository
    api_response = api_instance.delete_snapshot_repository(repository_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformConfigurationSnapshotsApi->delete_snapshot_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**| Custom name of a snapshot repository configuration. | 

### Return type

[**EmptyResponse**](EmptyResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_snapshot_repositories**
> RepositoryConfigs get_snapshot_repositories()

Get snapshot repositories

Retrieves a list of all available snapshot repository configurations. Privileged access required for configuration contents.

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
api_instance = swagger_client.PlatformConfigurationSnapshotsApi()

try: 
    # Get snapshot repositories
    api_response = api_instance.get_snapshot_repositories()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformConfigurationSnapshotsApi->get_snapshot_repositories: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**RepositoryConfigs**](RepositoryConfigs.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_snapshot_repository**
> RepositoryConfig get_snapshot_repository(repository_name)

Get snapshot repository

Retrieve a repository configuration by name. Privileged access required for configuration contents.

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
api_instance = swagger_client.PlatformConfigurationSnapshotsApi()
repository_name = 'repository_name_example' # str | Custom name of a snapshot repository configuration.

try: 
    # Get snapshot repository
    api_response = api_instance.get_snapshot_repository(repository_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformConfigurationSnapshotsApi->get_snapshot_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**| Custom name of a snapshot repository configuration. | 

### Return type

[**RepositoryConfig**](RepositoryConfig.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_snapshot_repository**
> RepositoryConfig set_snapshot_repository(repository_name, body, version=version)

Set snapshot repository

Creates or updates an existing snapshot repository configuration by name.

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
api_instance = swagger_client.PlatformConfigurationSnapshotsApi()
repository_name = 'repository_name_example' # str | Custom name of a snapshot repository configuration.
body = swagger_client.SnapshotRepositoryConfiguration() # SnapshotRepositoryConfiguration | The Elasticsearch snapshot repository configuration.
version = 56 # int | If specified, checks for conflicts against the version of the repository configuration (returned in 'x-cloud-resource-version' of the GET request) (optional)

try: 
    # Set snapshot repository
    api_response = api_instance.set_snapshot_repository(repository_name, body, version=version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformConfigurationSnapshotsApi->set_snapshot_repository: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_name** | **str**| Custom name of a snapshot repository configuration. | 
 **body** | [**SnapshotRepositoryConfiguration**](SnapshotRepositoryConfiguration.md)| The Elasticsearch snapshot repository configuration. | 
 **version** | **int**| If specified, checks for conflicts against the version of the repository configuration (returned in &#39;x-cloud-resource-version&#39; of the GET request) | [optional] 

### Return type

[**RepositoryConfig**](RepositoryConfig.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

