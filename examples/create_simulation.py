from python.refinerycalc.models.create_simulation_request import CreateSimulationRequest
from initialization import RefineryCalc

if __name__ == "__main__":
    # you can get refinery ids with a separate call.
    # hardcoded here for convenience
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
