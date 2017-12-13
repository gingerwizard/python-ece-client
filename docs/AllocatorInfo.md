# AllocatorInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | [**AllocatorHealthStatus**](AllocatorHealthStatus.md) |  | [optional] 
**allocator_id** | **str** | Identifier for this allocator | [optional] 
**zone_id** | **str** | Identifier of the zone | [optional] 
**host_ip** | **str** | Host IP of this allocator | [optional] 
**public_hostname** | **str** | Public hostname of this allocator | [optional] 
**capacity** | [**AllocatorCapacity**](AllocatorCapacity.md) |  | [optional] 
**settings** | [**AllocatorSettings**](AllocatorSettings.md) |  | [optional] 
**instances** | [**list[AllocatedInstanceStatus]**](AllocatedInstanceStatus.md) |  | [optional] 
**metadata** | [**list[AllocatorMetadataItem]**](AllocatorMetadataItem.md) | Arbitrary metadata associated with this allocator | [optional] 
**features** | **list[str]** | List of features associated with this allocator. Note this is only present for backwards compatibility purposes and is scheduled for removal in the next major version release. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


