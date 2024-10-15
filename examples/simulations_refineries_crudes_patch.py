# Update Crudes for One or More Refineries
# v1_simulations_id_refineries_crudes_patch

from initialization import RefineryCalcExampleClient
from refinerycalc.models.update_simulation_refinery_crude_request import UpdateSimulationRefineryCrudeRequest
from refinerycalc.models.refinery_crude_item import RefineryCrudeItem
from refinerycalc.models.crude_item import CrudeItem

client = RefineryCalcExampleClient()

def get_simulation_refinery_id(simulation_id):
    simulation_refineries = client.simulations.v1_simulations_id_refineries_get(simulation_id)
    return simulation_refineries.refineries[0].id
   
def get_simulation_refinery_crude_id(simulation_id, refinery_id):
    simulation_refinery_crudes = client.simulations.v1_simulations_id_refineries_refinery_id_crude_get(simulation_id, refinery_id)
    print(simulation_refinery_crudes)
    return simulation_refinery_crudes.calculator_refinery_crudes[0].id


if __name__ == "__main__":
    # create an instance of the API class
    id = '<SIMULATION ID FROM RUN SIMULATION>' # str | simulation id
    simulation_refinery_id = get_simulation_refinery_id(id)
    req = UpdateSimulationRefineryCrudeRequest() # UpdateSimulationRefineryCrudeRequest | the list of refineries with refinery crude ids and crudes (optional)
    refineries = []
    refinery =  RefineryCrudeItem()
    refinery.apply_all = False
    refinery.refinery_id = simulation_refinery_id
    crudes = []
    crude = CrudeItem()
    crude.crude_id = 276 # Need to change as per your need
    crude.refinery_crude_id = get_simulation_refinery_crude_id(id, simulation_refinery_id)
    crudes.append(crude)
    refinery.crudes = crudes
    refineries.append(refinery)
    req.refineries = refineries
    # Update Crudes for One or More Refineries
    api_response = client.simulations.v1_simulations_id_refineries_crudes_patch(id, body=req)
    if api_response.success:
        print(api_response)
