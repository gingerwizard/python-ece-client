# ElasticsearchClusterInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **str** | The id of the cluster | 
**cluster_name** | **str** | The name of the cluster | 
**healthy** | **bool** | Whether the cluster is healthy or not (one or more of the info subsections will have healthy: false) | 
**status** | **str** | Cluster status | [optional] 
**plan_info** | [**ElasticsearchClusterPlansInfo**](ElasticsearchClusterPlansInfo.md) |  | 
**elasticsearch** | [**ElasticsearchInfo**](ElasticsearchInfo.md) |  | 
**metadata** | [**ClusterMetadataInfo**](ClusterMetadataInfo.md) |  | 
**topology** | [**ClusterTopologyInfo**](ClusterTopologyInfo.md) |  | 
**system_alerts** | [**list[ClusterSystemAlert]**](ClusterSystemAlert.md) | List of cluster system alerts | [optional] 
**associated_kibana_clusters** | [**list[KibanaSubClusterInfo]**](KibanaSubClusterInfo.md) |  | 
**security** | [**ElasticsearchClusterSecurityInfo**](ElasticsearchClusterSecurityInfo.md) |  | [optional] 
**elasticsearch_monitoring_info** | [**ElasticsearchMonitoringInfo**](ElasticsearchMonitoringInfo.md) |  | [optional] 
**snapshots** | [**SnapshotStatusInfo**](SnapshotStatusInfo.md) |  | 
**external_links** | [**list[ExternalHyperlink]**](ExternalHyperlink.md) | External resources related to the cluster | 
**links** | [**dict(str, Hyperlink)**](Hyperlink.md) | A map of application-specific operations (which map to &#39;operationId&#39;s in the Swagger API) to metadata about that operation | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


