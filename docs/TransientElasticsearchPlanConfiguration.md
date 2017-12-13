# TransientElasticsearchPlanConfiguration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**strategy** | [**PlanStrategy**](PlanStrategy.md) |  | [optional] 
**plan_configuration** | [**ElasticsearchPlanControlConfiguration**](ElasticsearchPlanControlConfiguration.md) |  | [optional] 
**restore_snapshot** | [**RestoreSnapshotConfiguration**](RestoreSnapshotConfiguration.md) |  | [optional] 
**cluster_settings_json** | **object** | If specified, contains transient settings to be applied to an Elasticsearch cluster during changes, with the following default values applied. - indices.store.throttle.max_bytes_per_sec: 150Mb - indices.recovery.max_bytes_per_sec: 150Mb - cluster.routing.allocation.cluster_concurrent_rebalance: 10 - cluster.routing.allocation.node_initial_primaries_recoveries: 8 These can be overridden by specifying them in the map. Additional settings can also be set. Settings will be cleared after the plan has finished. If not specified, no settings will be applied. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


