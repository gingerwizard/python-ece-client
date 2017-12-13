# SnapshotStatusInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**healthy** | **bool** | Health status of snapshots for this cluster | 
**count** | **int** | Number of snapshots stored for this cluster | 
**latest_successful** | **bool** | Latest snapshot status | [optional] 
**latest_status** | **str** | Status of the latest snapshot attempt, if any exist. | [optional] 
**scheduled_time** | **datetime** | Scheduled time of next snapshot attempt | [optional] 
**latest_end_time** | **datetime** | The end time of the most recently attempted snapshot | [optional] 
**latest_successful_end_time** | **datetime** | The end time of the most recently successful snapshot | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


