# ElasticsearchClusterTopologyElement

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**node_type** | [**ElasticsearchNodeType**](ElasticsearchNodeType.md) |  | [optional] 
**memory_per_node** | **int** | The memory capacity in MB for each node of this type built in each zone. NOTES: (Only powers of 2 starting with 1024 are supported. Will fail to allocate if too much memory is requested - use &#39;node_count_per_zone&#39; in that case to split the cluster up within a zone) | 
**node_count_per_zone** | **int** | The number of nodes of this type that are allocated within each zone. NOTES: (ie total capacity per zone &#x3D; &#39;node_count_per_zone&#39; * &#39;memory_per_node&#39; in MB). Cannot be set for tiebreaker topologies. For dedicated master nodes, must be 1 if an entry exists | 
**zone_count** | **int** | The default number of zones in which data nodes will be placed | [optional] 
**elasticsearch** | [**ElasticsearchConfiguration**](ElasticsearchConfiguration.md) |  | [optional] 
**allocator_filter** | **object** | DEPRECATED: Controls the allocation strategy of this node type using a simplified version of the Elasticsearch filter DSL (together with &#39;node_configuration&#39;) | [optional] 
**node_configuration** | **str** | Controls the allocation strategy of this node type by pointing to the names of pre-registered allocator settings. Unless otherwise specified for this deployment, only &#39;default&#39; is supported (equivalent to omitting). | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


