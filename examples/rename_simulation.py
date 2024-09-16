from refinerycalc.models.simulation_rename_request_model import SimulationRenameRequestModel
from initialization import RefineryCalcExampleClient

if __name__ == "__main__":
    client = RefineryCalcExampleClient()
    req = SimulationRenameRequestModel("my new name")
    response = client.simulations.v1_simulations_id_rename_patch("10aef717-d138-4a01-b366-2afc8cdf077a", body=req)
    print(response)
