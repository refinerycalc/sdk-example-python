# refinerycalc.ProductPricesApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_product_prices_get**](ProductPricesApi.md#v1_product_prices_get) | **GET** /v1/product/prices | Returns product price list
[**v1_product_prices_id_get**](ProductPricesApi.md#v1_product_prices_id_get) | **GET** /v1/product/prices/{id} | Get product price by id
[**v1_product_prices_region_id_get**](ProductPricesApi.md#v1_product_prices_region_id_get) | **GET** /v1/product/prices/region/{id} | Get product price by region id
[**v1_product_prices_region_region_name_get**](ProductPricesApi.md#v1_product_prices_region_region_name_get) | **GET** /v1/product/prices/region/{regionName} | Get product price by region

# **v1_product_prices_get**
> list[ProductPriceModel] v1_product_prices_get()

Returns product price list

### Example
```python
from __future__ import print_function
import time
import refinerycalc
from refinerycalc.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = refinerycalc.ProductPricesApi()

try:
    # Returns product price list
    api_response = api_instance.v1_product_prices_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductPricesApi->v1_product_prices_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[ProductPriceModel]**](ProductPriceModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_product_prices_id_get**
> ProductPriceModel v1_product_prices_id_get(id)

Get product price by id

### Example
```python
from __future__ import print_function
import time
import refinerycalc
from refinerycalc.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = refinerycalc.ProductPricesApi()
id = 56 # int | The id of the product price

try:
    # Get product price by id
    api_response = api_instance.v1_product_prices_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductPricesApi->v1_product_prices_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| The id of the product price | 

### Return type

[**ProductPriceModel**](ProductPriceModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_product_prices_region_id_get**
> ProductPriceModel v1_product_prices_region_id_get(id)

Get product price by region id

### Example
```python
from __future__ import print_function
import time
import refinerycalc
from refinerycalc.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = refinerycalc.ProductPricesApi()
id = 56 # int | region id

try:
    # Get product price by region id
    api_response = api_instance.v1_product_prices_region_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductPricesApi->v1_product_prices_region_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| region id | 

### Return type

[**ProductPriceModel**](ProductPriceModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_product_prices_region_region_name_get**
> ProductPriceModel v1_product_prices_region_region_name_get(region_name)

Get product price by region

### Example
```python
from __future__ import print_function
import time
import refinerycalc
from refinerycalc.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = refinerycalc.ProductPricesApi()
region_name = 'region_name_example' # str | 

try:
    # Get product price by region
    api_response = api_instance.v1_product_prices_region_region_name_get(region_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductPricesApi->v1_product_prices_region_region_name_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **region_name** | **str**|  | 

### Return type

[**ProductPriceModel**](ProductPriceModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

