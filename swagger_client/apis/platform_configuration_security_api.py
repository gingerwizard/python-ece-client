# coding: utf-8

"""
    

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import sys
import os
import re

# python 2 and python 3 compatibility library
from six import iteritems

from ..configuration import Configuration
from ..api_client import ApiClient


class PlatformConfigurationSecurityApi(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        config = Configuration()
        if api_client:
            self.api_client = api_client
        else:
            if not config.api_client:
                config.api_client = ApiClient()
            self.api_client = config.api_client

    def create_enrollment_token(self, body, **kwargs):
        """
        Create enrollment token
        Creates an enrollment token.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_enrollment_token(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param EnrollmentTokenRequest body: Request parameters for the enrollment token (required)
        :return: RequestEnrollmentTokenReply
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.create_enrollment_token_with_http_info(body, **kwargs)
        else:
            (data) = self.create_enrollment_token_with_http_info(body, **kwargs)
            return data

    def create_enrollment_token_with_http_info(self, body, **kwargs):
        """
        Create enrollment token
        Creates an enrollment token.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.create_enrollment_token_with_http_info(body, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param EnrollmentTokenRequest body: Request parameters for the enrollment token (required)
        :return: RequestEnrollmentTokenReply
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_enrollment_token" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params) or (params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_enrollment_token`")


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # Authentication setting
        auth_settings = ['apiKey', 'basicAuth']

        return self.api_client.call_api('/platform/configuration/security/enrollment-tokens', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='RequestEnrollmentTokenReply',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def delete_enrollment_token(self, token, **kwargs):
        """
        Delete enrollment token
        Revokes and deletes an enrollment token.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_enrollment_token(token, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str token: The token identifier (or token itself) to revoke (required)
        :return: EmptyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_enrollment_token_with_http_info(token, **kwargs)
        else:
            (data) = self.delete_enrollment_token_with_http_info(token, **kwargs)
            return data

    def delete_enrollment_token_with_http_info(self, token, **kwargs):
        """
        Delete enrollment token
        Revokes and deletes an enrollment token.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_enrollment_token_with_http_info(token, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str token: The token identifier (or token itself) to revoke (required)
        :return: EmptyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['token']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_enrollment_token" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'token' is set
        if ('token' not in params) or (params['token'] is None):
            raise ValueError("Missing the required parameter `token` when calling `delete_enrollment_token`")


        collection_formats = {}

        path_params = {}
        if 'token' in params:
            path_params['token'] = params['token']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['apiKey', 'basicAuth']

        return self.api_client.call_api('/platform/configuration/security/enrollment-tokens/{token}', 'DELETE',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='EmptyResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_enrollment_tokens(self, **kwargs):
        """
        Get enrollment tokens
        Retrieves a list of active enrollment tokens.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_enrollment_tokens(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: ListEnrollmentTokenReply
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_enrollment_tokens_with_http_info(**kwargs)
        else:
            (data) = self.get_enrollment_tokens_with_http_info(**kwargs)
            return data

    def get_enrollment_tokens_with_http_info(self, **kwargs):
        """
        Get enrollment tokens
        Retrieves a list of active enrollment tokens.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_enrollment_tokens_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :return: ListEnrollmentTokenReply
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_enrollment_tokens" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['apiKey', 'basicAuth']

        return self.api_client.call_api('/platform/configuration/security/enrollment-tokens', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='ListEnrollmentTokenReply',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_tls_certificate(self, service_name, **kwargs):
        """
        Get TLS certificate
        Retrieves a certificate in the TLS certificate chain.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_tls_certificate(service_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str service_name: The service certificate chain to read, one of adminconsole, proxy, ui (required)
        :return: TlsPublicCertChain
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_tls_certificate_with_http_info(service_name, **kwargs)
        else:
            (data) = self.get_tls_certificate_with_http_info(service_name, **kwargs)
            return data

    def get_tls_certificate_with_http_info(self, service_name, **kwargs):
        """
        Get TLS certificate
        Retrieves a certificate in the TLS certificate chain.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_tls_certificate_with_http_info(service_name, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str service_name: The service certificate chain to read, one of adminconsole, proxy, ui (required)
        :return: TlsPublicCertChain
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['service_name']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_tls_certificate" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'service_name' is set
        if ('service_name' not in params) or (params['service_name'] is None):
            raise ValueError("Missing the required parameter `service_name` when calling `get_tls_certificate`")


        collection_formats = {}

        path_params = {}
        if 'service_name' in params:
            path_params['service_name'] = params['service_name']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['apiKey', 'basicAuth']

        return self.api_client.call_api('/platform/configuration/security/tls/{service_name}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='TlsPublicCertChain',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def set_tls_certificate(self, service_name, chain, **kwargs):
        """
        Set TLS certificate
        Creates or updates an existing TLS certificate chain.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.set_tls_certificate(service_name, chain, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str service_name: The service certificate chain to update, one of adminconsole, proxy, ui (required)
        :param str chain: New certificate chain: the PEM encoded RSA private key, followed by the server certificate, followed by the CA certificate (required)
        :return: EmptyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.set_tls_certificate_with_http_info(service_name, chain, **kwargs)
        else:
            (data) = self.set_tls_certificate_with_http_info(service_name, chain, **kwargs)
            return data

    def set_tls_certificate_with_http_info(self, service_name, chain, **kwargs):
        """
        Set TLS certificate
        Creates or updates an existing TLS certificate chain.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.set_tls_certificate_with_http_info(service_name, chain, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str service_name: The service certificate chain to update, one of adminconsole, proxy, ui (required)
        :param str chain: New certificate chain: the PEM encoded RSA private key, followed by the server certificate, followed by the CA certificate (required)
        :return: EmptyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['service_name', 'chain']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method set_tls_certificate" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'service_name' is set
        if ('service_name' not in params) or (params['service_name'] is None):
            raise ValueError("Missing the required parameter `service_name` when calling `set_tls_certificate`")
        # verify the required parameter 'chain' is set
        if ('chain' not in params) or (params['chain'] is None):
            raise ValueError("Missing the required parameter `chain` when calling `set_tls_certificate`")


        collection_formats = {}

        path_params = {}
        if 'service_name' in params:
            path_params['service_name'] = params['service_name']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'chain' in params:
            body_params = params['chain']
        # Authentication setting
        auth_settings = ['apiKey', 'basicAuth']

        return self.api_client.call_api('/platform/configuration/security/tls/{service_name}', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='EmptyResponse',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)
