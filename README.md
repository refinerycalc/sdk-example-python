#Refinery Calc SDK Examples
This repository contains some examples on how to use the Refinery Calc Python SDK client which wraps the Refinery Calc API.

###Initialization
```python
class RefineryCalc:
    def __init__(self):
        config = Configuration()
        config.api_key = os.environ["RefineryCalc_Api_Key"]
        config.host = os.environ["RefineryCalc_Api_Url"]
        self.__apiClient = ApiClient(configuration=config, header_name="x-api-key", header_value=config.api_key)
        self.api = SimulationsApi(self.__apiClient)
```
`RefineryCalc_Api_Url` in production should be `https://api.refinerycalc.com`

###Create Simulation
to create a new simulation, you will need the list of refineries that will be used in that simulation. See the sample code below:
```python
    refs = [7, 8, 9, 10]
    client = RefineryCalc()
    req = CreateSimulationRequest()
    req.refineries = refs
    # 0 is default datasource and 1 for IIR
    req.data_source = 0
    req.name = "my new simulation"
    req.is_time_series = False
    response = client.api.v1_simulations_post(body=req)
    if response.success:
        print(response.simulation_id)
```
