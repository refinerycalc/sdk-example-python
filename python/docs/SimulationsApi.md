# refinerycalc.SimulationsApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**v1_simulations_get**](SimulationsApi.md#v1_simulations_get) | **GET** /v1/simulations | Returns simulation list
[**v1_simulations_id_delete**](SimulationsApi.md#v1_simulations_id_delete) | **DELETE** /v1/simulations/{id} | Delete a simulation
[**v1_simulations_id_get**](SimulationsApi.md#v1_simulations_id_get) | **GET** /v1/simulations/{id} | Returns simulations refineries details
[**v1_simulations_id_output_get**](SimulationsApi.md#v1_simulations_id_output_get) | **GET** /v1/simulations/{id}/output | Retrieves a OutputModel for the given input simuation Id.
[**v1_simulations_id_refineries_advanced_options_patch**](SimulationsApi.md#v1_simulations_id_refineries_advanced_options_patch) | **PATCH** /v1/simulations/{id}/refineries/advanced/options | Updates the advanced options for the given refineries
[**v1_simulations_id_refineries_crude_allocation_patch**](SimulationsApi.md#v1_simulations_id_refineries_crude_allocation_patch) | **PATCH** /v1/simulations/{id}/refineries/crude/allocation | Update Crude Allocation Value for One or More Refineries
[**v1_simulations_id_refineries_crude_allocations_default_patch**](SimulationsApi.md#v1_simulations_id_refineries_crude_allocations_default_patch) | **PATCH** /v1/simulations/{id}/refineries/crude/allocations/default | Refinery set default value for crude compositions
[**v1_simulations_id_refineries_crude_prices_default_patch**](SimulationsApi.md#v1_simulations_id_refineries_crude_prices_default_patch) | **PATCH** /v1/simulations/{id}/refineries/crude/prices/default | Refinery set default value for crude price
[**v1_simulations_id_refineries_crude_prices_patch**](SimulationsApi.md#v1_simulations_id_refineries_crude_prices_patch) | **PATCH** /v1/simulations/{id}/refineries/crude/prices | Update Crude Prices for One or More Refineries
[**v1_simulations_id_refineries_endpoint_mode_patch**](SimulationsApi.md#v1_simulations_id_refineries_endpoint_mode_patch) | **PATCH** /v1/simulations/{id}/refineries/endpoint/mode | Returns Success or failed
[**v1_simulations_id_refineries_endpoints_default_patch**](SimulationsApi.md#v1_simulations_id_refineries_endpoints_default_patch) | **PATCH** /v1/simulations/{id}/refineries/endpoints/default | Refinery set default value for end points
[**v1_simulations_id_refineries_get**](SimulationsApi.md#v1_simulations_id_refineries_get) | **GET** /v1/simulations/{id}/refineries | Retrieves a list of refineries for the given simulation.
[**v1_simulations_id_refineries_intermediate_products_patch**](SimulationsApi.md#v1_simulations_id_refineries_intermediate_products_patch) | **PATCH** /v1/simulations/{id}/refineries/intermediate/products | 
[**v1_simulations_id_refineries_post**](SimulationsApi.md#v1_simulations_id_refineries_post) | **POST** /v1/simulations/{id}/refineries | Adds a list of refineries to an existing simulation.
[**v1_simulations_id_refineries_product_prices_default_patch**](SimulationsApi.md#v1_simulations_id_refineries_product_prices_default_patch) | **PATCH** /v1/simulations/{id}/refineries/product/prices/default | Refinery set default value for product prices
[**v1_simulations_id_refineries_product_prices_patch**](SimulationsApi.md#v1_simulations_id_refineries_product_prices_patch) | **PATCH** /v1/simulations/{id}/refineries/product/prices | Simulation&#x27;s refineries set product price
[**v1_simulations_id_refineries_refinery_id_crude_get**](SimulationsApi.md#v1_simulations_id_refineries_refinery_id_crude_get) | **GET** /v1/simulations/{id}/refineries/{refineryId}/crude | 
[**v1_simulations_id_refineries_refinery_id_delete**](SimulationsApi.md#v1_simulations_id_refineries_refinery_id_delete) | **DELETE** /v1/simulations/{id}/refineries/{refineryId} | Remove Refinery from an existing simulation.
[**v1_simulations_id_refineries_refinery_id_endpoints_get**](SimulationsApi.md#v1_simulations_id_refineries_refinery_id_endpoints_get) | **GET** /v1/simulations/{id}/refineries/{refineryId}/endpoints | Retrieves a list of Endpoints for the given input simuation Id and Refinery Id.
[**v1_simulations_id_refineries_refinery_id_product_prices_get**](SimulationsApi.md#v1_simulations_id_refineries_refinery_id_product_prices_get) | **GET** /v1/simulations/{id}/refineries/{refineryId}/product/prices | Get product prices for a given simulation
[**v1_simulations_id_refineries_refinery_id_units_get**](SimulationsApi.md#v1_simulations_id_refineries_refinery_id_units_get) | **GET** /v1/simulations/{id}/refineries/{refineryId}/units | Retrieves Units for a given Simulation and Refinery
[**v1_simulations_id_refineries_units_bias_patch**](SimulationsApi.md#v1_simulations_id_refineries_units_bias_patch) | **PATCH** /v1/simulations/{id}/refineries/units/bias | Update simulation refinery unit bios
[**v1_simulations_id_refineries_units_default_patch**](SimulationsApi.md#v1_simulations_id_refineries_units_default_patch) | **PATCH** /v1/simulations/{id}/refineries/units/default | Refinery set default value for units
[**v1_simulations_id_refineries_units_health_state_patch**](SimulationsApi.md#v1_simulations_id_refineries_units_health_state_patch) | **PATCH** /v1/simulations/{id}/refineries/units/health/state | Update the health state of the specified units for the specified refineries in the given simulation
[**v1_simulations_id_refineries_units_mode_patch**](SimulationsApi.md#v1_simulations_id_refineries_units_mode_patch) | **PATCH** /v1/simulations/{id}/refineries/units/mode | Update simulation refinery unit mode
[**v1_simulations_id_refineries_units_rate_patch**](SimulationsApi.md#v1_simulations_id_refineries_units_rate_patch) | **PATCH** /v1/simulations/{id}/refineries/units/rate | Update simulation refinery unit rate
[**v1_simulations_id_refineries_units_toggle_shutdown_status_patch**](SimulationsApi.md#v1_simulations_id_refineries_units_toggle_shutdown_status_patch) | **PATCH** /v1/simulations/{id}/refineries/units/toggle/shutdown/status | Update simulation refinery toggle unit status
[**v1_simulations_id_refinery_change_endpoint_post**](SimulationsApi.md#v1_simulations_id_refinery_change_endpoint_post) | **POST** /v1/simulations/{id}/refinery/change/endpoint | Returns Success or failed
[**v1_simulations_id_rename_patch**](SimulationsApi.md#v1_simulations_id_rename_patch) | **PATCH** /v1/simulations/{id}/rename | Rename an existing simulation
[**v1_simulations_id_run_post**](SimulationsApi.md#v1_simulations_id_run_post) | **POST** /v1/simulations/{id}/run | Run a simulation by Id
[**v1_simulations_id_run_status_get**](SimulationsApi.md#v1_simulations_id_run_status_get) | **GET** /v1/simulations/{id}/run/status | Get simulation run status
[**v1_simulations_id_schedule_delete**](SimulationsApi.md#v1_simulations_id_schedule_delete) | **DELETE** /v1/simulations/{id}/schedule | Delete a simulation schedule.
[**v1_simulations_id_schedule_post**](SimulationsApi.md#v1_simulations_id_schedule_post) | **POST** /v1/simulations/{id}/schedule | Schedule a simulation to run
[**v1_simulations_post**](SimulationsApi.md#v1_simulations_post) | **POST** /v1/simulations | Create a new simulation from a given list of refineries
[**v1_simulations_schedules_get**](SimulationsApi.md#v1_simulations_schedules_get) | **GET** /v1/simulations/schedules | Retrieves list of the scheduled simulations.
[**v1_simulations_simulation_id_refineries_kero_mode_patch**](SimulationsApi.md#v1_simulations_simulation_id_refineries_kero_mode_patch) | **PATCH** /v1/simulations/{simulation_id}/refineries/kero/mode | Update refinery kero mode

# **v1_simulations_get**
> SimulationResponse v1_simulations_get()

Returns simulation list

### Example
```python
from __future__ import print_function
import time
import refinerycalc
from refinerycalc.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = refinerycalc.SimulationsApi()

try:
    # Returns simulation list
    api_response = api_instance.v1_simulations_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimulationsApi->v1_simulations_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SimulationResponse**](SimulationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_simulations_id_delete**
> ApiResponse v1_simulations_id_delete(id)

Delete a simulation

### Example
```python
from __future__ import print_function
import time
import refinerycalc
from refinerycalc.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = refinerycalc.SimulationsApi()
id = 'id_example' # str | 

try:
    # Delete a simulation
    api_response = api_instance.v1_simulations_id_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimulationsApi->v1_simulations_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_simulations_id_get**
> CalculatorModel v1_simulations_id_get(id)

Returns simulations refineries details

### Example
```python
from __future__ import print_function
import time
import refinerycalc
from refinerycalc.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = refinerycalc.SimulationsApi()
id = 'id_example' # str | 

try:
    # Returns simulations refineries details
    api_response = api_instance.v1_simulations_id_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimulationsApi->v1_simulations_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**CalculatorModel**](CalculatorModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_simulations_id_output_get**
> OutputTypeModel v1_simulations_id_output_get(id)

Retrieves a OutputModel for the given input simuation Id.

### Example
```python
from __future__ import print_function
import time
import refinerycalc
from refinerycalc.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = refinerycalc.SimulationsApi()
id = 'id_example' # str | Simulation Id

try:
    # Retrieves a OutputModel for the given input simuation Id.
    api_response = api_instance.v1_simulations_id_output_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimulationsApi->v1_simulations_id_output_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Simulation Id | 

### Return type

[**OutputTypeModel**](OutputTypeModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_simulations_id_refineries_advanced_options_patch**
> ApiResponse v1_simulations_id_refineries_advanced_options_patch(id, body=body)

Updates the advanced options for the given refineries

### Example
```python
from __future__ import print_function
import time
import refinerycalc
from refinerycalc.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = refinerycalc.SimulationsApi()
id = 'id_example' # str | simulation id
body = refinerycalc.AdvancedOptionsBatchRequest() # AdvancedOptionsBatchRequest |  (optional)

try:
    # Updates the advanced options for the given refineries
    api_response = api_instance.v1_simulations_id_refineries_advanced_options_patch(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimulationsApi->v1_simulations_id_refineries_advanced_options_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| simulation id | 
 **body** | [**AdvancedOptionsBatchRequest**](AdvancedOptionsBatchRequest.md)|  | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_simulations_id_refineries_crude_allocation_patch**
> ApiResponse v1_simulations_id_refineries_crude_allocation_patch(id, body=body)

Update Crude Allocation Value for One or More Refineries

### Example
```python
from __future__ import print_function
import time
import refinerycalc
from refinerycalc.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = refinerycalc.SimulationsApi()
id = 'id_example' # str | simulation id
body = refinerycalc.UpdateSimRefineryCrudeAllocationRequest() # UpdateSimRefineryCrudeAllocationRequest | the list of refineries with their crude allocations (optional)

try:
    # Update Crude Allocation Value for One or More Refineries
    api_response = api_instance.v1_simulations_id_refineries_crude_allocation_patch(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimulationsApi->v1_simulations_id_refineries_crude_allocation_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| simulation id | 
 **body** | [**UpdateSimRefineryCrudeAllocationRequest**](UpdateSimRefineryCrudeAllocationRequest.md)| the list of refineries with their crude allocations | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_simulations_id_refineries_crude_allocations_default_patch**
> ApiResponse v1_simulations_id_refineries_crude_allocations_default_patch(id, body=body)

Refinery set default value for crude compositions

### Example
```python
from __future__ import print_function
import time
import refinerycalc
from refinerycalc.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = refinerycalc.SimulationsApi()
id = 'id_example' # str | 
body = refinerycalc.RefineryUseDefaultRequestModel() # RefineryUseDefaultRequestModel |  (optional)

try:
    # Refinery set default value for crude compositions
    api_response = api_instance.v1_simulations_id_refineries_crude_allocations_default_patch(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimulationsApi->v1_simulations_id_refineries_crude_allocations_default_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**RefineryUseDefaultRequestModel**](RefineryUseDefaultRequestModel.md)|  | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_simulations_id_refineries_crude_prices_default_patch**
> ApiResponse v1_simulations_id_refineries_crude_prices_default_patch(id, body=body)

Refinery set default value for crude price

### Example
```python
from __future__ import print_function
import time
import refinerycalc
from refinerycalc.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = refinerycalc.SimulationsApi()
id = 'id_example' # str | 
body = refinerycalc.RefineryUseDefaultRequestModel() # RefineryUseDefaultRequestModel |  (optional)

try:
    # Refinery set default value for crude price
    api_response = api_instance.v1_simulations_id_refineries_crude_prices_default_patch(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimulationsApi->v1_simulations_id_refineries_crude_prices_default_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**RefineryUseDefaultRequestModel**](RefineryUseDefaultRequestModel.md)|  | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_simulations_id_refineries_crude_prices_patch**
> ApiResponse v1_simulations_id_refineries_crude_prices_patch(id, body=body)

Update Crude Prices for One or More Refineries

### Example
```python
from __future__ import print_function
import time
import refinerycalc
from refinerycalc.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = refinerycalc.SimulationsApi()
id = 'id_example' # str | simulation id
body = refinerycalc.UpdateSimRefineryCrudePricesRequest() # UpdateSimRefineryCrudePricesRequest | the list of refineries with their crude prices (optional)

try:
    # Update Crude Prices for One or More Refineries
    api_response = api_instance.v1_simulations_id_refineries_crude_prices_patch(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimulationsApi->v1_simulations_id_refineries_crude_prices_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| simulation id | 
 **body** | [**UpdateSimRefineryCrudePricesRequest**](UpdateSimRefineryCrudePricesRequest.md)| the list of refineries with their crude prices | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_simulations_id_refineries_endpoint_mode_patch**
> ApiResponse v1_simulations_id_refineries_endpoint_mode_patch(id, body=body)

Returns Success or failed

### Example
```python
from __future__ import print_function
import time
import refinerycalc
from refinerycalc.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = refinerycalc.SimulationsApi()
id = 'id_example' # str | 
body = refinerycalc.ChangeEndPointModeRequest() # ChangeEndPointModeRequest |  (optional)

try:
    # Returns Success or failed
    api_response = api_instance.v1_simulations_id_refineries_endpoint_mode_patch(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimulationsApi->v1_simulations_id_refineries_endpoint_mode_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**ChangeEndPointModeRequest**](ChangeEndPointModeRequest.md)|  | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_simulations_id_refineries_endpoints_default_patch**
> ApiResponse v1_simulations_id_refineries_endpoints_default_patch(id, body=body)

Refinery set default value for end points

### Example
```python
from __future__ import print_function
import time
import refinerycalc
from refinerycalc.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = refinerycalc.SimulationsApi()
id = 'id_example' # str | 
body = refinerycalc.RefineryUseDefaultRequestModel() # RefineryUseDefaultRequestModel |  (optional)

try:
    # Refinery set default value for end points
    api_response = api_instance.v1_simulations_id_refineries_endpoints_default_patch(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimulationsApi->v1_simulations_id_refineries_endpoints_default_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**RefineryUseDefaultRequestModel**](RefineryUseDefaultRequestModel.md)|  | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_simulations_id_refineries_get**
> GetRefineriesForSimulationResponse v1_simulations_id_refineries_get(id)

Retrieves a list of refineries for the given simulation.

### Example
```python
from __future__ import print_function
import time
import refinerycalc
from refinerycalc.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = refinerycalc.SimulationsApi()
id = 'id_example' # str | 

try:
    # Retrieves a list of refineries for the given simulation.
    api_response = api_instance.v1_simulations_id_refineries_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimulationsApi->v1_simulations_id_refineries_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**GetRefineriesForSimulationResponse**](GetRefineriesForSimulationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_simulations_id_refineries_intermediate_products_patch**
> ApiResponse v1_simulations_id_refineries_intermediate_products_patch(id, body=body)



### Example
```python
from __future__ import print_function
import time
import refinerycalc
from refinerycalc.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = refinerycalc.SimulationsApi()
id = 'id_example' # str | 
body = refinerycalc.RefineryChangeIntermediateProductsRequestModel() # RefineryChangeIntermediateProductsRequestModel |  (optional)

try:
    api_response = api_instance.v1_simulations_id_refineries_intermediate_products_patch(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimulationsApi->v1_simulations_id_refineries_intermediate_products_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**RefineryChangeIntermediateProductsRequestModel**](RefineryChangeIntermediateProductsRequestModel.md)|  | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_simulations_id_refineries_post**
> ApiResponse v1_simulations_id_refineries_post(id, body=body)

Adds a list of refineries to an existing simulation.

### Example
```python
from __future__ import print_function
import time
import refinerycalc
from refinerycalc.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = refinerycalc.SimulationsApi()
id = 'id_example' # str | The id of the simulation
body = refinerycalc.AddRefineriesToSimulationRequest() # AddRefineriesToSimulationRequest |  (optional)

try:
    # Adds a list of refineries to an existing simulation.
    api_response = api_instance.v1_simulations_id_refineries_post(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimulationsApi->v1_simulations_id_refineries_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the simulation | 
 **body** | [**AddRefineriesToSimulationRequest**](AddRefineriesToSimulationRequest.md)|  | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_simulations_id_refineries_product_prices_default_patch**
> ApiResponse v1_simulations_id_refineries_product_prices_default_patch(id, body=body)

Refinery set default value for product prices

### Example
```python
from __future__ import print_function
import time
import refinerycalc
from refinerycalc.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = refinerycalc.SimulationsApi()
id = 'id_example' # str | 
body = refinerycalc.RefineryUseDefaultRequestModel() # RefineryUseDefaultRequestModel |  (optional)

try:
    # Refinery set default value for product prices
    api_response = api_instance.v1_simulations_id_refineries_product_prices_default_patch(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimulationsApi->v1_simulations_id_refineries_product_prices_default_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**RefineryUseDefaultRequestModel**](RefineryUseDefaultRequestModel.md)|  | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_simulations_id_refineries_product_prices_patch**
> ApiResponse v1_simulations_id_refineries_product_prices_patch(id, body=body)

Simulation's refineries set product price

### Example
```python
from __future__ import print_function
import time
import refinerycalc
from refinerycalc.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = refinerycalc.SimulationsApi()
id = 'id_example' # str | 
body = refinerycalc.SaveRefineryProductPriceRequestModel() # SaveRefineryProductPriceRequestModel |  (optional)

try:
    # Simulation's refineries set product price
    api_response = api_instance.v1_simulations_id_refineries_product_prices_patch(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimulationsApi->v1_simulations_id_refineries_product_prices_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**SaveRefineryProductPriceRequestModel**](SaveRefineryProductPriceRequestModel.md)|  | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_simulations_id_refineries_refinery_id_crude_get**
> GetCalculatorRefineryCrudesResponse v1_simulations_id_refineries_refinery_id_crude_get(id, refinery_id)



### Example
```python
from __future__ import print_function
import time
import refinerycalc
from refinerycalc.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = refinerycalc.SimulationsApi()
id = 'id_example' # str | 
refinery_id = 56 # int | 

try:
    api_response = api_instance.v1_simulations_id_refineries_refinery_id_crude_get(id, refinery_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimulationsApi->v1_simulations_id_refineries_refinery_id_crude_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **refinery_id** | **int**|  | 

### Return type

[**GetCalculatorRefineryCrudesResponse**](GetCalculatorRefineryCrudesResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_simulations_id_refineries_refinery_id_delete**
> ApiResponse v1_simulations_id_refineries_refinery_id_delete(id, refinery_id)

Remove Refinery from an existing simulation.

### Example
```python
from __future__ import print_function
import time
import refinerycalc
from refinerycalc.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = refinerycalc.SimulationsApi()
id = 'id_example' # str | The id of the simulation
refinery_id = 56 # int | The id of the refinery

try:
    # Remove Refinery from an existing simulation.
    api_response = api_instance.v1_simulations_id_refineries_refinery_id_delete(id, refinery_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimulationsApi->v1_simulations_id_refineries_refinery_id_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the simulation | 
 **refinery_id** | **int**| The id of the refinery | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_simulations_id_refineries_refinery_id_endpoints_get**
> list[EndPointResponse] v1_simulations_id_refineries_refinery_id_endpoints_get(id, refinery_id)

Retrieves a list of Endpoints for the given input simuation Id and Refinery Id.

### Example
```python
from __future__ import print_function
import time
import refinerycalc
from refinerycalc.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = refinerycalc.SimulationsApi()
id = 'id_example' # str | 
refinery_id = 56 # int | 

try:
    # Retrieves a list of Endpoints for the given input simuation Id and Refinery Id.
    api_response = api_instance.v1_simulations_id_refineries_refinery_id_endpoints_get(id, refinery_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimulationsApi->v1_simulations_id_refineries_refinery_id_endpoints_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **refinery_id** | **int**|  | 

### Return type

[**list[EndPointResponse]**](EndPointResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_simulations_id_refineries_refinery_id_product_prices_get**
> list[ProductPriceModel] v1_simulations_id_refineries_refinery_id_product_prices_get(id, refinery_id)

Get product prices for a given simulation

### Example
```python
from __future__ import print_function
import time
import refinerycalc
from refinerycalc.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = refinerycalc.SimulationsApi()
id = 'id_example' # str | 
refinery_id = 56 # int | 

try:
    # Get product prices for a given simulation
    api_response = api_instance.v1_simulations_id_refineries_refinery_id_product_prices_get(id, refinery_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimulationsApi->v1_simulations_id_refineries_refinery_id_product_prices_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **refinery_id** | **int**|  | 

### Return type

[**list[ProductPriceModel]**](ProductPriceModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_simulations_id_refineries_refinery_id_units_get**
> RefineryUnitResponse v1_simulations_id_refineries_refinery_id_units_get(id, refinery_id)

Retrieves Units for a given Simulation and Refinery

### Example
```python
from __future__ import print_function
import time
import refinerycalc
from refinerycalc.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = refinerycalc.SimulationsApi()
id = 'id_example' # str | 
refinery_id = 56 # int | 

try:
    # Retrieves Units for a given Simulation and Refinery
    api_response = api_instance.v1_simulations_id_refineries_refinery_id_units_get(id, refinery_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimulationsApi->v1_simulations_id_refineries_refinery_id_units_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **refinery_id** | **int**|  | 

### Return type

[**RefineryUnitResponse**](RefineryUnitResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_simulations_id_refineries_units_bias_patch**
> ApiResponse v1_simulations_id_refineries_units_bias_patch(id, body=body)

Update simulation refinery unit bios

### Example
```python
from __future__ import print_function
import time
import refinerycalc
from refinerycalc.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = refinerycalc.SimulationsApi()
id = 'id_example' # str | simulation id
body = refinerycalc.RefineryChangeUnitRequestModel() # RefineryChangeUnitRequestModel |  (optional)

try:
    # Update simulation refinery unit bios
    api_response = api_instance.v1_simulations_id_refineries_units_bias_patch(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimulationsApi->v1_simulations_id_refineries_units_bias_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| simulation id | 
 **body** | [**RefineryChangeUnitRequestModel**](RefineryChangeUnitRequestModel.md)|  | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_simulations_id_refineries_units_default_patch**
> ApiResponse v1_simulations_id_refineries_units_default_patch(id, body=body)

Refinery set default value for units

### Example
```python
from __future__ import print_function
import time
import refinerycalc
from refinerycalc.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = refinerycalc.SimulationsApi()
id = 'id_example' # str | 
body = refinerycalc.RefineryUseDefaultRequestModel() # RefineryUseDefaultRequestModel |  (optional)

try:
    # Refinery set default value for units
    api_response = api_instance.v1_simulations_id_refineries_units_default_patch(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimulationsApi->v1_simulations_id_refineries_units_default_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**RefineryUseDefaultRequestModel**](RefineryUseDefaultRequestModel.md)|  | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_simulations_id_refineries_units_health_state_patch**
> ApiResponse v1_simulations_id_refineries_units_health_state_patch(id, body=body)

Update the health state of the specified units for the specified refineries in the given simulation

### Example
```python
from __future__ import print_function
import time
import refinerycalc
from refinerycalc.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = refinerycalc.SimulationsApi()
id = 'id_example' # str | simulation id
body = refinerycalc.HealthStateBatchRequest() # HealthStateBatchRequest |  (optional)

try:
    # Update the health state of the specified units for the specified refineries in the given simulation
    api_response = api_instance.v1_simulations_id_refineries_units_health_state_patch(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimulationsApi->v1_simulations_id_refineries_units_health_state_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| simulation id | 
 **body** | [**HealthStateBatchRequest**](HealthStateBatchRequest.md)|  | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_simulations_id_refineries_units_mode_patch**
> ApiResponse v1_simulations_id_refineries_units_mode_patch(id, body=body)

Update simulation refinery unit mode

### Example
```python
from __future__ import print_function
import time
import refinerycalc
from refinerycalc.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = refinerycalc.SimulationsApi()
id = 'id_example' # str | simulation id
body = refinerycalc.RefineryChangeUnitModeRequestModel() # RefineryChangeUnitModeRequestModel |  (optional)

try:
    # Update simulation refinery unit mode
    api_response = api_instance.v1_simulations_id_refineries_units_mode_patch(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimulationsApi->v1_simulations_id_refineries_units_mode_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| simulation id | 
 **body** | [**RefineryChangeUnitModeRequestModel**](RefineryChangeUnitModeRequestModel.md)|  | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_simulations_id_refineries_units_rate_patch**
> ApiResponse v1_simulations_id_refineries_units_rate_patch(id, body=body)

Update simulation refinery unit rate

### Example
```python
from __future__ import print_function
import time
import refinerycalc
from refinerycalc.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = refinerycalc.SimulationsApi()
id = 'id_example' # str | simulation id
body = refinerycalc.RefineryChangeUnitRequestModel() # RefineryChangeUnitRequestModel |  (optional)

try:
    # Update simulation refinery unit rate
    api_response = api_instance.v1_simulations_id_refineries_units_rate_patch(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimulationsApi->v1_simulations_id_refineries_units_rate_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| simulation id | 
 **body** | [**RefineryChangeUnitRequestModel**](RefineryChangeUnitRequestModel.md)|  | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_simulations_id_refineries_units_toggle_shutdown_status_patch**
> UnitToggleShutdownStatusResponseModel v1_simulations_id_refineries_units_toggle_shutdown_status_patch(id, body=body)

Update simulation refinery toggle unit status

### Example
```python
from __future__ import print_function
import time
import refinerycalc
from refinerycalc.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = refinerycalc.SimulationsApi()
id = 'id_example' # str | simulation id
body = refinerycalc.RefineryToggleUnitStatusRequestModel() # RefineryToggleUnitStatusRequestModel |  (optional)

try:
    # Update simulation refinery toggle unit status
    api_response = api_instance.v1_simulations_id_refineries_units_toggle_shutdown_status_patch(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimulationsApi->v1_simulations_id_refineries_units_toggle_shutdown_status_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| simulation id | 
 **body** | [**RefineryToggleUnitStatusRequestModel**](RefineryToggleUnitStatusRequestModel.md)|  | [optional] 

### Return type

[**UnitToggleShutdownStatusResponseModel**](UnitToggleShutdownStatusResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_simulations_id_refinery_change_endpoint_post**
> ApiResponse v1_simulations_id_refinery_change_endpoint_post(id, body=body)

Returns Success or failed

### Example
```python
from __future__ import print_function
import time
import refinerycalc
from refinerycalc.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = refinerycalc.SimulationsApi()
id = 'id_example' # str | 
body = refinerycalc.ChangeEndPointRequest() # ChangeEndPointRequest |  (optional)

try:
    # Returns Success or failed
    api_response = api_instance.v1_simulations_id_refinery_change_endpoint_post(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimulationsApi->v1_simulations_id_refinery_change_endpoint_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**ChangeEndPointRequest**](ChangeEndPointRequest.md)|  | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_simulations_id_rename_patch**
> ApiResponse v1_simulations_id_rename_patch(id, body=body)

Rename an existing simulation

### Example
```python
from __future__ import print_function
import time
import refinerycalc
from refinerycalc.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = refinerycalc.SimulationsApi()
id = 'id_example' # str | simulation id
body = refinerycalc.SimulationRenameRequestModel() # SimulationRenameRequestModel |  (optional)

try:
    # Rename an existing simulation
    api_response = api_instance.v1_simulations_id_rename_patch(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimulationsApi->v1_simulations_id_rename_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| simulation id | 
 **body** | [**SimulationRenameRequestModel**](SimulationRenameRequestModel.md)|  | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_simulations_id_run_post**
> RunSimulationResponseModel v1_simulations_id_run_post(id)

Run a simulation by Id

### Example
```python
from __future__ import print_function
import time
import refinerycalc
from refinerycalc.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = refinerycalc.SimulationsApi()
id = 'id_example' # str | simulation id

try:
    # Run a simulation by Id
    api_response = api_instance.v1_simulations_id_run_post(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimulationsApi->v1_simulations_id_run_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| simulation id | 

### Return type

[**RunSimulationResponseModel**](RunSimulationResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_simulations_id_run_status_get**
> RunSimulationResponseModel v1_simulations_id_run_status_get(id)

Get simulation run status

### Example
```python
from __future__ import print_function
import time
import refinerycalc
from refinerycalc.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = refinerycalc.SimulationsApi()
id = 'id_example' # str | 

try:
    # Get simulation run status
    api_response = api_instance.v1_simulations_id_run_status_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimulationsApi->v1_simulations_id_run_status_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**RunSimulationResponseModel**](RunSimulationResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_simulations_id_schedule_delete**
> ApiResponse v1_simulations_id_schedule_delete(id)

Delete a simulation schedule.

### Example
```python
from __future__ import print_function
import time
import refinerycalc
from refinerycalc.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = refinerycalc.SimulationsApi()
id = 'id_example' # str | The id of the Simulation

try:
    # Delete a simulation schedule.
    api_response = api_instance.v1_simulations_id_schedule_delete(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimulationsApi->v1_simulations_id_schedule_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the Simulation | 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_simulations_id_schedule_post**
> ScheduleJobResponse v1_simulations_id_schedule_post(id, body=body)

Schedule a simulation to run

### Example
```python
from __future__ import print_function
import time
import refinerycalc
from refinerycalc.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = refinerycalc.SimulationsApi()
id = 'id_example' # str | Simulation Id
body = refinerycalc.ScheduleSimulationRequestModel() # ScheduleSimulationRequestModel | SimulationRunRequestModel (optional)

try:
    # Schedule a simulation to run
    api_response = api_instance.v1_simulations_id_schedule_post(id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimulationsApi->v1_simulations_id_schedule_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| Simulation Id | 
 **body** | [**ScheduleSimulationRequestModel**](ScheduleSimulationRequestModel.md)| SimulationRunRequestModel | [optional] 

### Return type

[**ScheduleJobResponse**](ScheduleJobResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_simulations_post**
> CreateSimulationResponse v1_simulations_post(body=body)

Create a new simulation from a given list of refineries

### Example
```python
from __future__ import print_function
import time
import refinerycalc
from refinerycalc.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = refinerycalc.SimulationsApi()
body = refinerycalc.CreateSimulationRequest() # CreateSimulationRequest |  (optional)

try:
    # Create a new simulation from a given list of refineries
    api_response = api_instance.v1_simulations_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimulationsApi->v1_simulations_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateSimulationRequest**](CreateSimulationRequest.md)|  | [optional] 

### Return type

[**CreateSimulationResponse**](CreateSimulationResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_simulations_schedules_get**
> SimulationScheduleResponseModel v1_simulations_schedules_get()

Retrieves list of the scheduled simulations.

### Example
```python
from __future__ import print_function
import time
import refinerycalc
from refinerycalc.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = refinerycalc.SimulationsApi()

try:
    # Retrieves list of the scheduled simulations.
    api_response = api_instance.v1_simulations_schedules_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimulationsApi->v1_simulations_schedules_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**SimulationScheduleResponseModel**](SimulationScheduleResponseModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **v1_simulations_simulation_id_refineries_kero_mode_patch**
> ApiResponse v1_simulations_simulation_id_refineries_kero_mode_patch(simulation_id, body=body)

Update refinery kero mode

### Example
```python
from __future__ import print_function
import time
import refinerycalc
from refinerycalc.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = refinerycalc.SimulationsApi()
simulation_id = 'simulation_id_example' # str | simulation id
body = refinerycalc.RefineryChangeKeroModeRequestModel() # RefineryChangeKeroModeRequestModel |  (optional)

try:
    # Update refinery kero mode
    api_response = api_instance.v1_simulations_simulation_id_refineries_kero_mode_patch(simulation_id, body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SimulationsApi->v1_simulations_simulation_id_refineries_kero_mode_patch: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **simulation_id** | **str**| simulation id | 
 **body** | [**RefineryChangeKeroModeRequestModel**](RefineryChangeKeroModeRequestModel.md)|  | [optional] 

### Return type

[**ApiResponse**](ApiResponse.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

