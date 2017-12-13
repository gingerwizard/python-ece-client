# swagger_client.ClustersElasticsearchApi

All URIs are relative to *http://localhost/api/v1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_es_cluster_monitoring**](ClustersElasticsearchApi.md#cancel_es_cluster_monitoring) | **DELETE** /clusters/elasticsearch/{cluster_id}/monitoring | Cancel monitoring
[**cancel_es_cluster_pending_plan**](ClustersElasticsearchApi.md#cancel_es_cluster_pending_plan) | **DELETE** /clusters/elasticsearch/{cluster_id}/plan/pending | Cancel pending plan
[**create_es_cluster**](ClustersElasticsearchApi.md#create_es_cluster) | **POST** /clusters/elasticsearch | Create cluster
[**delete_es_cluster**](ClustersElasticsearchApi.md#delete_es_cluster) | **DELETE** /clusters/elasticsearch/{cluster_id} | Delete cluster
[**generate_es_cluster_diagnostics**](ClustersElasticsearchApi.md#generate_es_cluster_diagnostics) | **GET** /clusters/elasticsearch/{cluster_id}/support/_generate-diagnostics | Generate diagnostics
[**generate_es_cluster_logs**](ClustersElasticsearchApi.md#generate_es_cluster_logs) | **GET** /clusters/elasticsearch/{cluster_id}/support/_generate-logs | Generate logs
[**get_es_cluster**](ClustersElasticsearchApi.md#get_es_cluster) | **GET** /clusters/elasticsearch/{cluster_id} | Get cluster
[**get_es_cluster_metadata_raw**](ClustersElasticsearchApi.md#get_es_cluster_metadata_raw) | **GET** /clusters/elasticsearch/{cluster_id}/metadata/raw | Get cluster metadata in raw form
[**get_es_cluster_metadata_settings**](ClustersElasticsearchApi.md#get_es_cluster_metadata_settings) | **GET** /clusters/elasticsearch/{cluster_id}/metadata/settings | Get cluster metadata settings
[**get_es_cluster_pending_plan**](ClustersElasticsearchApi.md#get_es_cluster_pending_plan) | **GET** /clusters/elasticsearch/{cluster_id}/plan/pending | Get pending plan
[**get_es_cluster_plan**](ClustersElasticsearchApi.md#get_es_cluster_plan) | **GET** /clusters/elasticsearch/{cluster_id}/plan | Get plan
[**get_es_cluster_plan_activity**](ClustersElasticsearchApi.md#get_es_cluster_plan_activity) | **GET** /clusters/elasticsearch/{cluster_id}/plan/activity | Get plan activity
[**get_es_clusters**](ClustersElasticsearchApi.md#get_es_clusters) | **GET** /clusters/elasticsearch | Get clusters
[**move_es_cluster_instances**](ClustersElasticsearchApi.md#move_es_cluster_instances) | **POST** /clusters/elasticsearch/{cluster_id}/instances/{instance_ids}/_move | Move instances
[**move_es_cluster_instances_advanced**](ClustersElasticsearchApi.md#move_es_cluster_instances_advanced) | **POST** /clusters/elasticsearch/{cluster_id}/instances/_move | Move instances (advanced)
[**restart_es_cluster**](ClustersElasticsearchApi.md#restart_es_cluster) | **POST** /clusters/elasticsearch/{cluster_id}/_restart | Restart cluster
[**set_es_cluster_instances_all_settings_overrides**](ClustersElasticsearchApi.md#set_es_cluster_instances_all_settings_overrides) | **PUT** /clusters/elasticsearch/{cluster_id}/instances/settings | Set settings overrides (all instances)
[**set_es_cluster_instances_settings_overrides**](ClustersElasticsearchApi.md#set_es_cluster_instances_settings_overrides) | **PUT** /clusters/elasticsearch/{cluster_id}/instances/{instance_ids}/settings | Set settings overrides
[**set_es_cluster_metadata_raw**](ClustersElasticsearchApi.md#set_es_cluster_metadata_raw) | **POST** /clusters/elasticsearch/{cluster_id}/metadata/raw | Set cluster metadata
[**set_es_cluster_monitoring**](ClustersElasticsearchApi.md#set_es_cluster_monitoring) | **POST** /clusters/elasticsearch/{cluster_id}/monitoring/{dest_cluster_id} | Set monitoring
[**set_es_cluster_name**](ClustersElasticsearchApi.md#set_es_cluster_name) | **PUT** /clusters/elasticsearch/{cluster_id}/metadata/name/{new_name} | Set cluster name
[**shutdown_es_cluster**](ClustersElasticsearchApi.md#shutdown_es_cluster) | **POST** /clusters/elasticsearch/{cluster_id}/_shutdown | Shut down cluster
[**start_es_cluster_instances**](ClustersElasticsearchApi.md#start_es_cluster_instances) | **POST** /clusters/elasticsearch/{cluster_id}/instances/{instance_ids}/_start | Start instances
[**start_es_cluster_maintenance_mode**](ClustersElasticsearchApi.md#start_es_cluster_maintenance_mode) | **POST** /clusters/elasticsearch/{cluster_id}/instances/{instance_ids}/maintenance-mode/_start | Start maintenance mode
[**stop_es_cluster_instances**](ClustersElasticsearchApi.md#stop_es_cluster_instances) | **POST** /clusters/elasticsearch/{cluster_id}/instances/{instance_ids}/_stop | Stop instances
[**stop_es_cluster_maintenance_mode**](ClustersElasticsearchApi.md#stop_es_cluster_maintenance_mode) | **POST** /clusters/elasticsearch/{cluster_id}/instances/{instance_ids}/maintenance-mode/_stop | Stop maintenance mode
[**update_es_cluster_metadata_settings**](ClustersElasticsearchApi.md#update_es_cluster_metadata_settings) | **PATCH** /clusters/elasticsearch/{cluster_id}/metadata/settings | Update cluster metadata settings
[**update_es_cluster_plan**](ClustersElasticsearchApi.md#update_es_cluster_plan) | **POST** /clusters/elasticsearch/{cluster_id}/plan | Update plan


# **cancel_es_cluster_monitoring**
> EmptyResponse cancel_es_cluster_monitoring(cluster_id)

Cancel monitoring

Deletes all ECE-managed monitoring destinations for an Elasticsearch cluster.

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
api_instance = swagger_client.ClustersElasticsearchApi()
cluster_id = 'cluster_id_example' # str | Identifier for the Elasticsearch cluster

try: 
    # Cancel monitoring
    api_response = api_instance.cancel_es_cluster_monitoring(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersElasticsearchApi->cancel_es_cluster_monitoring: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| Identifier for the Elasticsearch cluster | 

### Return type

[**EmptyResponse**](EmptyResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **cancel_es_cluster_pending_plan**
> EmptyResponse cancel_es_cluster_pending_plan(cluster_id, ignore_missing=ignore_missing)

Cancel pending plan

Cancels the pending plan of an Elasticsearch cluster.

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
api_instance = swagger_client.ClustersElasticsearchApi()
cluster_id = 'cluster_id_example' # str | Identifier for the Elasticsearch cluster
ignore_missing = false # bool | If true, will return successfully regardless of whether there was a pending plan or not (optional) (default to false)

try: 
    # Cancel pending plan
    api_response = api_instance.cancel_es_cluster_pending_plan(cluster_id, ignore_missing=ignore_missing)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersElasticsearchApi->cancel_es_cluster_pending_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| Identifier for the Elasticsearch cluster | 
 **ignore_missing** | **bool**| If true, will return successfully regardless of whether there was a pending plan or not | [optional] [default to false]

### Return type

[**EmptyResponse**](EmptyResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_es_cluster**
> ClusterCrudResponse create_es_cluster(body, validate_only=validate_only)

Create cluster

Creates an Elasticsearch cluster.

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
api_instance = swagger_client.ClustersElasticsearchApi()
body = swagger_client.CreateElasticsearchClusterRequest() # CreateElasticsearchClusterRequest | The cluster definition
validate_only = false # bool | If true, will just validate the cluster definition but will not perform the creation (optional) (default to false)

try: 
    # Create cluster
    api_response = api_instance.create_es_cluster(body, validate_only=validate_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersElasticsearchApi->create_es_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateElasticsearchClusterRequest**](CreateElasticsearchClusterRequest.md)| The cluster definition | 
 **validate_only** | **bool**| If true, will just validate the cluster definition but will not perform the creation | [optional] [default to false]

### Return type

[**ClusterCrudResponse**](ClusterCrudResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_es_cluster**
> EmptyResponse delete_es_cluster(cluster_id)

Delete cluster

Deletes an Elasticsearch cluster. Requires that you have already successfully issued a `_shutdown` command against the cluster.

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
api_instance = swagger_client.ClustersElasticsearchApi()
cluster_id = 'cluster_id_example' # str | Identifier for the Elasticsearch cluster

try: 
    # Delete cluster
    api_response = api_instance.delete_es_cluster(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersElasticsearchApi->delete_es_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| Identifier for the Elasticsearch cluster | 

### Return type

[**EmptyResponse**](EmptyResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_es_cluster_diagnostics**
> str generate_es_cluster_diagnostics(cluster_id)

Generate diagnostics

Retrieves a support diagnostic bundle from the running Elasticsearch cluster.

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
api_instance = swagger_client.ClustersElasticsearchApi()
cluster_id = 'cluster_id_example' # str | Identifier for the Elasticsearch cluster

try: 
    # Generate diagnostics
    api_response = api_instance.generate_es_cluster_diagnostics(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersElasticsearchApi->generate_es_cluster_diagnostics: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| Identifier for the Elasticsearch cluster | 

### Return type

**str**

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate_es_cluster_logs**
> str generate_es_cluster_logs(cluster_id, date)

Generate logs

Retrieves a log file from the logging cluster. WARNING: not currently supported in ECE, SaaS only

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
api_instance = swagger_client.ClustersElasticsearchApi()
cluster_id = 'cluster_id_example' # str | Identifier for the Elasticsearch cluster
date = 'date_example' # str | A date string (standard format, eg 'YYY-MM-DD[THH[:mm]]') representing the start date for the log retrieval

try: 
    # Generate logs
    api_response = api_instance.generate_es_cluster_logs(cluster_id, date)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersElasticsearchApi->generate_es_cluster_logs: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| Identifier for the Elasticsearch cluster | 
 **date** | **str**| A date string (standard format, eg &#39;YYY-MM-DD[THH[:mm]]&#39;) representing the start date for the log retrieval | 

### Return type

**str**

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_es_cluster**
> ElasticsearchClusterInfo get_es_cluster(cluster_id, show_security=show_security, show_metadata=show_metadata, show_plans=show_plans, show_plan_logs=show_plan_logs, show_plan_defaults=show_plan_defaults, show_system_alerts=show_system_alerts)

Get cluster

Retrieves cluster information for an Elasticsearch cluster.

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
api_instance = swagger_client.ClustersElasticsearchApi()
cluster_id = 'cluster_id_example' # str | Identifier for the Elasticsearch cluster
show_security = false # bool | Whether to include the Elasticsearch 2.x security information in the response - can be large per cluster and also include credentials (optional) (default to false)
show_metadata = false # bool | Whether to include the full cluster metadata in the response - can be large per cluster and also include credentials (optional) (default to false)
show_plans = true # bool | Whether to include the full current and pending plan information in the response - can be large per cluster (optional) (default to true)
show_plan_logs = false # bool | Whether to include with the current and pending plan information the attempt log - can be very large per cluster (optional) (default to false)
show_plan_defaults = false # bool | If showing plans, whether to show values that are left at their default value (less readable but more informative) (optional) (default to false)
show_system_alerts = 0 # int | Number of system alerts (such as forced restarts due to memory limits) to be included in the response - can be large per cluster. Negative numbers or 0 will not return field. (optional) (default to 0)

try: 
    # Get cluster
    api_response = api_instance.get_es_cluster(cluster_id, show_security=show_security, show_metadata=show_metadata, show_plans=show_plans, show_plan_logs=show_plan_logs, show_plan_defaults=show_plan_defaults, show_system_alerts=show_system_alerts)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersElasticsearchApi->get_es_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| Identifier for the Elasticsearch cluster | 
 **show_security** | **bool**| Whether to include the Elasticsearch 2.x security information in the response - can be large per cluster and also include credentials | [optional] [default to false]
 **show_metadata** | **bool**| Whether to include the full cluster metadata in the response - can be large per cluster and also include credentials | [optional] [default to false]
 **show_plans** | **bool**| Whether to include the full current and pending plan information in the response - can be large per cluster | [optional] [default to true]
 **show_plan_logs** | **bool**| Whether to include with the current and pending plan information the attempt log - can be very large per cluster | [optional] [default to false]
 **show_plan_defaults** | **bool**| If showing plans, whether to show values that are left at their default value (less readable but more informative) | [optional] [default to false]
 **show_system_alerts** | **int**| Number of system alerts (such as forced restarts due to memory limits) to be included in the response - can be large per cluster. Negative numbers or 0 will not return field. | [optional] [default to 0]

### Return type

[**ElasticsearchClusterInfo**](ElasticsearchClusterInfo.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_es_cluster_metadata_raw**
> object get_es_cluster_metadata_raw(cluster_id)

Get cluster metadata in raw form

Advanced use only: Retrieves the internal cluster metadata (free-form JSON) for an Elasticsearch cluster.

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
api_instance = swagger_client.ClustersElasticsearchApi()
cluster_id = 'cluster_id_example' # str | Identifier for the Elasticsearch cluster

try: 
    # Get cluster metadata in raw form
    api_response = api_instance.get_es_cluster_metadata_raw(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersElasticsearchApi->get_es_cluster_metadata_raw: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| Identifier for the Elasticsearch cluster | 

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_es_cluster_metadata_settings**
> ClusterMetadataSettings get_es_cluster_metadata_settings(cluster_id)

Get cluster metadata settings



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
api_instance = swagger_client.ClustersElasticsearchApi()
cluster_id = 'cluster_id_example' # str | Identifier for the Elasticsearch cluster

try: 
    # Get cluster metadata settings
    api_response = api_instance.get_es_cluster_metadata_settings(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersElasticsearchApi->get_es_cluster_metadata_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| Identifier for the Elasticsearch cluster | 

### Return type

[**ClusterMetadataSettings**](ClusterMetadataSettings.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_es_cluster_pending_plan**
> ElasticsearchClusterPlan get_es_cluster_pending_plan(cluster_id, show_plan_defaults=show_plan_defaults)

Get pending plan

Retrieves the pending plan of a cluster.

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
api_instance = swagger_client.ClustersElasticsearchApi()
cluster_id = 'cluster_id_example' # str | Identifier for the Elasticsearch cluster
show_plan_defaults = false # bool | Whether to show values that are left at their default value (less readable but more informative) (optional) (default to false)

try: 
    # Get pending plan
    api_response = api_instance.get_es_cluster_pending_plan(cluster_id, show_plan_defaults=show_plan_defaults)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersElasticsearchApi->get_es_cluster_pending_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| Identifier for the Elasticsearch cluster | 
 **show_plan_defaults** | **bool**| Whether to show values that are left at their default value (less readable but more informative) | [optional] [default to false]

### Return type

[**ElasticsearchClusterPlan**](ElasticsearchClusterPlan.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_es_cluster_plan**
> ElasticsearchClusterPlan get_es_cluster_plan(cluster_id, show_plan_defaults=show_plan_defaults)

Get plan

Retrieves the active plan of an Elasticsearch cluster.

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
api_instance = swagger_client.ClustersElasticsearchApi()
cluster_id = 'cluster_id_example' # str | Identifier for the Elasticsearch cluster
show_plan_defaults = false # bool | Whether to show values that are left at their default value (less readable but more informative) (optional) (default to false)

try: 
    # Get plan
    api_response = api_instance.get_es_cluster_plan(cluster_id, show_plan_defaults=show_plan_defaults)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersElasticsearchApi->get_es_cluster_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| Identifier for the Elasticsearch cluster | 
 **show_plan_defaults** | **bool**| Whether to show values that are left at their default value (less readable but more informative) | [optional] [default to false]

### Return type

[**ElasticsearchClusterPlan**](ElasticsearchClusterPlan.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_es_cluster_plan_activity**
> ElasticsearchClusterPlansInfo get_es_cluster_plan_activity(cluster_id, show_plan_logs=show_plan_logs, show_plan_defaults=show_plan_defaults)

Get plan activity

Retrieves the current and historical plan information for an Elasticsearch cluster.

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
api_instance = swagger_client.ClustersElasticsearchApi()
cluster_id = 'cluster_id_example' # str | Identifier for the Elasticsearch cluster
show_plan_logs = true # bool | Whether to include with the current/pending/historical plan information the attempt log - can be very large per cluster (optional) (default to true)
show_plan_defaults = false # bool | Whether to show values that are left at their default value (less readable but more informative) (optional) (default to false)

try: 
    # Get plan activity
    api_response = api_instance.get_es_cluster_plan_activity(cluster_id, show_plan_logs=show_plan_logs, show_plan_defaults=show_plan_defaults)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersElasticsearchApi->get_es_cluster_plan_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| Identifier for the Elasticsearch cluster | 
 **show_plan_logs** | **bool**| Whether to include with the current/pending/historical plan information the attempt log - can be very large per cluster | [optional] [default to true]
 **show_plan_defaults** | **bool**| Whether to show values that are left at their default value (less readable but more informative) | [optional] [default to false]

### Return type

[**ElasticsearchClusterPlansInfo**](ElasticsearchClusterPlansInfo.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_es_clusters**
> ElasticsearchClustersInfo get_es_clusters(_from=_from, size=size, show_security=show_security, show_metadata=show_metadata, show_plans=show_plans, show_plan_defaults=show_plan_defaults, show_system_alerts=show_system_alerts, show_hidden=show_hidden)

Get clusters

Retrieves cluster information for all Elasticsearch clusters.

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
api_instance = swagger_client.ClustersElasticsearchApi()
_from = 0 # int | The number of clusters to skip over (optional) (default to 0)
size = 100 # int | The maximum number of clusters to return (set to -1 for all clusters - use with care, can result in large responses) (optional) (default to 100)
show_security = false # bool | Whether to include the Elasticsearch 2.x security information in the response - can be large per cluster and also include credentials (optional) (default to false)
show_metadata = false # bool | Whether to include the full cluster metadata in the response - can be large per cluster and also include credentials (optional) (default to false)
show_plans = false # bool | Whether to include the full current and pending plan information in the response - can be large per cluster (optional) (default to false)
show_plan_defaults = false # bool | If showing plans, whether to show values that are left at their default value (less readable but more informative) (optional) (default to false)
show_system_alerts = 0 # int | Number of system alerts (such as forced restarts due to memory limits) to be included in the response - can be large per cluster. Negative numbers or 0 will not return field. (optional) (default to 0)
show_hidden = true # bool | Whether to include hidden clusters in the response or not (optional)

try: 
    # Get clusters
    api_response = api_instance.get_es_clusters(_from=_from, size=size, show_security=show_security, show_metadata=show_metadata, show_plans=show_plans, show_plan_defaults=show_plan_defaults, show_system_alerts=show_system_alerts, show_hidden=show_hidden)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersElasticsearchApi->get_es_clusters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **int**| The number of clusters to skip over | [optional] [default to 0]
 **size** | **int**| The maximum number of clusters to return (set to -1 for all clusters - use with care, can result in large responses) | [optional] [default to 100]
 **show_security** | **bool**| Whether to include the Elasticsearch 2.x security information in the response - can be large per cluster and also include credentials | [optional] [default to false]
 **show_metadata** | **bool**| Whether to include the full cluster metadata in the response - can be large per cluster and also include credentials | [optional] [default to false]
 **show_plans** | **bool**| Whether to include the full current and pending plan information in the response - can be large per cluster | [optional] [default to false]
 **show_plan_defaults** | **bool**| If showing plans, whether to show values that are left at their default value (less readable but more informative) | [optional] [default to false]
 **show_system_alerts** | **int**| Number of system alerts (such as forced restarts due to memory limits) to be included in the response - can be large per cluster. Negative numbers or 0 will not return field. | [optional] [default to 0]
 **show_hidden** | **bool**| Whether to include hidden clusters in the response or not | [optional] 

### Return type

[**ElasticsearchClustersInfo**](ElasticsearchClustersInfo.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_es_cluster_instances**
> EmptyResponse move_es_cluster_instances(cluster_id, instance_ids, body=body, ignore_missing=ignore_missing, force_update=force_update, instances_down=instances_down, validate_only=validate_only)

Move instances

Moves one or more instances belonging to an Elasticsearch cluster

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
api_instance = swagger_client.ClustersElasticsearchApi()
cluster_id = 'cluster_id_example' # str | Identifier for the Elasticsearch cluster
instance_ids = ['instance_ids_example'] # list[str] | Optional comma-delimited list of instance identifiers of the Elasticsearch cluster, otherwise will apply to all instances
body = swagger_client.TransientElasticsearchPlanConfiguration() # TransientElasticsearchPlanConfiguration | Overrides defaults for the move, including setting the configuration of instances specified in the path (optional)
ignore_missing = false # bool | If true and the instance does not exist then quietly proceed to the next instance, otherwise treated as an error (optional) (default to false)
force_update = false # bool | If true, will cancel any pending plans and overwrite with this move plan, else will error (optional) (default to false)
instances_down = false # bool | If true the the instances specified by 'instance_ids' will be considered to be permanently down for the purposes of data migration logic (optional) (default to false)
validate_only = false # bool | If true, will validate the move request and return the calculated plan without actually applying it. (optional) (default to false)

try: 
    # Move instances
    api_response = api_instance.move_es_cluster_instances(cluster_id, instance_ids, body=body, ignore_missing=ignore_missing, force_update=force_update, instances_down=instances_down, validate_only=validate_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersElasticsearchApi->move_es_cluster_instances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| Identifier for the Elasticsearch cluster | 
 **instance_ids** | [**list[str]**](str.md)| Optional comma-delimited list of instance identifiers of the Elasticsearch cluster, otherwise will apply to all instances | 
 **body** | [**TransientElasticsearchPlanConfiguration**](TransientElasticsearchPlanConfiguration.md)| Overrides defaults for the move, including setting the configuration of instances specified in the path | [optional] 
 **ignore_missing** | **bool**| If true and the instance does not exist then quietly proceed to the next instance, otherwise treated as an error | [optional] [default to false]
 **force_update** | **bool**| If true, will cancel any pending plans and overwrite with this move plan, else will error | [optional] [default to false]
 **instances_down** | **bool**| If true the the instances specified by &#39;instance_ids&#39; will be considered to be permanently down for the purposes of data migration logic | [optional] [default to false]
 **validate_only** | **bool**| If true, will validate the move request and return the calculated plan without actually applying it. | [optional] [default to false]

### Return type

[**EmptyResponse**](EmptyResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_es_cluster_instances_advanced**
> ClusterCommandResponse move_es_cluster_instances_advanced(body, cluster_id, ignore_missing=ignore_missing, force_update=force_update, instances_down=instances_down, validate_only=validate_only)

Move instances (advanced)

Moves one or more instances belonging to an Elasticsearch cluster, with custom configuration posted in the body

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
api_instance = swagger_client.ClustersElasticsearchApi()
body = swagger_client.TransientElasticsearchPlanConfiguration() # TransientElasticsearchPlanConfiguration | Overrides defaults for the move, including setting the configuration of instances specified in the path
cluster_id = 'cluster_id_example' # str | Identifier for the Elasticsearch cluster
ignore_missing = false # bool | If true and the instance does not exist then quietly proceed to the next instance, otherwise treated as an error (optional) (default to false)
force_update = false # bool | If true, will cancel any pending plans and overwrite with this move plan, else will error (optional) (default to false)
instances_down = false # bool | If true the the instances specified by 'instance_ids' will be considered to be permanently down for the purposes of data migration logic (optional) (default to false)
validate_only = false # bool | If true, will validate the move request and return the calculated plan without actually applying it. (optional) (default to false)

try: 
    # Move instances (advanced)
    api_response = api_instance.move_es_cluster_instances_advanced(body, cluster_id, ignore_missing=ignore_missing, force_update=force_update, instances_down=instances_down, validate_only=validate_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersElasticsearchApi->move_es_cluster_instances_advanced: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TransientElasticsearchPlanConfiguration**](TransientElasticsearchPlanConfiguration.md)| Overrides defaults for the move, including setting the configuration of instances specified in the path | 
 **cluster_id** | **str**| Identifier for the Elasticsearch cluster | 
 **ignore_missing** | **bool**| If true and the instance does not exist then quietly proceed to the next instance, otherwise treated as an error | [optional] [default to false]
 **force_update** | **bool**| If true, will cancel any pending plans and overwrite with this move plan, else will error | [optional] [default to false]
 **instances_down** | **bool**| If true the the instances specified by &#39;instance_ids&#39; will be considered to be permanently down for the purposes of data migration logic | [optional] [default to false]
 **validate_only** | **bool**| If true, will validate the move request and return the calculated plan without actually applying it. | [optional] [default to false]

### Return type

[**ClusterCommandResponse**](ClusterCommandResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restart_es_cluster**
> ClusterCommandResponse restart_es_cluster(cluster_id, restore_snapshot=restore_snapshot, skip_snapshot=skip_snapshot, cancel_pending=cancel_pending, group_attribute=group_attribute)

Restart cluster

Restarts an Elasticsearch cluster. If a cluster is active: this command re-applies the existing plan but applies a \"cluster_reboot\", which issues an Elasticsearch restart command and waits for it to complete. If a cluster is inactive: this command starts it up with the most recent successful plan.

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
api_instance = swagger_client.ClustersElasticsearchApi()
cluster_id = 'cluster_id_example' # str | Identifier for the Elasticsearch cluster
restore_snapshot = true # bool | If restoring from shutdown and true (the default), then will restore the cluster from the last snapshot (if available) (optional) (default to true)
skip_snapshot = true # bool | If true, will take a snapshot of the cluster before restarting (if possible) (optional) (default to true)
cancel_pending = false # bool | If true, will cancel any pending plans before restarting (else will error) (optional) (default to false)
group_attribute = '\\_\\_all\\_\\_' # str | Indicates the property or properties used to divide the list of instances to restart in groups. Valid options are: '\\_\\_all\\_\\_' (restart all at once), '\\_\\_zone\\_\\_' by logical zone, '\\_\\_name\\_\\_' one instance at the time, or a comma-separated list of attributes of the instances (optional) (default to \_\_all\_\_)

try: 
    # Restart cluster
    api_response = api_instance.restart_es_cluster(cluster_id, restore_snapshot=restore_snapshot, skip_snapshot=skip_snapshot, cancel_pending=cancel_pending, group_attribute=group_attribute)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersElasticsearchApi->restart_es_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| Identifier for the Elasticsearch cluster | 
 **restore_snapshot** | **bool**| If restoring from shutdown and true (the default), then will restore the cluster from the last snapshot (if available) | [optional] [default to true]
 **skip_snapshot** | **bool**| If true, will take a snapshot of the cluster before restarting (if possible) | [optional] [default to true]
 **cancel_pending** | **bool**| If true, will cancel any pending plans before restarting (else will error) | [optional] [default to false]
 **group_attribute** | **str**| Indicates the property or properties used to divide the list of instances to restart in groups. Valid options are: &#39;\\_\\_all\\_\\_&#39; (restart all at once), &#39;\\_\\_zone\\_\\_&#39; by logical zone, &#39;\\_\\_name\\_\\_&#39; one instance at the time, or a comma-separated list of attributes of the instances | [optional] [default to \_\_all\_\_]

### Return type

[**ClusterCommandResponse**](ClusterCommandResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_es_cluster_instances_all_settings_overrides**
> ElasticsearchClusterInstanceSettingsOverrides set_es_cluster_instances_all_settings_overrides(cluster_id, body=body, restart_after_update=restart_after_update)

Set settings overrides (all instances)

Overrides settings for all instances belonging to an Elasticsearch cluster.

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
api_instance = swagger_client.ClustersElasticsearchApi()
cluster_id = 'cluster_id_example' # str | Identifier for the Elasticsearch cluster
body = swagger_client.ElasticsearchClusterInstanceSettingsOverrides() # ElasticsearchClusterInstanceSettingsOverrides | The settings to override for the instances. (optional)
restart_after_update = false # bool | Whether or not to restart the instances after the overrides are applied. (optional) (default to false)

try: 
    # Set settings overrides (all instances)
    api_response = api_instance.set_es_cluster_instances_all_settings_overrides(cluster_id, body=body, restart_after_update=restart_after_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersElasticsearchApi->set_es_cluster_instances_all_settings_overrides: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| Identifier for the Elasticsearch cluster | 
 **body** | [**ElasticsearchClusterInstanceSettingsOverrides**](ElasticsearchClusterInstanceSettingsOverrides.md)| The settings to override for the instances. | [optional] 
 **restart_after_update** | **bool**| Whether or not to restart the instances after the overrides are applied. | [optional] [default to false]

### Return type

[**ElasticsearchClusterInstanceSettingsOverrides**](ElasticsearchClusterInstanceSettingsOverrides.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_es_cluster_instances_settings_overrides**
> ElasticsearchClusterInstanceSettingsOverrides set_es_cluster_instances_settings_overrides(cluster_id, instance_ids, body=body, ignore_missing=ignore_missing, restart_after_update=restart_after_update)

Set settings overrides

Overrides settings for instances belonging to an Elasticsearch cluster.

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
api_instance = swagger_client.ClustersElasticsearchApi()
cluster_id = 'cluster_id_example' # str | Identifier for the Elasticsearch cluster
instance_ids = ['instance_ids_example'] # list[str] | Optional comma-delimited list of instance identifiers of the Elasticsearch cluster, otherwise will apply to all instances
body = swagger_client.ElasticsearchClusterInstanceSettingsOverrides() # ElasticsearchClusterInstanceSettingsOverrides | The settings to override for the specified instances. (optional)
ignore_missing = false # bool | If true and the instance does not exist then quietly proceed to the next instance, otherwise treated as an error (optional) (default to false)
restart_after_update = false # bool | Whether or not to restart the instances after the overrides are applied. (optional) (default to false)

try: 
    # Set settings overrides
    api_response = api_instance.set_es_cluster_instances_settings_overrides(cluster_id, instance_ids, body=body, ignore_missing=ignore_missing, restart_after_update=restart_after_update)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersElasticsearchApi->set_es_cluster_instances_settings_overrides: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| Identifier for the Elasticsearch cluster | 
 **instance_ids** | [**list[str]**](str.md)| Optional comma-delimited list of instance identifiers of the Elasticsearch cluster, otherwise will apply to all instances | 
 **body** | [**ElasticsearchClusterInstanceSettingsOverrides**](ElasticsearchClusterInstanceSettingsOverrides.md)| The settings to override for the specified instances. | [optional] 
 **ignore_missing** | **bool**| If true and the instance does not exist then quietly proceed to the next instance, otherwise treated as an error | [optional] [default to false]
 **restart_after_update** | **bool**| Whether or not to restart the instances after the overrides are applied. | [optional] [default to false]

### Return type

[**ElasticsearchClusterInstanceSettingsOverrides**](ElasticsearchClusterInstanceSettingsOverrides.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_es_cluster_metadata_raw**
> object set_es_cluster_metadata_raw(cluster_id, body, version=version)

Set cluster metadata

Advanced use only: Sets the internal cluster metadata (free-form JSON) for an Elasticsearch cluster. Must only be used to set a modified version of the JSON returned from the get version of the metadata.

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
api_instance = swagger_client.ClustersElasticsearchApi()
cluster_id = 'cluster_id_example' # str | Identifier for the Elasticsearch cluster
body = 'body_example' # str | The freeform JSON for the cluster (should always be based on the current version retrieved from the GET)
version = 56 # int | If specified then checks for conflicts against the version of the cluster metadata (returned in 'x-cloud-resource-version' of the GET request) (optional)

try: 
    # Set cluster metadata
    api_response = api_instance.set_es_cluster_metadata_raw(cluster_id, body, version=version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersElasticsearchApi->set_es_cluster_metadata_raw: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| Identifier for the Elasticsearch cluster | 
 **body** | **str**| The freeform JSON for the cluster (should always be based on the current version retrieved from the GET) | 
 **version** | **int**| If specified then checks for conflicts against the version of the cluster metadata (returned in &#39;x-cloud-resource-version&#39; of the GET request) | [optional] 

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_es_cluster_monitoring**
> EmptyResponse set_es_cluster_monitoring(cluster_id, dest_cluster_id)

Set monitoring

Overwrites or creates the ECE-managed monitoring destination for an Elasticsearch cluster.

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
api_instance = swagger_client.ClustersElasticsearchApi()
cluster_id = 'cluster_id_example' # str | Identifier for the Elasticsearch cluster
dest_cluster_id = 'dest_cluster_id_example' # str | The id of the cluster that will be the new monitoring destination

try: 
    # Set monitoring
    api_response = api_instance.set_es_cluster_monitoring(cluster_id, dest_cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersElasticsearchApi->set_es_cluster_monitoring: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| Identifier for the Elasticsearch cluster | 
 **dest_cluster_id** | **str**| The id of the cluster that will be the new monitoring destination | 

### Return type

[**EmptyResponse**](EmptyResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_es_cluster_name**
> EmptyResponse set_es_cluster_name(cluster_id, new_name)

Set cluster name

Sets the name of an Elasticsearch cluster.

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
api_instance = swagger_client.ClustersElasticsearchApi()
cluster_id = 'cluster_id_example' # str | Identifier for the Elasticsearch cluster
new_name = 'new_name_example' # str | The new name for the cluster

try: 
    # Set cluster name
    api_response = api_instance.set_es_cluster_name(cluster_id, new_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersElasticsearchApi->set_es_cluster_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| Identifier for the Elasticsearch cluster | 
 **new_name** | **str**| The new name for the cluster | 

### Return type

[**EmptyResponse**](EmptyResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shutdown_es_cluster**
> ClusterCommandResponse shutdown_es_cluster(cluster_id, skip_snapshot=skip_snapshot, hide=hide)

Shut down cluster

Shuts down a running cluster and removes all nodes belonging to the cluster. The plan for the cluster is retained. Warning: this will lose all cluster data that is not saved in a snapshot repository.

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
api_instance = swagger_client.ClustersElasticsearchApi()
cluster_id = 'cluster_id_example' # str | Identifier for the Elasticsearch cluster
skip_snapshot = false # bool | If true, will skip taking a snapshot of the cluster before shutting the cluster down (if even possible) (optional) (default to false)
hide = false # bool | Hide cluster on shutdown. Hidden clusters are not listed by default. (optional) (default to false)

try: 
    # Shut down cluster
    api_response = api_instance.shutdown_es_cluster(cluster_id, skip_snapshot=skip_snapshot, hide=hide)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersElasticsearchApi->shutdown_es_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| Identifier for the Elasticsearch cluster | 
 **skip_snapshot** | **bool**| If true, will skip taking a snapshot of the cluster before shutting the cluster down (if even possible) | [optional] [default to false]
 **hide** | **bool**| Hide cluster on shutdown. Hidden clusters are not listed by default. | [optional] [default to false]

### Return type

[**ClusterCommandResponse**](ClusterCommandResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_es_cluster_instances**
> ClusterCommandResponse start_es_cluster_instances(cluster_id, instance_ids, ignore_missing=ignore_missing)

Start instances

Starts the instances belonging to an Elasticsearch cluster

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
api_instance = swagger_client.ClustersElasticsearchApi()
cluster_id = 'cluster_id_example' # str | Identifier for the Elasticsearch cluster
instance_ids = ['instance_ids_example'] # list[str] | Optional comma-delimited list of instance identifiers of the Elasticsearch cluster, otherwise will apply to all instances
ignore_missing = false # bool | If true and the instance does not exist then quietly proceed to the next instance, otherwise treated as an error (optional) (default to false)

try: 
    # Start instances
    api_response = api_instance.start_es_cluster_instances(cluster_id, instance_ids, ignore_missing=ignore_missing)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersElasticsearchApi->start_es_cluster_instances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| Identifier for the Elasticsearch cluster | 
 **instance_ids** | [**list[str]**](str.md)| Optional comma-delimited list of instance identifiers of the Elasticsearch cluster, otherwise will apply to all instances | 
 **ignore_missing** | **bool**| If true and the instance does not exist then quietly proceed to the next instance, otherwise treated as an error | [optional] [default to false]

### Return type

[**ClusterCommandResponse**](ClusterCommandResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_es_cluster_maintenance_mode**
> ClusterCommandResponse start_es_cluster_maintenance_mode(cluster_id, instance_ids, ignore_missing=ignore_missing)

Start maintenance mode

Starts maintenance mode of instances belonging to an Elasticsearch cluster.

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
api_instance = swagger_client.ClustersElasticsearchApi()
cluster_id = 'cluster_id_example' # str | Identifier for the Elasticsearch cluster
instance_ids = ['instance_ids_example'] # list[str] | Optional comma-delimited list of instance identifiers of the Elasticsearch cluster, otherwise will apply to all instances
ignore_missing = false # bool | If true and the instance does not exist then quietly proceed to the next instance, otherwise treated as an error (optional) (default to false)

try: 
    # Start maintenance mode
    api_response = api_instance.start_es_cluster_maintenance_mode(cluster_id, instance_ids, ignore_missing=ignore_missing)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersElasticsearchApi->start_es_cluster_maintenance_mode: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| Identifier for the Elasticsearch cluster | 
 **instance_ids** | [**list[str]**](str.md)| Optional comma-delimited list of instance identifiers of the Elasticsearch cluster, otherwise will apply to all instances | 
 **ignore_missing** | **bool**| If true and the instance does not exist then quietly proceed to the next instance, otherwise treated as an error | [optional] [default to false]

### Return type

[**ClusterCommandResponse**](ClusterCommandResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_es_cluster_instances**
> ClusterCommandResponse stop_es_cluster_instances(cluster_id, instance_ids, ignore_missing=ignore_missing)

Stop instances

Stops the instances belonging to an Elasticsearch cluster.

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
api_instance = swagger_client.ClustersElasticsearchApi()
cluster_id = 'cluster_id_example' # str | Identifier for the Elasticsearch cluster
instance_ids = ['instance_ids_example'] # list[str] | Optional comma-delimited list of instance identifiers of the Elasticsearch cluster, otherwise will apply to all instances
ignore_missing = false # bool | If true and the instance does not exist then quietly proceed to the next instance, otherwise treated as an error (optional) (default to false)

try: 
    # Stop instances
    api_response = api_instance.stop_es_cluster_instances(cluster_id, instance_ids, ignore_missing=ignore_missing)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersElasticsearchApi->stop_es_cluster_instances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| Identifier for the Elasticsearch cluster | 
 **instance_ids** | [**list[str]**](str.md)| Optional comma-delimited list of instance identifiers of the Elasticsearch cluster, otherwise will apply to all instances | 
 **ignore_missing** | **bool**| If true and the instance does not exist then quietly proceed to the next instance, otherwise treated as an error | [optional] [default to false]

### Return type

[**ClusterCommandResponse**](ClusterCommandResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_es_cluster_maintenance_mode**
> ClusterCommandResponse stop_es_cluster_maintenance_mode(cluster_id, instance_ids, ignore_missing=ignore_missing)

Stop maintenance mode

Stops maintenance mode of instances belonging to an Elasticsearch cluster.

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
api_instance = swagger_client.ClustersElasticsearchApi()
cluster_id = 'cluster_id_example' # str | Identifier for the Elasticsearch cluster
instance_ids = ['instance_ids_example'] # list[str] | Optional comma-delimited list of instance identifiers of the Elasticsearch cluster, otherwise will apply to all instances
ignore_missing = false # bool | If true and the instance does not exist then quietly proceed to the next instance, otherwise treated as an error (optional) (default to false)

try: 
    # Stop maintenance mode
    api_response = api_instance.stop_es_cluster_maintenance_mode(cluster_id, instance_ids, ignore_missing=ignore_missing)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersElasticsearchApi->stop_es_cluster_maintenance_mode: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| Identifier for the Elasticsearch cluster | 
 **instance_ids** | [**list[str]**](str.md)| Optional comma-delimited list of instance identifiers of the Elasticsearch cluster, otherwise will apply to all instances | 
 **ignore_missing** | **bool**| If true and the instance does not exist then quietly proceed to the next instance, otherwise treated as an error | [optional] [default to false]

### Return type

[**ClusterCommandResponse**](ClusterCommandResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_es_cluster_metadata_settings**
> ClusterMetadataSettings update_es_cluster_metadata_settings(cluster_id, body, version=version)

Update cluster metadata settings

Any changes in the PATCHed object will be applied to the metadata settings object.  PATCHing existing fields will cause same values to be re-applied. PATCHing a value of 'null' will cause the field to be reverted to its default value or removed if no default value exists

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
api_instance = swagger_client.ClustersElasticsearchApi()
cluster_id = 'cluster_id_example' # str | Identifier for the Elasticsearch cluster
body = swagger_client.ClusterMetadataSettings() # ClusterMetadataSettings | The cluster settings including updated values
version = 56 # int | If specified then checks for conflicts against the version of the cluster metadata (returned in 'x-cloud-resource-version' of the GET request) (optional)

try: 
    # Update cluster metadata settings
    api_response = api_instance.update_es_cluster_metadata_settings(cluster_id, body, version=version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersElasticsearchApi->update_es_cluster_metadata_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| Identifier for the Elasticsearch cluster | 
 **body** | [**ClusterMetadataSettings**](ClusterMetadataSettings.md)| The cluster settings including updated values | 
 **version** | **int**| If specified then checks for conflicts against the version of the cluster metadata (returned in &#39;x-cloud-resource-version&#39; of the GET request) | [optional] 

### Return type

[**ClusterMetadataSettings**](ClusterMetadataSettings.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_es_cluster_plan**
> ClusterCrudResponse update_es_cluster_plan(body, cluster_id, validate_only=validate_only)

Update plan

Updates the configuration of an existing Elasticsearch cluster.

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
api_instance = swagger_client.ClustersElasticsearchApi()
body = swagger_client.ElasticsearchClusterPlan() # ElasticsearchClusterPlan | The update plan definition
cluster_id = 'cluster_id_example' # str | Identifier for the Elasticsearch cluster
validate_only = false # bool | If true, will just validate the cluster definition but will not perform the update (optional) (default to false)

try: 
    # Update plan
    api_response = api_instance.update_es_cluster_plan(body, cluster_id, validate_only=validate_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersElasticsearchApi->update_es_cluster_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ElasticsearchClusterPlan**](ElasticsearchClusterPlan.md)| The update plan definition | 
 **cluster_id** | **str**| Identifier for the Elasticsearch cluster | 
 **validate_only** | **bool**| If true, will just validate the cluster definition but will not perform the update | [optional] [default to false]

### Return type

[**ClusterCrudResponse**](ClusterCrudResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

