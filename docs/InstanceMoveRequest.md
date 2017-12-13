# InstanceMoveRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**_from** | **str** | The instance id that is going to be moved | 
**to** | **list[str]** | An optional list of allocator ids to which the instance should be moved. If not specified then any available allocator can be used (including the current one if it is healthy) | [optional] 
**instance_down** | **bool** | Tells the infrastructure that the instance should be considered as permanently down when deciding how to migrate data to new nodes. If left blank then the system will automatically decide (currently: will treat the instances as up) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


