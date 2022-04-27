# refinerycalc.EndPointsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_endpoints_get**](EndPointsApi.md#v1_endpoints_get) | **GET** /v1/endpoints | Returns end point list
[**v1_endpoints_id_get**](EndPointsApi.md#v1_endpoints_id_get) | **GET** /v1/endpoints/{id} | Get end point by id

# **v1_endpoints_get**
> list[EndPointModel] v1_endpoints_get()

Returns end point list

### Example
```python
from __future__ import print_function
import time
import refinerycalc
from refinerycalc.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = refinerycalc.EndPointsApi()

try:
    # Returns end point list
    api_response = api_instance.v1_endpoints_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndPointsApi->v1_endpoints_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[EndPointModel]**](EndPointModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_endpoints_id_get**
> EndPointModel v1_endpoints_id_get(id)

Get end point by id

### Example
```python
from __future__ import print_function
import time
import refinerycalc
from refinerycalc.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = refinerycalc.EndPointsApi()
id = 56 # int | End point id

try:
    # Get end point by id
    api_response = api_instance.v1_endpoints_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling EndPointsApi->v1_endpoints_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| End point id | 

### Return type

[**EndPointModel**](EndPointModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

