# Refinery Calc SDK Examples

This repository contains some examples on how to use the Refinery Calc Python SDK client which wraps the Refinery Calc API.

### Getting Started
* Clone the repository 
* cd into the root directory
* create a python virtual environment
```
python -m venv .venv
```
Activate the virtual environment (macOS)
```
source .venv/bin/activate
```
Activate the virtual environment (Windows)
```
.venv\Scripts\activate
```
Install the Refinery Calc SDK
```
pip install refinerycalc-api
```
### Initialization

#### Api Key
Ensure you add your API Key to an Environment Variable `RefineryCalc_Api_Key`

```python
class RefineryCalcExampleClient:
    def __init__(self):
        # Get API key and URL from environment variables
        api_key = os.getenv("RefineryCalc_Api_Key")
        api_url = os.getenv("RefineryCalc_Api_Url", "https://api.refinerycalc.com")  # Default URL if not set
        
        # Error handling for missing API key
        if api_key is None:
            raise ValueError("API key is not set. Please set RefineryCalc_Api_Key in your environment.")
        
        # Set up configuration
        config = Configuration()
        config.api_key = api_key
        config.host = api_url
        
        # Initialize the API client
        self.__apiClient = ApiClient(configuration=config, header_name="x-api-key", header_value=config.api_key)
        
        # Set up APIs
        self.simulations = SimulationsApi(self.__apiClient)
        self.refineries = RefineriesApi(self.__apiClient)
        self.productPrices = ProductPricesApi(self.__apiClient)
```


### Create Simulation
to create a new simulation, you will need the list of refineries that will be used in that simulation. See the sample code below:

```python
    refs = [7, 8, 9, 10]
client = RefineryCalcExampleClient()
req = CreateSimulationRequest()
req.refineries = refs
# 0 is default datasource and 1 for IIR
req.data_source = 0
req.name = "my new simulation"
req.is_time_series = False
response = client.simulations.v1_simulations_post(body=req)
if response.success:
    print(response.simulation_id)
```
