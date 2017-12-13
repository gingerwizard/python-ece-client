# ElasticsearchScriptTypeSettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool** | If enabled (default: true) then scripts are enabled, either for sandboxing languages (by default), or for all installed languages if &#39;sandbox_mode&#39; is disabled (or for 6.x). NOTES: (Corresponds to the parameter &#39;script.file|stored/indexed|inline&#39;) | [optional] 
**sandbox_mode** | **bool** | If enabled (default: true) and this script type is enabled, then only the sandbox languages are allowed. By default the sandbox languages are painless, expressions and mustache, but this can be restricted via the &#39;painless_enabled&#39;, &#39;mustache_enabled&#39; &#39;expression_enabled&#39; settings.NOTES: Not supported in 6.x. (Corresponds to the parameters &#39;script.engine.[painless|mustache|expressions].[file|stored|inline]&#39;) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


