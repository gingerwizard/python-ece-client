# KibanaClusterInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **str** | The id of the cluster | 
**cluster_name** | **str** | The name of the cluster | 
**elasticsearch_cluster** | [**TargetElasticsearchCluster**](TargetElasticsearchCluster.md) |  | 
**healthy** | **bool** | Whether the cluster is healthy or not (one or more of the info subsections will have healthy: false) | 
**status** | **str** | Cluster status | [optional] 
**plan_info** | [**KibanaClusterPlansInfo**](KibanaClusterPlansInfo.md) |  | 
**metadata** | [**ClusterMetadataInfo**](ClusterMetadataInfo.md) |  | 
**topology** | [**ClusterTopologyInfo**](ClusterTopologyInfo.md) |  | 
**external_links** | [**list[ExternalHyperlink]**](ExternalHyperlink.md) | External resources related to the cluster | 
**links** | [**dict(str, Hyperlink)**](Hyperlink.md) | A map of application-specific operations (which map to &#39;operationId&#39;s in the Swagger API) to metadata about that operation | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


