# ElasticsearchClusterSecurityInfo

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **int** | The resource version number of the security settings | 
**last_modified** | **datetime** | The most recent time the security settings were changed (ISO format in UTC) | 
**allow_anonymous** | **bool** | Whether anonymous access to the cluster is allowed | 
**users** | [**list[ElasticsearchClusterUser]**](ElasticsearchClusterUser.md) |  | 
**roles** | **object** | An arbitrarily nested JSON object mapping roles to sets of resources and permissions - see the Elasticsearch security documentation for more details on roles | 
**users_roles** | [**list[ElasticsearchClusterRole]**](ElasticsearchClusterRole.md) |  | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


