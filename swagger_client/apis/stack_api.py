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


class StackApi(object):
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

    def delete_version_stack(self, version, **kwargs):
        """
        Mark an Elastic Stack version for deletion
        Sets a flag 'deleted' that effectively only removes the Elastic Stack Version from the list of available versions. The version can be restored later by sending an update request for the version (See PUT request)
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_version_stack(version, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str version: An Elastic Stack version (required)
        :return: EmptyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.delete_version_stack_with_http_info(version, **kwargs)
        else:
            (data) = self.delete_version_stack_with_http_info(version, **kwargs)
            return data

    def delete_version_stack_with_http_info(self, version, **kwargs):
        """
        Mark an Elastic Stack version for deletion
        Sets a flag 'deleted' that effectively only removes the Elastic Stack Version from the list of available versions. The version can be restored later by sending an update request for the version (See PUT request)
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.delete_version_stack_with_http_info(version, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str version: An Elastic Stack version (required)
        :return: EmptyResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['version']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_version_stack" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'version' is set
        if ('version' not in params) or (params['version'] is None):
            raise ValueError("Missing the required parameter `version` when calling `delete_version_stack`")


        collection_formats = {}

        path_params = {}
        if 'version' in params:
            path_params['version'] = params['version']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['apiKey', 'basicAuth']

        return self.api_client.call_api('/stack/versions/{version}', 'DELETE',
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

    def get_version_stack(self, version, **kwargs):
        """
        Get an Elastic Stack version
        Retrieves a single Elastic Stack version with template.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_version_stack(version, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str version: An Elastic Stack version (required)
        :return: StackVersionConfig
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_version_stack_with_http_info(version, **kwargs)
        else:
            (data) = self.get_version_stack_with_http_info(version, **kwargs)
            return data

    def get_version_stack_with_http_info(self, version, **kwargs):
        """
        Get an Elastic Stack version
        Retrieves a single Elastic Stack version with template.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_version_stack_with_http_info(version, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str version: An Elastic Stack version (required)
        :return: StackVersionConfig
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['version']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_version_stack" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'version' is set
        if ('version' not in params) or (params['version'] is None):
            raise ValueError("Missing the required parameter `version` when calling `get_version_stack`")


        collection_formats = {}

        path_params = {}
        if 'version' in params:
            path_params['version'] = params['version']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['apiKey', 'basicAuth']

        return self.api_client.call_api('/stack/versions/{version}', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='StackVersionConfig',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def get_version_stacks(self, **kwargs):
        """
        Get all available Elastic Stack versions
        By default it returns only available versions. Use parameter `show_deleted` to get all versions
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_version_stacks(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param bool show_deleted: Whether to show deleted stack versions or not
        :return: StackVersionConfigs
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.get_version_stacks_with_http_info(**kwargs)
        else:
            (data) = self.get_version_stacks_with_http_info(**kwargs)
            return data

    def get_version_stacks_with_http_info(self, **kwargs):
        """
        Get all available Elastic Stack versions
        By default it returns only available versions. Use parameter `show_deleted` to get all versions
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.get_version_stacks_with_http_info(callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param bool show_deleted: Whether to show deleted stack versions or not
        :return: StackVersionConfigs
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['show_deleted']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_version_stacks" % key
                )
            params[key] = val
        del params['kwargs']


        collection_formats = {}

        path_params = {}

        query_params = []
        if 'show_deleted' in params:
            query_params.append(('show_deleted', params['show_deleted']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = ['apiKey', 'basicAuth']

        return self.api_client.call_api('/stack/versions', 'GET',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='StackVersionConfigs',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def update_stack_packs(self, file, **kwargs):
        """
        Submit Elastic Stack packs
        Adds a new or updates existing Elastic Stack version and its template. Besides `multipart/form-data` requests, the endpoint supports `application/zip` and `application/octet-stream` requests with a binary body. Maximum size of the payload is 1Mb. If the archive contains a stack configuration that is already available through the API, then the existing configuration and its template will be overwritten.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_stack_packs(file, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param file file: Zip file that contains one or multiple stack configurations (required)
        :return: StackVersionArchiveProcessingResult
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_stack_packs_with_http_info(file, **kwargs)
        else:
            (data) = self.update_stack_packs_with_http_info(file, **kwargs)
            return data

    def update_stack_packs_with_http_info(self, file, **kwargs):
        """
        Submit Elastic Stack packs
        Adds a new or updates existing Elastic Stack version and its template. Besides `multipart/form-data` requests, the endpoint supports `application/zip` and `application/octet-stream` requests with a binary body. Maximum size of the payload is 1Mb. If the archive contains a stack configuration that is already available through the API, then the existing configuration and its template will be overwritten.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_stack_packs_with_http_info(file, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param file file: Zip file that contains one or multiple stack configurations (required)
        :return: StackVersionArchiveProcessingResult
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['file']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_stack_packs" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'file' is set
        if ('file' not in params) or (params['file'] is None):
            raise ValueError("Missing the required parameter `file` when calling `update_stack_packs`")


        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}
        if 'file' in params:
            local_var_files['file'] = params['file']

        body_params = None
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.\
            select_header_content_type(['multipart/form-data'])

        # Authentication setting
        auth_settings = ['apiKey', 'basicAuth']

        return self.api_client.call_api('/stack/versions', 'POST',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='StackVersionArchiveProcessingResult',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)

    def update_version_stack(self, version, stack_config, **kwargs):
        """
        Update an Elastic Stack version
        Updates the configuration of an existing Elastic Stack version.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_version_stack(version, stack_config, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str version: An Elastic Stack version (required)
        :param StackVersionConfigPost stack_config: Elastic Stack configuration object (required)
        :return: StackVersionConfig
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('callback'):
            return self.update_version_stack_with_http_info(version, stack_config, **kwargs)
        else:
            (data) = self.update_version_stack_with_http_info(version, stack_config, **kwargs)
            return data

    def update_version_stack_with_http_info(self, version, stack_config, **kwargs):
        """
        Update an Elastic Stack version
        Updates the configuration of an existing Elastic Stack version.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please define a `callback` function
        to be invoked when receiving the response.
        >>> def callback_function(response):
        >>>     pprint(response)
        >>>
        >>> thread = api.update_version_stack_with_http_info(version, stack_config, callback=callback_function)

        :param callback function: The callback function
            for asynchronous request. (optional)
        :param str version: An Elastic Stack version (required)
        :param StackVersionConfigPost stack_config: Elastic Stack configuration object (required)
        :return: StackVersionConfig
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['version', 'stack_config']
        all_params.append('callback')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_version_stack" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'version' is set
        if ('version' not in params) or (params['version'] is None):
            raise ValueError("Missing the required parameter `version` when calling `update_version_stack`")
        # verify the required parameter 'stack_config' is set
        if ('stack_config' not in params) or (params['stack_config'] is None):
            raise ValueError("Missing the required parameter `stack_config` when calling `update_version_stack`")


        collection_formats = {}

        path_params = {}
        if 'version' in params:
            path_params['version'] = params['version']

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'stack_config' in params:
            body_params = params['stack_config']
        # Authentication setting
        auth_settings = ['apiKey', 'basicAuth']

        return self.api_client.call_api('/stack/versions/{version}', 'PUT',
                                        path_params,
                                        query_params,
                                        header_params,
                                        body=body_params,
                                        post_params=form_params,
                                        files=local_var_files,
                                        response_type='StackVersionConfig',
                                        auth_settings=auth_settings,
                                        callback=params.get('callback'),
                                        _return_http_data_only=params.get('_return_http_data_only'),
                                        _preload_content=params.get('_preload_content', True),
                                        _request_timeout=params.get('_request_timeout'),
                                        collection_formats=collection_formats)