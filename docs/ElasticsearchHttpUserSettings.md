# ElasticsearchHttpUserSettings

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**compression** | **bool** | Controls whether HTTP API responses are compressed (default: true). NOTES: (Corresponds to the parameter &#39;http.compression&#39;) | [optional] 
**cors_enabled** | **bool** | Enables or disables (default is disabled) CORS support - see CORS documentation. NOTES: (Corresponds to the parameter &#39;http.cors.enabled&#39;) | [optional] 
**cors_allow_origin** | **str** | Which origins to allow. Defaults to no origins allowed. If you prepend and append a / to the value, this will be treated as a regular expression, allowing you to support HTTP and HTTPs. for example using /https?://localhost(:[0-9]+)?/ would return the request header appropriately in both cases. * is a valid value but is considered a security risk as your elasticsearch instance is open to cross origin requests from anywhere. NOTES: (Corresponds to the parameter &#39;http.cors.allow-origin&#39;) | [optional] 
**cors_max_age** | **int** | Browsers send a \&quot;preflight\&quot; OPTIONS-request to determine CORS settings. max-age defines how long the result should be cached for. Defaults to 1728000 (20 days). NOTES: (Corresponds to the parameter &#39;http.cors.max-age&#39;) | [optional] 
**cors_allow_methods** | **str** | Which methods to allow. Defaults to \&quot;OPTIONS, HEAD, GET, POST, PUT, DELETE\&quot;. NOTES: (The string is inserted into the value for header &#39;http.cors.allow-methods&#39;) | [optional] 
**cors_allow_headers** | **str** | Which headers to allow. Defaults to \&quot;X-Requested-With, Content-Type, Content-Length\&quot;. NOTES: (The string is inserted into the value for header &#39;http.cors.allow-headers&#39;) | [optional] 
**cors_allow_credentials** | **bool** | Whether the Access-Control-Allow-Credentials header should be returned. Note: This header is only returned, when the setting is set to true. Defaults to false. NOTES: (Corresponds to the parameter &#39;http.cors.allow-credentials&#39;) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


