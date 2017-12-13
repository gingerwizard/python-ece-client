# RestoreSnapshotApiConfiguration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**indices** | **list[str]** | The list of indices to restore (supports +ve and -ve selection and wildcarding - see the default Elasticsearch index format documentation) | [optional] 
**raw_settings** | **object** | This JSON object (merged with the &#39;indices&#39; field (if present) is passed untouched into the restore command - see the Elasticsearch &#39;_snapshot&#39; documentation for more details on supported formats | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


