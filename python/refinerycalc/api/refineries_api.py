# coding: utf-8

"""
    Refinery Calc API Documentation

    Integrate the powerful Refinery Calc Engine into your process using this API.  # noqa: E501

    OpenAPI spec version: 1.0
    Contact: support@refinerycalc.com.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from refinerycalc.api_client import ApiClient


class RefineriesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def v1_refineries_aggregates_get(self, **kwargs):  # noqa: E501
        """Get Aggregated Refineries by datasource. user can also filter refineries by providing it's name, region and country.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_refineries_aggregates_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DataSource data_source:
        :param str name:
        :param str region:
        :param str country:
        :return: list[RefineryResponse]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_refineries_aggregates_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.v1_refineries_aggregates_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def v1_refineries_aggregates_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get Aggregated Refineries by datasource. user can also filter refineries by providing it's name, region and country.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_refineries_aggregates_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DataSource data_source:
        :param str name:
        :param str region:
        :param str country:
        :return: list[RefineryResponse]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['data_source', 'name', 'region', 'country']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_refineries_aggregates_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'data_source' in params:
            query_params.append(('dataSource', params['data_source']))  # noqa: E501
        if 'name' in params:
            query_params.append(('name', params['name']))  # noqa: E501
        if 'region' in params:
            query_params.append(('region', params['region']))  # noqa: E501
        if 'country' in params:
            query_params.append(('country', params['country']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/refineries/aggregates', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[RefineryResponse]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_refineries_crude_id_get(self, id, **kwargs):  # noqa: E501
        """Get refinery crude by using refineryCrude id.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_refineries_crude_id_get(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Refinery Crude Id (required)
        :return: RefineryCrudeModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_refineries_crude_id_get_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_refineries_crude_id_get_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def v1_refineries_crude_id_get_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get refinery crude by using refineryCrude id.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_refineries_crude_id_get_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: Refinery Crude Id (required)
        :return: RefineryCrudeModel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_refineries_crude_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `v1_refineries_crude_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/refineries/crude/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RefineryCrudeModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_refineries_get(self, **kwargs):  # noqa: E501
        """Get all Refineries by datasource, user can also filter refineries by providing it's name, region and country.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_refineries_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DataSource data_source:
        :param str name:
        :param str region:
        :param str country:
        :return: list[RefineryResponse]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_refineries_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.v1_refineries_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def v1_refineries_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get all Refineries by datasource, user can also filter refineries by providing it's name, region and country.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_refineries_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DataSource data_source:
        :param str name:
        :param str region:
        :param str country:
        :return: list[RefineryResponse]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['data_source', 'name', 'region', 'country']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_refineries_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'data_source' in params:
            query_params.append(('dataSource', params['data_source']))  # noqa: E501
        if 'name' in params:
            query_params.append(('name', params['name']))  # noqa: E501
        if 'region' in params:
            query_params.append(('region', params['region']))  # noqa: E501
        if 'country' in params:
            query_params.append(('country', params['country']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/refineries', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[RefineryResponse]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_refineries_id_get(self, id, **kwargs):  # noqa: E501
        """Get Refinery by Id.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_refineries_id_get(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: (required)
        :return: RefineryModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_refineries_id_get_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_refineries_id_get_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def v1_refineries_id_get_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get Refinery by Id.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_refineries_id_get_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: (required)
        :return: RefineryModel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_refineries_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `v1_refineries_id_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/refineries/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RefineryModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_refineries_id_units_get(self, id, **kwargs):  # noqa: E501
        """Get all units of refinery id.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_refineries_id_units_get(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: (required)
        :return: list[RefineryUnitModel]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_refineries_id_units_get_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_refineries_id_units_get_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def v1_refineries_id_units_get_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get all units of refinery id.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_refineries_id_units_get_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: (required)
        :return: list[RefineryUnitModel]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_refineries_id_units_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `v1_refineries_id_units_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'id' in params:
            path_params['id'] = params['id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/refineries/{id}/units', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[RefineryUnitModel]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_refineries_individual_get(self, **kwargs):  # noqa: E501
        """Get Individual Refineries by datasource. user can also filter refineries by providing it's name, region and country.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_refineries_individual_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DataSource data_source:
        :param str name:
        :param str region:
        :param str country:
        :return: list[RefineryResponse]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_refineries_individual_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.v1_refineries_individual_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def v1_refineries_individual_get_with_http_info(self, **kwargs):  # noqa: E501
        """Get Individual Refineries by datasource. user can also filter refineries by providing it's name, region and country.  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_refineries_individual_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param DataSource data_source:
        :param str name:
        :param str region:
        :param str country:
        :return: list[RefineryResponse]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['data_source', 'name', 'region', 'country']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_refineries_individual_get" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'data_source' in params:
            query_params.append(('dataSource', params['data_source']))  # noqa: E501
        if 'name' in params:
            query_params.append(('name', params['name']))  # noqa: E501
        if 'region' in params:
            query_params.append(('region', params['region']))  # noqa: E501
        if 'country' in params:
            query_params.append(('country', params['country']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/refineries/individual', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[RefineryResponse]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
