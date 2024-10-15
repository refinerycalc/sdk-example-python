# Update Crude Prices for One or More Refineries
# v1_simulations_id_refineries_crude_prices_patch

from initialization import RefineryCalcExampleClient
from refinerycalc.models.update_sim_refinery_crude_prices_request import UpdateSimRefineryCrudePricesRequest
from refinerycalc.models.refinery_crude_price import RefineryCrudePrice
from refinerycalc.models.crude_price import CrudePrice

client = RefineryCalcExampleClient()

def get_simulation_refinery_id(simulation_id):
    simulation_refineries = client.simulations.v1_simulations_id_refineries_get(simulation_id)
    return simulation_refineries.refineries[0].id
   
def get_simulation_refinery_crude_id(simulation_id, refinery_id, crude_index):
    simulation_refinery_crudes = client.simulations.v1_simulations_id_refineries_refinery_id_crude_get(simulation_id, refinery_id)
    print(simulation_refinery_crudes)
    return simulation_refinery_crudes.calculator_refinery_crudes[crude_index].id


if __name__ == "__main__":
    # create an instance of the API class
    id = '<SIMULATION ID FROM RUN SIMULATION>' # str | simulation id
    req = UpdateSimRefineryCrudePricesRequest() # UpdateSimRefineryCrudePricesRequest | the list of refineries with their crude prices (optional)
    simulation_refinery_id = get_simulation_refinery_id(id)
    refineries = []
    refinery =  RefineryCrudePrice()
    refinery.apply_all = False
    refinery.refinery_id = simulation_refinery_id
    crudes = []
    
    crude = CrudePrice()
    crude.crude_id = get_simulation_refinery_crude_id(id, simulation_refinery_id, 0)
    crude.price = 66.66 # Need to change as per your need
    crude.freight = 0.22 # Need to change as per your need
    crudes.append(crude)

    crude = CrudePrice()
    crude.crude_id = get_simulation_refinery_crude_id(id, simulation_refinery_id, 4)
    crude.price = 55.55 # Need to change as per your need
    crude.freight = 0.55 # Need to change as per your need
    crudes.append(crude)

    refinery.crudes = crudes
    refineries.append(refinery)
    req.refineries = refineries
    # Update Crudes for One or More Refineries
    api_response = client.simulations.v1_simulations_id_refineries_crude_prices_patch(id, body=req)
    if api_response.success:
        print(api_response)
