# ElasticsearchClusterPlan

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**zone_count** | **int** | The default number of zones in which data nodes will be placed, if not specified in the per topology settings | [optional] 
**tiebreaker_override** | **bool** | Whether to add a tiebreaker node in an unused zone (defaults to auto-decide based on topology). If master nodes are specified then this cannot be left blank, you must explictly decide true or false. | [optional] 
**tiebreaker_topology** | [**TiebreakerTopologyElement**](TiebreakerTopologyElement.md) |  | [optional] 
**cluster_topology** | [**list[ElasticsearchClusterTopologyElement]**](ElasticsearchClusterTopologyElement.md) |  | 
**elasticsearch** | [**ElasticsearchConfiguration**](ElasticsearchConfiguration.md) |  | 
**transient** | [**TransientElasticsearchPlanConfiguration**](TransientElasticsearchPlanConfiguration.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


