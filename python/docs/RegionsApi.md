# refinerycalc.RegionsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_regions_get**](RegionsApi.md#v1_regions_get) | **GET** /v1/regions | Get all regions

# **v1_regions_get**
> list[ProductPriceModel] v1_regions_get()

Get all regions

### Example
```python
from __future__ import print_function
import time
import refinerycalc
from refinerycalc.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = refinerycalc.RegionsApi()

try:
    # Get all regions
    api_response = api_instance.v1_regions_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RegionsApi->v1_regions_get: %s\n" % e)
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

