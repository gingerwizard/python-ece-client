# swagger_client.ClustersKibanaApi

All URIs are relative to *http://localhost/api/v1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_kibana_cluster_pending_plan**](ClustersKibanaApi.md#cancel_kibana_cluster_pending_plan) | **DELETE** /clusters/kibana/{cluster_id}/plan/pending | Cancel pending plan
[**create_kibana_cluster**](ClustersKibanaApi.md#create_kibana_cluster) | **POST** /clusters/kibana | Create cluster
[**delete_kibana_cluster**](ClustersKibanaApi.md#delete_kibana_cluster) | **DELETE** /clusters/kibana/{cluster_id} | Delete cluster
[**get_kibana_cluster**](ClustersKibanaApi.md#get_kibana_cluster) | **GET** /clusters/kibana/{cluster_id} | Get cluster
[**get_kibana_cluster_metadata_raw**](ClustersKibanaApi.md#get_kibana_cluster_metadata_raw) | **GET** /clusters/kibana/{cluster_id}/metadata/raw | Get cluster metadata
[**get_kibana_cluster_metadata_settings**](ClustersKibanaApi.md#get_kibana_cluster_metadata_settings) | **GET** /clusters/kibana/{cluster_id}/metadata/settings | Get cluster metadata settings
[**get_kibana_cluster_pending_plan**](ClustersKibanaApi.md#get_kibana_cluster_pending_plan) | **GET** /clusters/kibana/{cluster_id}/plan/pending | Get pending plan
[**get_kibana_cluster_plan**](ClustersKibanaApi.md#get_kibana_cluster_plan) | **GET** /clusters/kibana/{cluster_id}/plan | Get plan
[**get_kibana_cluster_plan_activity**](ClustersKibanaApi.md#get_kibana_cluster_plan_activity) | **GET** /clusters/kibana/{cluster_id}/plan/activity | Get plan activity
[**get_kibana_clusters**](ClustersKibanaApi.md#get_kibana_clusters) | **GET** /clusters/kibana | Get clusters
[**move_kibana_cluster_instances**](ClustersKibanaApi.md#move_kibana_cluster_instances) | **POST** /clusters/kibana/{cluster_id}/instances/{instance_ids}/_move | Move instances
[**move_kibana_cluster_instances_advanced**](ClustersKibanaApi.md#move_kibana_cluster_instances_advanced) | **POST** /clusters/kibana/{cluster_id}/instances/_move | Move instances (advanced)
[**restart_kibana_cluster**](ClustersKibanaApi.md#restart_kibana_cluster) | **POST** /clusters/kibana/{cluster_id}/_restart | Restart cluster
[**set_kibana_cluster_metadata_raw**](ClustersKibanaApi.md#set_kibana_cluster_metadata_raw) | **POST** /clusters/kibana/{cluster_id}/metadata/raw | Set cluster metadata
[**set_kibana_cluster_name**](ClustersKibanaApi.md#set_kibana_cluster_name) | **PUT** /clusters/kibana/{cluster_id}/metadata/name/{new_name} | Set cluster name
[**shutdown_kibana_cluster**](ClustersKibanaApi.md#shutdown_kibana_cluster) | **POST** /clusters/kibana/{cluster_id}/_shutdown | Shut down cluster
[**start_kibana_cluster_instances**](ClustersKibanaApi.md#start_kibana_cluster_instances) | **POST** /clusters/kibana/{cluster_id}/instances/{instance_ids}/_start | Start instances
[**start_kibana_cluster_maintenance_mode**](ClustersKibanaApi.md#start_kibana_cluster_maintenance_mode) | **POST** /clusters/kibana/{cluster_id}/instances/{instance_ids}/maintenance-mode/_start | Start maintenance mode
[**stop_kibana_cluster_instances**](ClustersKibanaApi.md#stop_kibana_cluster_instances) | **POST** /clusters/kibana/{cluster_id}/instances/{instance_ids}/_stop | Stop instances
[**stop_kibana_cluster_maintenance_mode**](ClustersKibanaApi.md#stop_kibana_cluster_maintenance_mode) | **POST** /clusters/kibana/{cluster_id}/instances/{instance_ids}/maintenance-mode/_stop | Stop maintenance mode
[**update_kibana_cluster_metadata_settings**](ClustersKibanaApi.md#update_kibana_cluster_metadata_settings) | **PATCH** /clusters/kibana/{cluster_id}/metadata/settings | Update cluster metadata settings
[**update_kibana_cluster_plan**](ClustersKibanaApi.md#update_kibana_cluster_plan) | **POST** /clusters/kibana/{cluster_id}/plan | Update plan


# **cancel_kibana_cluster_pending_plan**
> EmptyResponse cancel_kibana_cluster_pending_plan(cluster_id, ignore_missing=ignore_missing)

Cancel pending plan

Cancels the pending plan of a Kibana cluster.

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
api_instance = swagger_client.ClustersKibanaApi()
cluster_id = 'cluster_id_example' # str | Identifier for the Kibana cluster
ignore_missing = false # bool | If true (default false), will return successfully regardless of whether there was a pending plan or not (optional) (default to false)

try: 
    # Cancel pending plan
    api_response = api_instance.cancel_kibana_cluster_pending_plan(cluster_id, ignore_missing=ignore_missing)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersKibanaApi->cancel_kibana_cluster_pending_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| Identifier for the Kibana cluster | 
 **ignore_missing** | **bool**| If true (default false), will return successfully regardless of whether there was a pending plan or not | [optional] [default to false]

### Return type

[**EmptyResponse**](EmptyResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_kibana_cluster**
> ClusterCrudResponse create_kibana_cluster(body, validate_only=validate_only)

Create cluster

Creates a Kibana cluster for a given Elasticsearch cluster.

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
api_instance = swagger_client.ClustersKibanaApi()
body = swagger_client.CreateKibanaClusterRequest() # CreateKibanaClusterRequest | The cluster definition
validate_only = false # bool | If true, will just validate the cluster definition but will not perform the creation (optional) (default to false)

try: 
    # Create cluster
    api_response = api_instance.create_kibana_cluster(body, validate_only=validate_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersKibanaApi->create_kibana_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateKibanaClusterRequest**](CreateKibanaClusterRequest.md)| The cluster definition | 
 **validate_only** | **bool**| If true, will just validate the cluster definition but will not perform the creation | [optional] [default to false]

### Return type

[**ClusterCrudResponse**](ClusterCrudResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_kibana_cluster**
> EmptyResponse delete_kibana_cluster(cluster_id)

Delete cluster

Deletes a Kibana cluster. Requires that you have already successfully issued `_shutdown` command against the cluster.

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
api_instance = swagger_client.ClustersKibanaApi()
cluster_id = 'cluster_id_example' # str | Identifier for the Kibana cluster

try: 
    # Delete cluster
    api_response = api_instance.delete_kibana_cluster(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersKibanaApi->delete_kibana_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| Identifier for the Kibana cluster | 

### Return type

[**EmptyResponse**](EmptyResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kibana_cluster**
> KibanaClusterInfo get_kibana_cluster(cluster_id, show_metadata=show_metadata, show_plans=show_plans, show_plan_logs=show_plan_logs, show_plan_defaults=show_plan_defaults)

Get cluster

Retrieves cluster information for a Kibana cluster.

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
api_instance = swagger_client.ClustersKibanaApi()
cluster_id = 'cluster_id_example' # str | Identifier for the Kibana cluster
show_metadata = false # bool | Whether to include the full cluster metadata in the response - can be large per cluster and also include credentials (optional) (default to false)
show_plans = true # bool | Whether to include the full current and pending plan information in the response - can be large per cluster (optional) (default to true)
show_plan_logs = false # bool | Whether to include with the current and pending plan information the attempt log - can be very large per cluster (optional) (default to false)
show_plan_defaults = false # bool | If showing plans, whether to show values that are left at their default value (less readable but more informative) (optional) (default to false)

try: 
    # Get cluster
    api_response = api_instance.get_kibana_cluster(cluster_id, show_metadata=show_metadata, show_plans=show_plans, show_plan_logs=show_plan_logs, show_plan_defaults=show_plan_defaults)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersKibanaApi->get_kibana_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| Identifier for the Kibana cluster | 
 **show_metadata** | **bool**| Whether to include the full cluster metadata in the response - can be large per cluster and also include credentials | [optional] [default to false]
 **show_plans** | **bool**| Whether to include the full current and pending plan information in the response - can be large per cluster | [optional] [default to true]
 **show_plan_logs** | **bool**| Whether to include with the current and pending plan information the attempt log - can be very large per cluster | [optional] [default to false]
 **show_plan_defaults** | **bool**| If showing plans, whether to show values that are left at their default value (less readable but more informative) | [optional] [default to false]

### Return type

[**KibanaClusterInfo**](KibanaClusterInfo.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kibana_cluster_metadata_raw**
> object get_kibana_cluster_metadata_raw(cluster_id)

Get cluster metadata

Advanced use only: Retrieves the internal cluster metadata for a Kibana cluster as free-form JSON.

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
api_instance = swagger_client.ClustersKibanaApi()
cluster_id = 'cluster_id_example' # str | Identifier for the Kibana cluster

try: 
    # Get cluster metadata
    api_response = api_instance.get_kibana_cluster_metadata_raw(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersKibanaApi->get_kibana_cluster_metadata_raw: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| Identifier for the Kibana cluster | 

### Return type

**object**

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kibana_cluster_metadata_settings**
> ClusterMetadataSettings get_kibana_cluster_metadata_settings(cluster_id)

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
api_instance = swagger_client.ClustersKibanaApi()
cluster_id = 'cluster_id_example' # str | Identifier for the Kibana cluster

try: 
    # Get cluster metadata settings
    api_response = api_instance.get_kibana_cluster_metadata_settings(cluster_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersKibanaApi->get_kibana_cluster_metadata_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| Identifier for the Kibana cluster | 

### Return type

[**ClusterMetadataSettings**](ClusterMetadataSettings.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kibana_cluster_pending_plan**
> KibanaClusterPlan get_kibana_cluster_pending_plan(cluster_id, show_plan_defaults=show_plan_defaults)

Get pending plan

Retrieves the pending plan of a Kibana cluster.

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
api_instance = swagger_client.ClustersKibanaApi()
cluster_id = 'cluster_id_example' # str | Identifier for the Kibana cluster
show_plan_defaults = false # bool | Whether to show values that are left at their default value (less readable but more informative) (optional) (default to false)

try: 
    # Get pending plan
    api_response = api_instance.get_kibana_cluster_pending_plan(cluster_id, show_plan_defaults=show_plan_defaults)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersKibanaApi->get_kibana_cluster_pending_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| Identifier for the Kibana cluster | 
 **show_plan_defaults** | **bool**| Whether to show values that are left at their default value (less readable but more informative) | [optional] [default to false]

### Return type

[**KibanaClusterPlan**](KibanaClusterPlan.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kibana_cluster_plan**
> KibanaClusterPlan get_kibana_cluster_plan(cluster_id, show_plan_defaults=show_plan_defaults)

Get plan

Retrieves the active plan of a Kibana cluster.

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
api_instance = swagger_client.ClustersKibanaApi()
cluster_id = 'cluster_id_example' # str | Identifier for the Kibana cluster
show_plan_defaults = false # bool | Whether to show values that are left at their default value (less readable but more informative) (optional) (default to false)

try: 
    # Get plan
    api_response = api_instance.get_kibana_cluster_plan(cluster_id, show_plan_defaults=show_plan_defaults)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersKibanaApi->get_kibana_cluster_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| Identifier for the Kibana cluster | 
 **show_plan_defaults** | **bool**| Whether to show values that are left at their default value (less readable but more informative) | [optional] [default to false]

### Return type

[**KibanaClusterPlan**](KibanaClusterPlan.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kibana_cluster_plan_activity**
> KibanaClusterPlansInfo get_kibana_cluster_plan_activity(cluster_id, show_plan_logs=show_plan_logs, show_plan_defaults=show_plan_defaults)

Get plan activity

Retrieves the current and historical plan information for a Kibana cluster.

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
api_instance = swagger_client.ClustersKibanaApi()
cluster_id = 'cluster_id_example' # str | Identifier for the Kibana cluster
show_plan_logs = true # bool | Whether to include with the current/pending/historical plan information the attempt log - can be very large per cluster (optional) (default to true)
show_plan_defaults = false # bool | Whether to show values that are left at their default value (less readable but more informative) (optional) (default to false)

try: 
    # Get plan activity
    api_response = api_instance.get_kibana_cluster_plan_activity(cluster_id, show_plan_logs=show_plan_logs, show_plan_defaults=show_plan_defaults)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersKibanaApi->get_kibana_cluster_plan_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| Identifier for the Kibana cluster | 
 **show_plan_logs** | **bool**| Whether to include with the current/pending/historical plan information the attempt log - can be very large per cluster | [optional] [default to true]
 **show_plan_defaults** | **bool**| Whether to show values that are left at their default value (less readable but more informative) | [optional] [default to false]

### Return type

[**KibanaClusterPlansInfo**](KibanaClusterPlansInfo.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_kibana_clusters**
> KibanaClustersInfo get_kibana_clusters(_from=_from, size=size, show_metadata=show_metadata, show_plans=show_plans, show_hidden=show_hidden, show_plan_defaults=show_plan_defaults)

Get clusters

Retrieves cluster information for all Kibana clusters.

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
api_instance = swagger_client.ClustersKibanaApi()
_from = 0 # int | The number of clusters to skip over (optional) (default to 0)
size = 100 # int | The maximum number of clusters to return (set to -1 for all clusters - use with care, can result in large responses) (optional) (default to 100)
show_metadata = false # bool | Whether to include the full cluster metadata in the response - can be large per cluster and also include credentials (optional) (default to false)
show_plans = true # bool | Whether to include the full current and pending plan information in the response - can be large per cluster (optional)
show_hidden = false # bool | Whether to include hidden clusters in the response or not (optional) (default to false)
show_plan_defaults = false # bool | If showing plans, whether to show values that are left at their default value (less readable but more informative) (optional) (default to false)

try: 
    # Get clusters
    api_response = api_instance.get_kibana_clusters(_from=_from, size=size, show_metadata=show_metadata, show_plans=show_plans, show_hidden=show_hidden, show_plan_defaults=show_plan_defaults)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersKibanaApi->get_kibana_clusters: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **_from** | **int**| The number of clusters to skip over | [optional] [default to 0]
 **size** | **int**| The maximum number of clusters to return (set to -1 for all clusters - use with care, can result in large responses) | [optional] [default to 100]
 **show_metadata** | **bool**| Whether to include the full cluster metadata in the response - can be large per cluster and also include credentials | [optional] [default to false]
 **show_plans** | **bool**| Whether to include the full current and pending plan information in the response - can be large per cluster | [optional] 
 **show_hidden** | **bool**| Whether to include hidden clusters in the response or not | [optional] [default to false]
 **show_plan_defaults** | **bool**| If showing plans, whether to show values that are left at their default value (less readable but more informative) | [optional] [default to false]

### Return type

[**KibanaClustersInfo**](KibanaClustersInfo.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_kibana_cluster_instances**
> EmptyResponse move_kibana_cluster_instances(cluster_id, instance_ids, body=body, ignore_missing=ignore_missing, force_update=force_update, validate_only=validate_only)

Move instances

Moves one or more instances belonging to a Kibana cluster

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
api_instance = swagger_client.ClustersKibanaApi()
cluster_id = 'cluster_id_example' # str | Identifier for the Kibana cluster
instance_ids = ['instance_ids_example'] # list[str] | Optional comma-delimited list of instance identifiers of the Kibana cluster, otherwise will apply to all instances
body = swagger_client.TransientKibanaPlanConfiguration() # TransientKibanaPlanConfiguration | Overrides defaults for the move, including setting the configuration of instances specified in the path (optional)
ignore_missing = false # bool | If true and the instance does not exist then quietly proceed to the next instance, otherwise treated as an error (optional) (default to false)
force_update = false # bool | If true, will cancel any pending plans and overwrite with this move plan, else will error (optional) (default to false)
validate_only = false # bool | If true, will validate the move request and return the calculated plan without actually applying it. (optional) (default to false)

try: 
    # Move instances
    api_response = api_instance.move_kibana_cluster_instances(cluster_id, instance_ids, body=body, ignore_missing=ignore_missing, force_update=force_update, validate_only=validate_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersKibanaApi->move_kibana_cluster_instances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| Identifier for the Kibana cluster | 
 **instance_ids** | [**list[str]**](str.md)| Optional comma-delimited list of instance identifiers of the Kibana cluster, otherwise will apply to all instances | 
 **body** | [**TransientKibanaPlanConfiguration**](TransientKibanaPlanConfiguration.md)| Overrides defaults for the move, including setting the configuration of instances specified in the path | [optional] 
 **ignore_missing** | **bool**| If true and the instance does not exist then quietly proceed to the next instance, otherwise treated as an error | [optional] [default to false]
 **force_update** | **bool**| If true, will cancel any pending plans and overwrite with this move plan, else will error | [optional] [default to false]
 **validate_only** | **bool**| If true, will validate the move request and return the calculated plan without actually applying it. | [optional] [default to false]

### Return type

[**EmptyResponse**](EmptyResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **move_kibana_cluster_instances_advanced**
> ClusterCommandResponse move_kibana_cluster_instances_advanced(body, cluster_id, ignore_missing=ignore_missing, force_update=force_update, validate_only=validate_only)

Move instances (advanced)

Moves one or more instances belonging to a Kibana cluster, with custom configuration posted in the body

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
api_instance = swagger_client.ClustersKibanaApi()
body = swagger_client.TransientKibanaPlanConfiguration() # TransientKibanaPlanConfiguration | Overrides defaults for the move, including setting the configuration of instances specified in the path
cluster_id = 'cluster_id_example' # str | Identifier for the Kibana cluster
ignore_missing = false # bool | If true and the instance does not exist then quietly proceed to the next instance, otherwise treated as an error (optional) (default to false)
force_update = false # bool | If true, will cancel any pending plans and overwrite with this move plan, else will error (optional) (default to false)
validate_only = false # bool | If true, will validate the move request and return the calculated plan without actually applying it. (optional) (default to false)

try: 
    # Move instances (advanced)
    api_response = api_instance.move_kibana_cluster_instances_advanced(body, cluster_id, ignore_missing=ignore_missing, force_update=force_update, validate_only=validate_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersKibanaApi->move_kibana_cluster_instances_advanced: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**TransientKibanaPlanConfiguration**](TransientKibanaPlanConfiguration.md)| Overrides defaults for the move, including setting the configuration of instances specified in the path | 
 **cluster_id** | **str**| Identifier for the Kibana cluster | 
 **ignore_missing** | **bool**| If true and the instance does not exist then quietly proceed to the next instance, otherwise treated as an error | [optional] [default to false]
 **force_update** | **bool**| If true, will cancel any pending plans and overwrite with this move plan, else will error | [optional] [default to false]
 **validate_only** | **bool**| If true, will validate the move request and return the calculated plan without actually applying it. | [optional] [default to false]

### Return type

[**ClusterCommandResponse**](ClusterCommandResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **restart_kibana_cluster**
> ClusterCommandResponse restart_kibana_cluster(cluster_id, cancel_pending=cancel_pending)

Restart cluster

Restarts a Kibana cluster. If a cluster is active: this command re-applies the existing plan but applies a \"cluster_reboot\", which issues a Kibana restart command and waits for it to complete. If a cluster is inactive: this command starts it up with the most recent successful plan.

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
api_instance = swagger_client.ClustersKibanaApi()
cluster_id = 'cluster_id_example' # str | Identifier for the Kibana cluster
cancel_pending = false # bool | If true, will cancel any pending plans before restarting (else will error) (optional) (default to false)

try: 
    # Restart cluster
    api_response = api_instance.restart_kibana_cluster(cluster_id, cancel_pending=cancel_pending)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersKibanaApi->restart_kibana_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| Identifier for the Kibana cluster | 
 **cancel_pending** | **bool**| If true, will cancel any pending plans before restarting (else will error) | [optional] [default to false]

### Return type

[**ClusterCommandResponse**](ClusterCommandResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_kibana_cluster_metadata_raw**
> object set_kibana_cluster_metadata_raw(cluster_id, body, version=version)

Set cluster metadata

Advanced use only: Sets the internal cluster metadata for a Kibana cluster with free-form JSON. Must only be used to set a modified version of the JSON returned from the get version of the metadata.

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
api_instance = swagger_client.ClustersKibanaApi()
cluster_id = 'cluster_id_example' # str | Identifier for the Kibana cluster
body = 'body_example' # str | The freeform JSON for the cluster (should always be based on the current version retrieved from the GET)
version = 56 # int | If specified then checks for conflicts against the version of the cluster metadata (returned in 'x-cloud-resource-version' of the GET request) (optional)

try: 
    # Set cluster metadata
    api_response = api_instance.set_kibana_cluster_metadata_raw(cluster_id, body, version=version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersKibanaApi->set_kibana_cluster_metadata_raw: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| Identifier for the Kibana cluster | 
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

# **set_kibana_cluster_name**
> EmptyResponse set_kibana_cluster_name(cluster_id, new_name)

Set cluster name

Sets the name of a Kibana cluster.

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
api_instance = swagger_client.ClustersKibanaApi()
cluster_id = 'cluster_id_example' # str | Identifier for the Kibana cluster
new_name = 'new_name_example' # str | The new name for the cluster

try: 
    # Set cluster name
    api_response = api_instance.set_kibana_cluster_name(cluster_id, new_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersKibanaApi->set_kibana_cluster_name: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| Identifier for the Kibana cluster | 
 **new_name** | **str**| The new name for the cluster | 

### Return type

[**EmptyResponse**](EmptyResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shutdown_kibana_cluster**
> ClusterCommandResponse shutdown_kibana_cluster(cluster_id, hide=hide)

Shut down cluster

Shuts down a running cluster and removes all nodes belonging to the cluster. The cluster definition is retained. Warning: this will lose all cluster data that is not saved in a snapshot repository.

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
api_instance = swagger_client.ClustersKibanaApi()
cluster_id = 'cluster_id_example' # str | Identifier for the Kibana cluster
hide = false # bool | Hide cluster on shutdown. Hidden clusters are not listed by default. (optional) (default to false)

try: 
    # Shut down cluster
    api_response = api_instance.shutdown_kibana_cluster(cluster_id, hide=hide)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersKibanaApi->shutdown_kibana_cluster: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| Identifier for the Kibana cluster | 
 **hide** | **bool**| Hide cluster on shutdown. Hidden clusters are not listed by default. | [optional] [default to false]

### Return type

[**ClusterCommandResponse**](ClusterCommandResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_kibana_cluster_instances**
> ClusterCommandResponse start_kibana_cluster_instances(cluster_id, instance_ids, ignore_missing=ignore_missing)

Start instances

Starts the instances belonging to a Kibana cluster.

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
api_instance = swagger_client.ClustersKibanaApi()
cluster_id = 'cluster_id_example' # str | Identifier for the Kibana cluster
instance_ids = ['instance_ids_example'] # list[str] | Optional comma-delimited list of instance identifiers of the Kibana cluster, otherwise will apply to all instances
ignore_missing = false # bool | If true and the instance does not exist then quietly proceed to the next instance, otherwise treated as an error (optional) (default to false)

try: 
    # Start instances
    api_response = api_instance.start_kibana_cluster_instances(cluster_id, instance_ids, ignore_missing=ignore_missing)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersKibanaApi->start_kibana_cluster_instances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| Identifier for the Kibana cluster | 
 **instance_ids** | [**list[str]**](str.md)| Optional comma-delimited list of instance identifiers of the Kibana cluster, otherwise will apply to all instances | 
 **ignore_missing** | **bool**| If true and the instance does not exist then quietly proceed to the next instance, otherwise treated as an error | [optional] [default to false]

### Return type

[**ClusterCommandResponse**](ClusterCommandResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **start_kibana_cluster_maintenance_mode**
> ClusterCommandResponse start_kibana_cluster_maintenance_mode(cluster_id, instance_ids, ignore_missing=ignore_missing)

Start maintenance mode

Starts maintenance mode of instances belonging to a Kibana cluster.

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
api_instance = swagger_client.ClustersKibanaApi()
cluster_id = 'cluster_id_example' # str | Identifier for the Kibana cluster
instance_ids = ['instance_ids_example'] # list[str] | Optional comma-delimited list of instance identifiers of the Kibana cluster, otherwise will apply to all instances
ignore_missing = false # bool | If true and the instance does not exist then quietly proceed to the next instance, otherwise treated as an error (optional) (default to false)

try: 
    # Start maintenance mode
    api_response = api_instance.start_kibana_cluster_maintenance_mode(cluster_id, instance_ids, ignore_missing=ignore_missing)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersKibanaApi->start_kibana_cluster_maintenance_mode: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| Identifier for the Kibana cluster | 
 **instance_ids** | [**list[str]**](str.md)| Optional comma-delimited list of instance identifiers of the Kibana cluster, otherwise will apply to all instances | 
 **ignore_missing** | **bool**| If true and the instance does not exist then quietly proceed to the next instance, otherwise treated as an error | [optional] [default to false]

### Return type

[**ClusterCommandResponse**](ClusterCommandResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_kibana_cluster_instances**
> ClusterCommandResponse stop_kibana_cluster_instances(cluster_id, instance_ids, ignore_missing=ignore_missing)

Stop instances

Stops the instances belonging to a Kibana cluster.

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
api_instance = swagger_client.ClustersKibanaApi()
cluster_id = 'cluster_id_example' # str | Identifier for the Kibana cluster
instance_ids = ['instance_ids_example'] # list[str] | Optional comma-delimited list of instance identifiers of the Kibana cluster, otherwise will apply to all instances
ignore_missing = false # bool | If true and the instance does not exist then quietly proceed to the next instance, otherwise treated as an error (optional) (default to false)

try: 
    # Stop instances
    api_response = api_instance.stop_kibana_cluster_instances(cluster_id, instance_ids, ignore_missing=ignore_missing)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersKibanaApi->stop_kibana_cluster_instances: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| Identifier for the Kibana cluster | 
 **instance_ids** | [**list[str]**](str.md)| Optional comma-delimited list of instance identifiers of the Kibana cluster, otherwise will apply to all instances | 
 **ignore_missing** | **bool**| If true and the instance does not exist then quietly proceed to the next instance, otherwise treated as an error | [optional] [default to false]

### Return type

[**ClusterCommandResponse**](ClusterCommandResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **stop_kibana_cluster_maintenance_mode**
> ClusterCommandResponse stop_kibana_cluster_maintenance_mode(cluster_id, instance_ids, ignore_missing=ignore_missing)

Stop maintenance mode

Stops maintenance mode of instances belonging to a Kibana cluster.

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
api_instance = swagger_client.ClustersKibanaApi()
cluster_id = 'cluster_id_example' # str | Identifier for the Kibana cluster
instance_ids = ['instance_ids_example'] # list[str] | Optional comma-delimited list of instance identifiers of the Kibana cluster, otherwise will apply to all instances
ignore_missing = false # bool | If true and the instance does not exist then quietly proceed to the next instance, otherwise treated as an error (optional) (default to false)

try: 
    # Stop maintenance mode
    api_response = api_instance.stop_kibana_cluster_maintenance_mode(cluster_id, instance_ids, ignore_missing=ignore_missing)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersKibanaApi->stop_kibana_cluster_maintenance_mode: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| Identifier for the Kibana cluster | 
 **instance_ids** | [**list[str]**](str.md)| Optional comma-delimited list of instance identifiers of the Kibana cluster, otherwise will apply to all instances | 
 **ignore_missing** | **bool**| If true and the instance does not exist then quietly proceed to the next instance, otherwise treated as an error | [optional] [default to false]

### Return type

[**ClusterCommandResponse**](ClusterCommandResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_kibana_cluster_metadata_settings**
> ClusterMetadataSettings update_kibana_cluster_metadata_settings(cluster_id, body, version=version)

Update cluster metadata settings

Any changes in the PATCHed object will be applied to the metadata object.  PATCHing existing fields will cause same values to be re-applied.PATCHing a value of 'null' will cause the field to be reverted to it's default value or removed if no default value exists

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
api_instance = swagger_client.ClustersKibanaApi()
cluster_id = 'cluster_id_example' # str | Identifier for the Kibana cluster
body = swagger_client.ClusterMetadataSettings() # ClusterMetadataSettings | The cluster settings including updated values
version = 56 # int | If specified then checks for conflicts against the version of the cluster metadata (returned in 'x-cloud-resource-version' of the GET request) (optional)

try: 
    # Update cluster metadata settings
    api_response = api_instance.update_kibana_cluster_metadata_settings(cluster_id, body, version=version)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersKibanaApi->update_kibana_cluster_metadata_settings: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **cluster_id** | **str**| Identifier for the Kibana cluster | 
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

# **update_kibana_cluster_plan**
> ClusterCrudResponse update_kibana_cluster_plan(body, cluster_id, validate_only=validate_only)

Update plan

Updates the configuration of an existing Kibana cluster.

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
api_instance = swagger_client.ClustersKibanaApi()
body = swagger_client.KibanaClusterPlan() # KibanaClusterPlan | The update plan definition
cluster_id = 'cluster_id_example' # str | Identifier for the Kibana cluster
validate_only = false # bool | If true, will just validate the cluster definition but will not perform the update (optional) (default to false)

try: 
    # Update plan
    api_response = api_instance.update_kibana_cluster_plan(body, cluster_id, validate_only=validate_only)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClustersKibanaApi->update_kibana_cluster_plan: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**KibanaClusterPlan**](KibanaClusterPlan.md)| The update plan definition | 
 **cluster_id** | **str**| Identifier for the Kibana cluster | 
 **validate_only** | **bool**| If true, will just validate the cluster definition but will not perform the update | [optional] [default to false]

### Return type

[**ClusterCrudResponse**](ClusterCrudResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

