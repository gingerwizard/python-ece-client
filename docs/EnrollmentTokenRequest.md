# EnrollmentTokenRequest

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**roles** | **list[str]** | The additional services for which this enrollment token applies (empty if not specified, ie system services only) | [optional] 
**persistent** | **bool** | Whether this token can subsequently to its grant be revoked from the UI | 
**validity_in_seconds** | **int** | The time in seconds for which this token is valid (defaults to 1 hour). Currently this can only be set for ephemeral (persistent: false) tokens. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


