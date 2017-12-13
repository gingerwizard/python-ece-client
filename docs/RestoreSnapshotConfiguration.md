# RestoreSnapshotConfiguration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repository_name** | **str** | If specified, contains the name of the snapshot repository - else will default to the Elastic Cloud system repo (&#39;found-snapshots&#39;) | [optional] 
**snapshot_name** | **str** | The name of the snapshot to restore. Use &#39;\\_\\_latest_success\\_\\_&#39; to get the most recent snapshot from the specified repository | 
**repository_config** | [**RestoreSnapshotRepoConfiguration**](RestoreSnapshotRepoConfiguration.md) |  | [optional] 
**restore_payload** | [**RestoreSnapshotApiConfiguration**](RestoreSnapshotApiConfiguration.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


