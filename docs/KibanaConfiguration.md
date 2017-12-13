# KibanaConfiguration

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**version** | **str** | The version of the Kibana cluster (must be one of the ECE supported versions, and won&#39;t work unless it matches the Elasticsearch version. Leave blank to auto-detect version.) | [optional] 
**docker_image** | **str** | A docker URI that allows overriding of the default docker image specified for this version | [optional] 
**system_settings** | [**KibanaSystemSettings**](KibanaSystemSettings.md) |  | [optional] 
**user_settings_json** | **object** | An arbitrary JSON object allowing (non-admin) cluster owners to set their parameters (only one of this and &#39;user_settings_yaml&#39; is allowed), provided they are on the whitelist (&#39;user_settings_whitelist&#39;) and not on the blacklist (&#39;user_settings_blacklist&#39;). (This field together with &#39;user_settings_override*&#39; and &#39;system_settings&#39; defines the total set of Kibana settings) | [optional] 
**user_settings_yaml** | **str** | An arbitrary YAML object allowing (non-admin) cluster owners to set their parameters (only one of this and &#39;user_settings_json&#39; is allowed), provided they are on the whitelist (&#39;user_settings_whitelist&#39;) and not on the blacklist (&#39;user_settings_blacklist&#39;). (These field together with &#39;user_settings_override*&#39; and &#39;system_settings&#39; defines the total set of Kibana settings) | [optional] 
**user_settings_override_json** | **object** | An arbitrary JSON object allowing ECE admins owners to set clusters&#39; parameters (only one of this and &#39;user_settings_override_yaml&#39; is allowed), ie in addition to the documented &#39;system_settings&#39;. (This field together with &#39;system_settings&#39; and &#39;user_settings*&#39; defines the total set of Kibana settings) | [optional] 
**user_settings_override_yaml** | **str** | An arbitrary YAML object allowing ECE admins owners to set clusters&#39; parameters (only one of this and &#39;user_settings_override_json&#39; is allowed), ie in addition to the documented &#39;system_settings&#39;. (This field together with &#39;system_settings&#39; and &#39;user_settings*&#39; defines the total set of Kibana settings) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


