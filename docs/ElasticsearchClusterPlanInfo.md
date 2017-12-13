# ElasticsearchClusterPlanInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan_attempt_id** | **str** | A UUID for each plan attempt | [optional] 
**plan_attempt_name** | **str** | A human readable name for each plan attempt, only populated when retrieving plan histories | [optional] 
**healthy** | **bool** | Either the plan ended successfully, or is not yet completed (and no errors have occurred) | 
**attempt_start_time** | **datetime** | When this plan attempt (ie to apply the plan to the cluster) started (ISO format in UTC) | 
**attempt_end_time** | **datetime** | If this plan completed or failed (ie is not pending), when the attempt ended (ISO format in UTC) | [optional] 
**plan_end_time** | **datetime** | If this plan is not current or pending, when the plan was no longer active (ISO format in UTC) | [optional] 
**plan** | [**ElasticsearchClusterPlan**](ElasticsearchClusterPlan.md) |  | [optional] 
**plan_attempt_log** | [**list[ClusterPlanStepInfo]**](ClusterPlanStepInfo.md) |  | 
**source** | [**ChangeSourceInfo**](ChangeSourceInfo.md) | Information describing the source that facilitated the plans current state | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


