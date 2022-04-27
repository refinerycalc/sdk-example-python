# refinerycalc.RefineriesApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_refineries_aggregates_get**](RefineriesApi.md#v1_refineries_aggregates_get) | **GET** /v1/refineries/aggregates | Get Aggregated Refineries by datasource. user can also filter refineries by providing it&#x27;s name, region and country.
[**v1_refineries_crude_id_get**](RefineriesApi.md#v1_refineries_crude_id_get) | **GET** /v1/refineries/crude/{id} | Get refinery crude by using refineryCrude id.
[**v1_refineries_get**](RefineriesApi.md#v1_refineries_get) | **GET** /v1/refineries | Get all Refineries by datasource, user can also filter refineries by providing it&#x27;s name, region and country.
[**v1_refineries_id_get**](RefineriesApi.md#v1_refineries_id_get) | **GET** /v1/refineries/{id} | Get Refinery by Id.
[**v1_refineries_id_units_get**](RefineriesApi.md#v1_refineries_id_units_get) | **GET** /v1/refineries/{id}/units | Get all units of refinery id.
[**v1_refineries_individual_get**](RefineriesApi.md#v1_refineries_individual_get) | **GET** /v1/refineries/individual | Get Individual Refineries by datasource. user can also filter refineries by providing it&#x27;s name, region and country.

# **v1_refineries_aggregates_get**
> list[RefineryResponse] v1_refineries_aggregates_get(data_source=data_source, name=name, region=region, country=country)

Get Aggregated Refineries by datasource. user can also filter refineries by providing it's name, region and country.

### Example
```python
from __future__ import print_function
import time
import refinerycalc
from refinerycalc.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = refinerycalc.RefineriesApi()
data_source = refinerycalc.DataSource() # DataSource |  (optional)
name = 'name_example' # str |  (optional)
region = 'region_example' # str |  (optional)
country = 'country_example' # str |  (optional)

try:
    # Get Aggregated Refineries by datasource. user can also filter refineries by providing it's name, region and country.
    api_response = api_instance.v1_refineries_aggregates_get(data_source=data_source, name=name, region=region, country=country)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RefineriesApi->v1_refineries_aggregates_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_source** | [**DataSource**](.md)|  | [optional] 
 **name** | **str**|  | [optional] 
 **region** | **str**|  | [optional] 
 **country** | **str**|  | [optional] 

### Return type

[**list[RefineryResponse]**](RefineryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_refineries_crude_id_get**
> RefineryCrudeModel v1_refineries_crude_id_get(id)

Get refinery crude by using refineryCrude id.

### Example
```python
from __future__ import print_function
import time
import refinerycalc
from refinerycalc.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = refinerycalc.RefineriesApi()
id = 56 # int | Refinery Crude Id

try:
    # Get refinery crude by using refineryCrude id.
    api_response = api_instance.v1_refineries_crude_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RefineriesApi->v1_refineries_crude_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**| Refinery Crude Id | 

### Return type

[**RefineryCrudeModel**](RefineryCrudeModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_refineries_get**
> list[RefineryResponse] v1_refineries_get(data_source=data_source, name=name, region=region, country=country)

Get all Refineries by datasource, user can also filter refineries by providing it's name, region and country.

### Example
```python
from __future__ import print_function
import time
import refinerycalc
from refinerycalc.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = refinerycalc.RefineriesApi()
data_source = refinerycalc.DataSource() # DataSource |  (optional)
name = 'name_example' # str |  (optional)
region = 'region_example' # str |  (optional)
country = 'country_example' # str |  (optional)

try:
    # Get all Refineries by datasource, user can also filter refineries by providing it's name, region and country.
    api_response = api_instance.v1_refineries_get(data_source=data_source, name=name, region=region, country=country)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RefineriesApi->v1_refineries_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_source** | [**DataSource**](.md)|  | [optional] 
 **name** | **str**|  | [optional] 
 **region** | **str**|  | [optional] 
 **country** | **str**|  | [optional] 

### Return type

[**list[RefineryResponse]**](RefineryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_refineries_id_get**
> RefineryModel v1_refineries_id_get(id)

Get Refinery by Id.

### Example
```python
from __future__ import print_function
import time
import refinerycalc
from refinerycalc.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = refinerycalc.RefineriesApi()
id = 56 # int | 

try:
    # Get Refinery by Id.
    api_response = api_instance.v1_refineries_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RefineriesApi->v1_refineries_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**RefineryModel**](RefineryModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_refineries_id_units_get**
> list[RefineryUnitModel] v1_refineries_id_units_get(id)

Get all units of refinery id.

### Example
```python
from __future__ import print_function
import time
import refinerycalc
from refinerycalc.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = refinerycalc.RefineriesApi()
id = 56 # int | 

try:
    # Get all units of refinery id.
    api_response = api_instance.v1_refineries_id_units_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RefineriesApi->v1_refineries_id_units_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **int**|  | 

### Return type

[**list[RefineryUnitModel]**](RefineryUnitModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_refineries_individual_get**
> list[RefineryResponse] v1_refineries_individual_get(data_source=data_source, name=name, region=region, country=country)

Get Individual Refineries by datasource. user can also filter refineries by providing it's name, region and country.

### Example
```python
from __future__ import print_function
import time
import refinerycalc
from refinerycalc.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = refinerycalc.RefineriesApi()
data_source = refinerycalc.DataSource() # DataSource |  (optional)
name = 'name_example' # str |  (optional)
region = 'region_example' # str |  (optional)
country = 'country_example' # str |  (optional)

try:
    # Get Individual Refineries by datasource. user can also filter refineries by providing it's name, region and country.
    api_response = api_instance.v1_refineries_individual_get(data_source=data_source, name=name, region=region, country=country)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RefineriesApi->v1_refineries_individual_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **data_source** | [**DataSource**](.md)|  | [optional] 
 **name** | **str**|  | [optional] 
 **region** | **str**|  | [optional] 
 **country** | **str**|  | [optional] 

### Return type

[**list[RefineryResponse]**](RefineryResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

