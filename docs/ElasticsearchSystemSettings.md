# ElasticsearchSystemSettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scripting** | [**ElasticsearchScriptingUserSettings**](ElasticsearchScriptingUserSettings.md) |  | [optional] 
**reindex_whitelist** | **list[str]** | Limits remote Elasticsearch clusters that can be used as the source for &#39;_reindex&#39; API commands | [optional] 
**use_disk_threshold** | **bool** | Whether to factor in the available disk space on a node before deciding whether to allocate new shards to that node or actively relocate shards away from the node (default: true). NOTES: (Corresponds to the parameter &#39;cluster.routing.allocation.disk.threshold_enabled&#39;) | [optional] 
**auto_create_index** | **bool** | If true (the default), then any write operation on an index that does not currently exist will create it. NOTES: (Corresponds to the parameter &#39;action.auto_create_index&#39;) | [optional] 
**enable_close_index** | **bool** | If false (the default), then the API commands to close indices are disabled. This is important because Elasticsearch does not snapshot or migrate close indices, therefore standard Elastic Cloud configuration operations will cause irretrievable loss of indices&#39; data. NOTES: (Corresponds to the parameter &#39;cluster.indices.close.enable&#39;) | [optional] 
**destructive_requires_name** | **bool** | If true (default is false) then the index deletion API will not support wildcards or &#39;_all&#39;. NOTES: (Corresponds to the parameter &#39;action.destructive_requires_name&#39;) | [optional] 
**watcher_trigger_engine** | **str** | The trigger engine for Watcher, defaults to &#39;scheduler&#39; - see the xpack documentation for more information. NOTES: (Corresponds to the parameter &#39;(xpack.)watcher.trigger.schedule.engine&#39;, depending on version. Ignored from 6.x onwards.) | [optional] 
**default_shards_per_index** | **int** | (2.x only - to get the same result in 5.x template mappings must be used) Sets the default number of shards per index, defaulting to 1 if not specified. (Corresponds to the parameter &#39;index.number_of_shards&#39; in 2.x, not supported in 5.x) | [optional] 
**monitoring_collection_interval** | **int** | The default interval at which monitoring information from the cluster if collected, if monitoring is enabled. NOTES: (Corresponds to the parameter &#39;marvel.agent.interval&#39; in 2.x and &#39;xpack.monitoring.collection.interval&#39; in 5.x) | [optional] 
**monitoring_history_duration** | **str** | The duration for which monitoring history is stored (format &#39;(NUMBER)d&#39; eg &#39;3d&#39; for 3 days). NOTES: (&#39;Corresponds to the parameter xpack.monitoring.history.duration&#39; in 5.x, defaults to &#39;7d&#39;) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


