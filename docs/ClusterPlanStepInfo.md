# ClusterPlanStepInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**step_id** | **str** | ID of current step | 
**started** | **datetime** | When the step started (ISO format in UTC) | 
**completed** | **datetime** | When the step completed (ISO format in UTC) | [optional] 
**duration_in_millis** | **int** | The duration of the step in MS | [optional] 
**status** | **str** | The status of the step (success, warning, error - warning means something didn&#39;t go as expected but it was not serious enough to abort the plan) | 
**stage** | **str** | Current stage that the step is in | 
**info_log** | [**list[ClusterPlanStepLogMessageInfo]**](ClusterPlanStepLogMessageInfo.md) | Human readable summaries of the step, including messages for each stage of the step | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


