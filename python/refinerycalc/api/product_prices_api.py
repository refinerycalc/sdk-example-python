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


class ProductPricesApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def v1_product_prices_get(self, **kwargs):  # noqa: E501
        """Returns product price list  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_product_prices_get(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[ProductPriceModel]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_product_prices_get_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.v1_product_prices_get_with_http_info(**kwargs)  # noqa: E501
            return data

    def v1_product_prices_get_with_http_info(self, **kwargs):  # noqa: E501
        """Returns product price list  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_product_prices_get_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[ProductPriceModel]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_product_prices_get" % key
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
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/product/prices', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ProductPriceModel]',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_product_prices_id_get(self, id, **kwargs):  # noqa: E501
        """Get product price by id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_product_prices_id_get(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The id of the product price (required)
        :return: ProductPriceModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_product_prices_id_get_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_product_prices_id_get_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def v1_product_prices_id_get_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get product price by id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_product_prices_id_get_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The id of the product price (required)
        :return: ProductPriceModel
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
                    " to method v1_product_prices_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `v1_product_prices_id_get`")  # noqa: E501

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
            '/v1/product/prices/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ProductPriceModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_product_prices_region_id_get(self, id, **kwargs):  # noqa: E501
        """Get product price by region id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_product_prices_region_id_get(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: region id (required)
        :return: ProductPriceModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_product_prices_region_id_get_with_http_info(id, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_product_prices_region_id_get_with_http_info(id, **kwargs)  # noqa: E501
            return data

    def v1_product_prices_region_id_get_with_http_info(self, id, **kwargs):  # noqa: E501
        """Get product price by region id  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_product_prices_region_id_get_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: region id (required)
        :return: ProductPriceModel
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
                    " to method v1_product_prices_region_id_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `v1_product_prices_region_id_get`")  # noqa: E501

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
            '/v1/product/prices/region/{id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ProductPriceModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def v1_product_prices_region_region_name_get(self, region_name, **kwargs):  # noqa: E501
        """Get product price by region  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_product_prices_region_region_name_get(region_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str region_name: (required)
        :return: ProductPriceModel
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.v1_product_prices_region_region_name_get_with_http_info(region_name, **kwargs)  # noqa: E501
        else:
            (data) = self.v1_product_prices_region_region_name_get_with_http_info(region_name, **kwargs)  # noqa: E501
            return data

    def v1_product_prices_region_region_name_get_with_http_info(self, region_name, **kwargs):  # noqa: E501
        """Get product price by region  # noqa: E501

        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.v1_product_prices_region_region_name_get_with_http_info(region_name, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str region_name: (required)
        :return: ProductPriceModel
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['region_name']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method v1_product_prices_region_region_name_get" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'region_name' is set
        if ('region_name' not in params or
                params['region_name'] is None):
            raise ValueError("Missing the required parameter `region_name` when calling `v1_product_prices_region_region_name_get`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'region_name' in params:
            path_params['regionName'] = params['region_name']  # noqa: E501

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
            '/v1/product/prices/region/{regionName}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ProductPriceModel',  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
