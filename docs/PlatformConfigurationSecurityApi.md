# swagger_client.PlatformConfigurationSecurityApi

All URIs are relative to *http://localhost/api/v1/*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_enrollment_token**](PlatformConfigurationSecurityApi.md#create_enrollment_token) | **POST** /platform/configuration/security/enrollment-tokens | Create enrollment token
[**delete_enrollment_token**](PlatformConfigurationSecurityApi.md#delete_enrollment_token) | **DELETE** /platform/configuration/security/enrollment-tokens/{token} | Delete enrollment token
[**get_enrollment_tokens**](PlatformConfigurationSecurityApi.md#get_enrollment_tokens) | **GET** /platform/configuration/security/enrollment-tokens | Get enrollment tokens
[**get_tls_certificate**](PlatformConfigurationSecurityApi.md#get_tls_certificate) | **GET** /platform/configuration/security/tls/{service_name} | Get TLS certificate
[**set_tls_certificate**](PlatformConfigurationSecurityApi.md#set_tls_certificate) | **POST** /platform/configuration/security/tls/{service_name} | Set TLS certificate


# **create_enrollment_token**
> RequestEnrollmentTokenReply create_enrollment_token(body)

Create enrollment token

Creates an enrollment token.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: basicAuth
swagger_client.configuration.username = 'YOUR_USERNAME'
swagger_client.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.PlatformConfigurationSecurityApi()
body = swagger_client.EnrollmentTokenRequest() # EnrollmentTokenRequest | Request parameters for the enrollment token

try: 
    # Create enrollment token
    api_response = api_instance.create_enrollment_token(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformConfigurationSecurityApi->create_enrollment_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**EnrollmentTokenRequest**](EnrollmentTokenRequest.md)| Request parameters for the enrollment token | 

### Return type

[**RequestEnrollmentTokenReply**](RequestEnrollmentTokenReply.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_enrollment_token**
> EmptyResponse delete_enrollment_token(token)

Delete enrollment token

Revokes and deletes an enrollment token.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: basicAuth
swagger_client.configuration.username = 'YOUR_USERNAME'
swagger_client.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.PlatformConfigurationSecurityApi()
token = 'token_example' # str | The token identifier (or token itself) to revoke

try: 
    # Delete enrollment token
    api_response = api_instance.delete_enrollment_token(token)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformConfigurationSecurityApi->delete_enrollment_token: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **token** | **str**| The token identifier (or token itself) to revoke | 

### Return type

[**EmptyResponse**](EmptyResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_enrollment_tokens**
> ListEnrollmentTokenReply get_enrollment_tokens()

Get enrollment tokens

Retrieves a list of active enrollment tokens.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: basicAuth
swagger_client.configuration.username = 'YOUR_USERNAME'
swagger_client.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.PlatformConfigurationSecurityApi()

try: 
    # Get enrollment tokens
    api_response = api_instance.get_enrollment_tokens()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformConfigurationSecurityApi->get_enrollment_tokens: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**ListEnrollmentTokenReply**](ListEnrollmentTokenReply.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_tls_certificate**
> TlsPublicCertChain get_tls_certificate(service_name)

Get TLS certificate

Retrieves a certificate in the TLS certificate chain.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: basicAuth
swagger_client.configuration.username = 'YOUR_USERNAME'
swagger_client.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.PlatformConfigurationSecurityApi()
service_name = 'service_name_example' # str | The service certificate chain to read, one of adminconsole, proxy, ui

try: 
    # Get TLS certificate
    api_response = api_instance.get_tls_certificate(service_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformConfigurationSecurityApi->get_tls_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_name** | **str**| The service certificate chain to read, one of adminconsole, proxy, ui | 

### Return type

[**TlsPublicCertChain**](TlsPublicCertChain.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **set_tls_certificate**
> EmptyResponse set_tls_certificate(service_name, chain)

Set TLS certificate

Creates or updates an existing TLS certificate chain.

### Example 
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: apiKey
swagger_client.configuration.api_key['Authorization'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# swagger_client.configuration.api_key_prefix['Authorization'] = 'Bearer'
# Configure HTTP basic authorization: basicAuth
swagger_client.configuration.username = 'YOUR_USERNAME'
swagger_client.configuration.password = 'YOUR_PASSWORD'

# create an instance of the API class
api_instance = swagger_client.PlatformConfigurationSecurityApi()
service_name = 'service_name_example' # str | The service certificate chain to update, one of adminconsole, proxy, ui
chain = 'chain_example' # str | New certificate chain: the PEM encoded RSA private key, followed by the server certificate, followed by the CA certificate

try: 
    # Set TLS certificate
    api_response = api_instance.set_tls_certificate(service_name, chain)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling PlatformConfigurationSecurityApi->set_tls_certificate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_name** | **str**| The service certificate chain to update, one of adminconsole, proxy, ui | 
 **chain** | **str**| New certificate chain: the PEM encoded RSA private key, followed by the server certificate, followed by the CA certificate | 

### Return type

[**EmptyResponse**](EmptyResponse.md)

### Authorization

[apiKey](../README.md#apiKey), [basicAuth](../README.md#basicAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

