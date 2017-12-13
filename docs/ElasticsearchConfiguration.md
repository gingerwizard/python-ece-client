# ElasticsearchConfiguration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** | The version of the Elasticsearch cluster (must be one of the ECE supported versions). Currently cannot be different across the topology (and is generally specified in the globals) | [optional] 
**docker_image** | **str** | A docker URI that allows overriding of the default docker image specified for this version | [optional] 
**system_settings** | [**ElasticsearchSystemSettings**](ElasticsearchSystemSettings.md) |  | [optional] 
**user_settings_json** | **object** | An arbitrary JSON object allowing cluster owners to set their parameters (only one of this and &#39;user_settings_yaml&#39; is allowed), provided they are on the whitelist (&#39;user_settings_whitelist&#39;) and not on the blacklist (&#39;user_settings_blacklist&#39;). NOTES: (This field together with &#39;user_settings_override*&#39; and &#39;system_settings&#39; defines the total set of Elasticsearch settings) | [optional] 
**user_settings_yaml** | **str** | An arbitrary YAML object allowing cluster owners to set their parameters (only one of this and &#39;user_settings_json&#39; is allowed), provided they are on the whitelist (&#39;user_settings_whitelist&#39;) and not on the blacklist (&#39;user_settings_blacklist&#39;). NOTES: (This field together with &#39;user_settings_override*&#39; and &#39;system_settings&#39; defines the total set of Elasticsearch settings) | [optional] 
**user_settings_override_json** | **object** | An arbitrary JSON object allowing ECE admins owners to set clusters&#39; parameters (only one of this and &#39;user_settings_override_yaml&#39; is allowed), ie in addition to the documented &#39;system_settings&#39;. NOTES: (This field together with &#39;system_settings&#39; and &#39;user_settings*&#39; defines the total set of Elasticsearch settings) | [optional] 
**user_settings_override_yaml** | **str** | An arbitrary YAML object allowing ECE admins owners to set clusters&#39; parameters (only one of this and &#39;user_settings_override_json&#39; is allowed), ie in addition to the documented &#39;system_settings&#39;. NOTES: (This field together with &#39;system_settings&#39; and &#39;user_settings*&#39; defines the total set of Elasticsearch settings) | [optional] 
**enabled_built_in_plugins** | **list[str]** | A list of plugin names from the Elastic-supported subset that are bundled with the version images. NOTES: (Users should consult the Elastic stack objects to see what plugins are available, this is currently only available from the UI) | [optional] 
**user_plugins** | [**list[ElasticsearchUserPlugin]**](ElasticsearchUserPlugin.md) | A list of admin-uploaded plugin objects that are available for this user. NOTES: Not yet supported in ECE, SaaS only | [optional] 
**user_bundles** | [**list[ElasticsearchUserBundle]**](ElasticsearchUserBundle.md) | A list of admin-uploaded bundle objects (eg scripts, synonym files) that are available for this user. NOTES: Not yet supported in ECE, SaaS only | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


