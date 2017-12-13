# ClusterInstanceInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance_name** | **str** | Whether the instance is healthy (ie started and running) | 
**service_version** | **str** | The version of the service that the instance is running (eg Elasticsearch or Kibana), if available | [optional] 
**service_id** | **str** | The service-specific (eg Elasticsearch) id of the node, if available | [optional] 
**healthy** | **bool** | Whether the instance is healthy (ie started and running) | 
**container_started** | **bool** | Whether the container has started (does not tell you anything about the service -ie Elasticsearch- running inside the container) | 
**service_running** | **bool** | Whether the service launched inside the container -ie Elasticsearch- is actually running | 
**maintenance_mode** | **bool** | Whether the service is is maintenance mode (meaning that the proxy is not routing external traffic to it) | 
**zone** | **str** | The zone in which this instance is being allocated | [optional] 
**allocator_id** | **str** | The id of the allocator on which this instance is running (if the container is started or starting) | [optional] 
**memory** | [**ClusterInstanceMemoryInfo**](ClusterInstanceMemoryInfo.md) |  | [optional] 
**disk** | [**ClusterInstanceDiskInfo**](ClusterInstanceDiskInfo.md) |  | [optional] 
**service_roles** | **list[str]** | List of roles assigned to the service running in the instance. Currently only populated for Elasticsearch, with possible values: master,data,ingest | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


