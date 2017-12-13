# swagger_client.PlatformInfrastructureApi

All URIs are relative to *http://localhost/api/v1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**delete_allocator**](PlatformInfrastructureApi.md#delete_allocator) | **DELETE** /platform/infrastructure/allocators/{allocator_id} | Delete allocator
[**delete_allocator_metadata_item**](PlatformInfrastructureApi.md#delete_allocator_metadata_item) | **DELETE** /platform/infrastructure/allocators/{allocator_id}/metadata/{key} | Delete allocator metadata item
[**get_allocator**](PlatformInfrastructureApi.md#get_allocator) | **GET** /platform/infrastructure/allocators/{allocator_id} | Get allocator
[**get_allocator_metadata**](PlatformInfrastructureApi.md#get_allocator_metadata) | **GET** /platform/infrastructure/allocators/{allocator_id}/metadata | Get allocator metadata
[**get_allocator_settings**](PlatformInfrastructureApi.md#get_allocator_settings) | **GET** /platform/infrastructure/allocators/{allocator_id}/settings | Get allocator settings
[**get_allocators**](PlatformInfrastructureApi.md#get_allocators) | **GET** /platform/infrastructure/allocators | Get allocators
[**move_clusters**](PlatformInfrastructureApi.md#move_clusters) | **POST** /platform/infrastructure/allocators/{allocator_id}/clusters/_move | Move clusters
[**move_clusters_by_type**](PlatformInfrastructureApi.md#move_clusters_by_type) | **POST** /platform/infrastructure/allocators/{allocator_id}/clusters/{cluster_type}/_move | Move clusters by type
[**search_allocators**](PlatformInfrastructureApi.md#search_allocators) | **POST** /platform/infrastructure/allocators/_search | Search allocators
[**set_allocator_metadata**](PlatformInfrastructureApi.md#set_allocator_metadata) | **PUT** /platform/infrastructure/allocators/{allocator_id}/metadata | Set allocator metadata
[**set_allocator_metadata_item**](PlatformInfrastructureApi.md#set_allocator_metadata_item) | **PUT** /platform/infrastructure/allocators/{allocator_id}/metadata/{key} | Set allocator metadata item
[**set_allocator_settings**](PlatformInfrastructureApi.md#set_allocator_settings) | **PUT** /platform/infrastructure/allocators/{allocator_id}/settings | Set allocator settings
[**update_allocator_settings**](PlatformInfrastructureApi.md#update_allocator_settings) | **PATCH** /platform/infrastructure/allocators/{allocator_id}/settings | Update allocator settings


# **delete_allocator**
> EmptyResponse delete_allocator(allocator_id, remove_instances=remove_instances)

Delete allocator

Deletes an allocator by id.

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
api_instance = swagger_client.PlatformInfrastructureApi()
allocator_id = 'allocator_id_example' # str | Identifier for the allocator
remove_instances = true # bool | Whether or not to also remove the instances on the allocator that's being deleted. (optional)

try: 
    # Delete allocator
    api_response = api_instance.delete_allocator(allocator_id, remove_instances=remove_instances)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformInfrastructureApi->delete_allocator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **allocator_id** | **str**| Identifier for the allocator | 
 **remove_instances** | **bool**| Whether or not to also remove the instances on the allocator that&#39;s being deleted. | [optional] 

### Return type

[**EmptyResponse**](EmptyResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_allocator_metadata_item**
> list[AllocatorMetadataItem] delete_allocator_metadata_item(allocator_id, key, version=version)

Delete allocator metadata item

Removes a single item from a given allocators metadata.

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
api_instance = swagger_client.PlatformInfrastructureApi()
allocator_id = 'allocator_id_example' # str | The identifier for the allocator.
key = 'key_example' # str | The key of the metadata item to remove.
version = 56 # int | If specified, checks for conflicts against the version of the metadata (returned in 'x-cloud-resource-version' of the GET request) (optional)

try: 
    # Delete allocator metadata item
    api_response = api_instance.delete_allocator_metadata_item(allocator_id, key, version=version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformInfrastructureApi->delete_allocator_metadata_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **allocator_id** | **str**| The identifier for the allocator. | 
 **key** | **str**| The key of the metadata item to remove. | 
 **version** | **int**| If specified, checks for conflicts against the version of the metadata (returned in &#39;x-cloud-resource-version&#39; of the GET request) | [optional] 

### Return type

[**list[AllocatorMetadataItem]**](AllocatorMetadataItem.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_allocator**
> AllocatorInfo get_allocator(allocator_id)

Get allocator

Retrieves an allocator by id.

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
api_instance = swagger_client.PlatformInfrastructureApi()
allocator_id = 'allocator_id_example' # str | Identifier for the allocator

try: 
    # Get allocator
    api_response = api_instance.get_allocator(allocator_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformInfrastructureApi->get_allocator: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **allocator_id** | **str**| Identifier for the allocator | 

### Return type

[**AllocatorInfo**](AllocatorInfo.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_allocator_metadata**
> list[AllocatorMetadataItem] get_allocator_metadata(allocator_id)

Get allocator metadata

Retrieves the metadata for a given allocator.

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
api_instance = swagger_client.PlatformInfrastructureApi()
allocator_id = 'allocator_id_example' # str | The identifier for the allocator.

try: 
    # Get allocator metadata
    api_response = api_instance.get_allocator_metadata(allocator_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformInfrastructureApi->get_allocator_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **allocator_id** | **str**| The identifier for the allocator. | 

### Return type

[**list[AllocatorMetadataItem]**](AllocatorMetadataItem.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_allocator_settings**
> AllocatorSettings get_allocator_settings(allocator_id)

Get allocator settings

Retrieves overridable settings for an allocator.

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
api_instance = swagger_client.PlatformInfrastructureApi()
allocator_id = 'allocator_id_example' # str | Identifier for the allocator

try: 
    # Get allocator settings
    api_response = api_instance.get_allocator_settings(allocator_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformInfrastructureApi->get_allocator_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **allocator_id** | **str**| Identifier for the allocator | 

### Return type

[**AllocatorSettings**](AllocatorSettings.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_allocators**
> AllocatorOverview get_allocators(q=q)

Get allocators

Retrieves an overview of all allocators in an ECE installation.

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
api_instance = swagger_client.PlatformInfrastructureApi()
q = 'q_example' # str | An optional query to filter allocators by. Maps to an Elasticsearch query_string query. (optional)

try: 
    # Get allocators
    api_response = api_instance.get_allocators(q=q)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformInfrastructureApi->get_allocators: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **q** | **str**| An optional query to filter allocators by. Maps to an Elasticsearch query_string query. | [optional] 

### Return type

[**AllocatorOverview**](AllocatorOverview.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_clusters**
> MoveClustersCommandResponse move_clusters(allocator_id, body=body, force_update=force_update, allocator_down=allocator_down, validate_only=validate_only)

Move clusters

Moves clusters off an allocator.

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
api_instance = swagger_client.PlatformInfrastructureApi()
allocator_id = 'allocator_id_example' # str | The identifier of the allocator of which to move clusters.
body = swagger_client.MoveClustersRequest() # MoveClustersRequest | Overrides defaults for the move of each cluster (optional)
force_update = false # bool | If true, will cancel any pending plans and overwrite with this move plan for all clusters, else will error (optional) (default to false)
allocator_down = false # bool | Tells the infrastructure that all instances on the allocator should be considered as permanently down when deciding how to migrate data to new nodes. If left blank then the system will auto-decide (currently: will treat the allocator as up) (optional) (default to false)
validate_only = false # bool | If true, will validate the plan overrides and return the plan that would be applied, without performing the move. (optional) (default to false)

try: 
    # Move clusters
    api_response = api_instance.move_clusters(allocator_id, body=body, force_update=force_update, allocator_down=allocator_down, validate_only=validate_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformInfrastructureApi->move_clusters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **allocator_id** | **str**| The identifier of the allocator of which to move clusters. | 
 **body** | [**MoveClustersRequest**](MoveClustersRequest.md)| Overrides defaults for the move of each cluster | [optional] 
 **force_update** | **bool**| If true, will cancel any pending plans and overwrite with this move plan for all clusters, else will error | [optional] [default to false]
 **allocator_down** | **bool**| Tells the infrastructure that all instances on the allocator should be considered as permanently down when deciding how to migrate data to new nodes. If left blank then the system will auto-decide (currently: will treat the allocator as up) | [optional] [default to false]
 **validate_only** | **bool**| If true, will validate the plan overrides and return the plan that would be applied, without performing the move. | [optional] [default to false]

### Return type

[**MoveClustersCommandResponse**](MoveClustersCommandResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_clusters_by_type**
> MoveClustersCommandResponse move_clusters_by_type(allocator_id, cluster_type, body=body, force_update=force_update, allocator_down=allocator_down, validate_only=validate_only)

Move clusters by type

Moves clusters of a given type off an allocator.

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
api_instance = swagger_client.PlatformInfrastructureApi()
allocator_id = 'allocator_id_example' # str | The identifier of the allocator of which to move clusters.
cluster_type = 'cluster_type_example' # str | The type of clusters to move off the allocator (either Elasticsearch or Kibana).  If not specified, then all clusters are moved.
body = swagger_client.MoveClustersRequest() # MoveClustersRequest | Overrides defaults for the move of each cluster (optional)
force_update = false # bool | If true, will cancel any pending plans and overwrite with this move plan for all clusters, else will error (optional) (default to false)
allocator_down = false # bool | If true all clusters on the allocator will be considered to be permanently down for the purposes of data migration logic (optional) (default to false)
validate_only = false # bool | If true, will validate the plan overrides and return the plan that would be applied, without performing the move. (optional) (default to false)

try: 
    # Move clusters by type
    api_response = api_instance.move_clusters_by_type(allocator_id, cluster_type, body=body, force_update=force_update, allocator_down=allocator_down, validate_only=validate_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformInfrastructureApi->move_clusters_by_type: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **allocator_id** | **str**| The identifier of the allocator of which to move clusters. | 
 **cluster_type** | **str**| The type of clusters to move off the allocator (either Elasticsearch or Kibana).  If not specified, then all clusters are moved. | 
 **body** | [**MoveClustersRequest**](MoveClustersRequest.md)| Overrides defaults for the move of each cluster | [optional] 
 **force_update** | **bool**| If true, will cancel any pending plans and overwrite with this move plan for all clusters, else will error | [optional] [default to false]
 **allocator_down** | **bool**| If true all clusters on the allocator will be considered to be permanently down for the purposes of data migration logic | [optional] [default to false]
 **validate_only** | **bool**| If true, will validate the plan overrides and return the plan that would be applied, without performing the move. | [optional] [default to false]

### Return type

[**MoveClustersCommandResponse**](MoveClustersCommandResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **search_allocators**
> AllocatorOverview search_allocators(body=body)

Search allocators

Retrieves allocators in an ECE installation that match a given query.

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
api_instance = swagger_client.PlatformInfrastructureApi()
body = swagger_client.SearchRequest() # SearchRequest | The optional search request to execute. If not supplied then all allocators are matched. (optional)

try: 
    # Search allocators
    api_response = api_instance.search_allocators(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformInfrastructureApi->search_allocators: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**SearchRequest**](SearchRequest.md)| The optional search request to execute. If not supplied then all allocators are matched. | [optional] 

### Return type

[**AllocatorOverview**](AllocatorOverview.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_allocator_metadata**
> list[AllocatorMetadataItem] set_allocator_metadata(body, allocator_id, version=version)

Set allocator metadata

Sets the metadata for a given allocator.

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
api_instance = swagger_client.PlatformInfrastructureApi()
body = swagger_client.AllocatorMetadataItems() # AllocatorMetadataItems | The metadata to update the allocator with.
allocator_id = 'allocator_id_example' # str | The identifier for the allocator.
version = 56 # int | If specified, checks for conflicts against the version of the metadata (returned in 'x-cloud-resource-version' of the GET request) (optional)

try: 
    # Set allocator metadata
    api_response = api_instance.set_allocator_metadata(body, allocator_id, version=version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformInfrastructureApi->set_allocator_metadata: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AllocatorMetadataItems**](AllocatorMetadataItems.md)| The metadata to update the allocator with. | 
 **allocator_id** | **str**| The identifier for the allocator. | 
 **version** | **int**| If specified, checks for conflicts against the version of the metadata (returned in &#39;x-cloud-resource-version&#39; of the GET request) | [optional] 

### Return type

[**list[AllocatorMetadataItem]**](AllocatorMetadataItem.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_allocator_metadata_item**
> list[AllocatorMetadataItem] set_allocator_metadata_item(allocator_id, key, body, version=version)

Set allocator metadata item

Adds or updates a single item to a given allocators metadata.

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
api_instance = swagger_client.PlatformInfrastructureApi()
allocator_id = 'allocator_id_example' # str | The identifier for the allocator.
key = 'key_example' # str | The key of the metadata item to add or update.
body = swagger_client.AllocatorMetadataItemValue() # AllocatorMetadataItemValue | The value of the metadata item to add or update.
version = 56 # int | If specified, checks for conflicts against the version of the metadata (returned in 'x-cloud-resource-version' of the GET request) (optional)

try: 
    # Set allocator metadata item
    api_response = api_instance.set_allocator_metadata_item(allocator_id, key, body, version=version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformInfrastructureApi->set_allocator_metadata_item: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **allocator_id** | **str**| The identifier for the allocator. | 
 **key** | **str**| The key of the metadata item to add or update. | 
 **body** | [**AllocatorMetadataItemValue**](AllocatorMetadataItemValue.md)| The value of the metadata item to add or update. | 
 **version** | **int**| If specified, checks for conflicts against the version of the metadata (returned in &#39;x-cloud-resource-version&#39; of the GET request) | [optional] 

### Return type

[**list[AllocatorMetadataItem]**](AllocatorMetadataItem.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_allocator_settings**
> AllocatorSettings set_allocator_settings(allocator_id, body, version=version)

Set allocator settings

Overwrites the entire settings for an allocator with the settings supplied, any fields not referenced here will be deleted.

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
api_instance = swagger_client.PlatformInfrastructureApi()
allocator_id = 'allocator_id_example' # str | Identifier for the allocator
body = swagger_client.AllocatorSettings() # AllocatorSettings | The allocator settings to apply.
version = 56 # int | If specified, checks for conflicts against the version of the settings (returned in 'x-cloud-resource-version' of the GET request) (optional)

try: 
    # Set allocator settings
    api_response = api_instance.set_allocator_settings(allocator_id, body, version=version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformInfrastructureApi->set_allocator_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **allocator_id** | **str**| Identifier for the allocator | 
 **body** | [**AllocatorSettings**](AllocatorSettings.md)| The allocator settings to apply. | 
 **version** | **int**| If specified, checks for conflicts against the version of the settings (returned in &#39;x-cloud-resource-version&#39; of the GET request) | [optional] 

### Return type

[**AllocatorSettings**](AllocatorSettings.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_allocator_settings**
> AllocatorSettings update_allocator_settings(allocator_id, body, version=version)

Update allocator settings

Applies the provided settings as a patch - fields not referenced in this update will not be altered.

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
api_instance = swagger_client.PlatformInfrastructureApi()
allocator_id = 'allocator_id_example' # str | Identifier for the allocator
body = swagger_client.AllocatorSettings() # AllocatorSettings | The allocator settings to update.
version = 56 # int | If specified, checks for conflicts against the version of the repository configuration (returned in 'x-cloud-resource-version' of the GET request) (optional)

try: 
    # Update allocator settings
    api_response = api_instance.update_allocator_settings(allocator_id, body, version=version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformInfrastructureApi->update_allocator_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **allocator_id** | **str**| Identifier for the allocator | 
 **body** | [**AllocatorSettings**](AllocatorSettings.md)| The allocator settings to update. | 
 **version** | **int**| If specified, checks for conflicts against the version of the repository configuration (returned in &#39;x-cloud-resource-version&#39; of the GET request) | [optional] 

### Return type

[**AllocatorSettings**](AllocatorSettings.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

