# ElasticsearchScriptingUserSettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**painless_enabled** | **bool** | (5.x+ only) If enabled (the default) then the painless scripting engine is allowed as a sandboxed language. Sandboxed languages are the only ones allowed if &#39;sandbox_mode&#39; is set to true. NOTES: (Corresponds to the parameters &#39;script.engine.painless.[file|stored|inline]&#39;) | [optional] 
**mustache_enabled** | **bool** | (5.x+ only) If enabled (the default) then the mustache scripting engine is allowed as a sandboxed language. Sandboxed languages are the only ones allowed if &#39;sandbox_mode&#39; is set to true. NOTES: (Corresponds to the parameters &#39;script.engine.mustache.[file|stored|inline]&#39;) | [optional] 
**expressions_enabled** | **bool** | (5.x+ only) If enabled (the default) then the expressions scripting engine is allowed as a sandboxed language. Sandboxed languages are the only ones allowed if &#39;sandbox_mode&#39; is set to true. NOTES: (Corresponds to the parameters &#39;script.engine.expression.[file|stored|inline]&#39;) | [optional] 
**stored** | [**ElasticsearchScriptTypeSettings**](ElasticsearchScriptTypeSettings.md) |  | [optional] 
**file** | [**ElasticsearchScriptTypeSettings**](ElasticsearchScriptTypeSettings.md) |  | [optional] 
**inline** | [**ElasticsearchScriptTypeSettings**](ElasticsearchScriptTypeSettings.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


