# AllocatorMoveRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_from** | **str** | The allocator id off which all instances in the cluster should be moved | 
**to** | **list[str]** | An optional list of allocator ids to which the instance(s) should be moved. If not specified then any available allocator can be used (including the current one if it is healthy) | [optional] 
**allocator_down** | **bool** | Tells the infrastructure that all instances on the allocator should be considered as permanently down when deciding how to migrate data to new nodes. If left blank then the system will auto-decide (currently: will treat the allocator as up) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


