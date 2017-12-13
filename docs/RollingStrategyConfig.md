# RollingStrategyConfig

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group_by** | **str** | Specifies the grouping attribute to use when rolling several instances. Instances that share the same value for the provided attribute key are rolled together as a unit. Examples that make sense to use are &#39;\\_\\_all\\_\\_&#39; (roll all instances as a single unit), &#39;logical_zone_name&#39; (roll instances by zone), &#39;\\_\\_name\\_\\_&#39; (roll one instance at a time, the default if not specified). Note that &#39;\\_\\_all\\_\\_&#39; is required when performing a major version upgrade | [optional] 
**allow_inline_resize** | **bool** | Whether we allow changing the capacity of instances (default false). This is currently implemented by stopping, re-creating then starting the affected instance on its associated allocator when performing the changes. NOTES: This requires a round-trip through the allocation infrastructure of the active constructor, as it has to reserve the target capacity without over-committing | [optional] 
**skip_synced_flush** | **bool** | Whether to skip attempting to do a synced flush on the filesystem of the container (default: false), which is less safe but may be required if the container is unhealthy | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


