# ClusterCrudResponse

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**elasticsearch_cluster_id** | **str** | For an operation creating or updating an Elasticsearch cluster, the Id of that cluster | [optional] 
**kibana_cluster_id** | **str** | For an operation creating or updating a Kibana cluster, the Id of that cluster | [optional] 
**credentials** | [**ClusterCredentials**](ClusterCredentials.md) |  | [optional] 
**diagnostics** | **object** | If the endpoint is called with URL param &#39;validate_only&#x3D;true&#39;, then this contains advanced debug info (the internal plan representation) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


