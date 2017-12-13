# ElasticsearchPlanControlConfiguration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**timeout** | **int** | The total timeout in seconds after which the plan is cancelled even if it is not complete. Defaults to 4x the max memory capacity per node (in MB). NOTES: (eg a 3 zone cluster with 2 nodes of 2048 each would have a timeout of 4*2048&#x3D;8192 seconds) | [optional] 
**calm_wait_time** | **int** | This timeout determines how long to give a cluster after it responds to API calls before performing actual operations on it. It defaults to 5s | [optional] 
**move_instances** | [**list[InstanceMoveRequest]**](InstanceMoveRequest.md) |  | [optional] 
**move_allocators** | [**list[AllocatorMoveRequest]**](AllocatorMoveRequest.md) |  | [optional] 
**reallocate_instances** | **bool** | If true (default: false) does not allow re-using any existing instances currently in the cluster, ie even unchanged instances will be re-created | [optional] 
**preferred_allocators** | **list[str]** | List of allocators on which instances are placed if possible (if not possible/not specified then any available allocator with space is used) | [optional] 
**skip_snapshot** | **bool** | If true (default: false), does not take (or require) a successful snapshot to be taken before performing any potentially destructive changes to this cluster | [optional] 
**max_snapshot_attempts** | **int** | If taking a snapshot (ie unless &#39;skip_snapshots&#39;: true) then will retry on failure at most this number of times (default: 5) | [optional] 
**extended_maintenance** | **bool** | If true (default false), does not clear the maintenance flag (which prevents its API from being accessed except by the constructor) on new instances added until after a snapshot has been restored, otherwise, the maintenance flag is cleared once the new instances successfully join the new cluster | [optional] 
**cluster_reboot** | **str** | Set to &#39;forced&#39; to force a reboot as part of the upgrade plan. NOTES: (ie taking an existing plan and leaving it alone except for setting &#39;transient.plan_configuration.cluster_reboot&#39;: &#39;forced&#39; will reboot the cluster) | [optional] 
**override_failsafe** | **bool** | If false (the default) then the plan will fail out if it believes the requested sequence of operations can result in data loss - this flag will override some of these restraints | [optional] 
**skip_data_migration** | **bool** | If true (default: false) then the plan will not wait for data to be migrated from old instances to new instances before continuing the plan (potentially deleting the old instances and losing data) | [optional] 
**skip_upgrade_checker** | **bool** | If false, the cluster is checked for issues that should be resolved before migration (eg contains old Lucene segments), if true this is bypassed | [optional] 
**skip_post_upgrade_steps** | **bool** | If false (the default), the cluster will run (currently) 2.x-&gt;5.x operations for any plan change ending with a 5.x cluster (eg apply a cluster license, ensure Monitoring is configured) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


