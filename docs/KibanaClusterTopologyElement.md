# KibanaClusterTopologyElement

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**memory_per_node** | **int** | The memory capacity in MB for each node of this type built in each zone | 
**node_count_per_zone** | **int** | The number of nodes of this type that are allocated within each zone | 
**allocator_filter** | **object** | DEPRECATED: Controls the allocation strategy of this node type using a simplified version of the Elasticsearch filter DSL (together with &#39;node_configuration&#39;) | [optional] 
**node_configuration** | **str** | Controls the allocation strategy of this node type by pointing to the names of pre-registered allocator settings. Unless otherwise specified for this deployment, should be omitted. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


