# Update simulation refinery unit bios
# v1_simulations_id_refineries_units_bias_patch

from initialization import RefineryCalcExampleClient
from refinerycalc.models.refinery_change_unit_request_model import RefineryChangeUnitRequestModel
from refinerycalc.models.refinery_change_unit import RefineryChangeUnit
from refinerycalc.models.refinery_unit_item import RefineryUnitItem

client = RefineryCalcExampleClient()

def get_simulation_refinery_id(simulation_id):
    simulation_refineries = client.simulations.v1_simulations_id_refineries_get(simulation_id)
    return simulation_refineries.refineries[0].id
   
def get_simulation_refinery_units_id(simulation_id, refinery_id, unit_name):
    simulation_refinery_units = client.simulations.v1_simulations_id_refineries_refinery_id_units_get(simulation_id, refinery_id)
    alky_units = [unit for unit in simulation_refinery_units.results if unit.name == unit_name]
    return alky_units[0].id

if __name__ == "__main__":
    # create an instance of the API class
    id = '<SIMULATION ID FROM RUN SIMULATION>' # str | simulation id
    req = RefineryChangeUnitRequestModel() # RefineryChangeUnitRequestModel |  (optional)
    simulation_refinery_id = get_simulation_refinery_id(id)
    refineries = []
    refinery =  RefineryChangeUnit()
    refinery.apply_all = False
    refinery.refinery_id = simulation_refinery_id
    units = []

    unit = RefineryUnitItem()
    unit.unit_id = get_simulation_refinery_units_id(id, simulation_refinery_id, 'Alky')
    unit.value = 1500 # Need to change as per your need
    units.append(unit)

    unit = RefineryUnitItem()
    unit.unit_id = get_simulation_refinery_units_id(id, simulation_refinery_id, 'Aromatics')
    unit.value = 2400 # Need to change as per your need
    units.append(unit)

    refinery.units = units
    refineries.append(refinery)
    req.refineries = refineries
    #Update Crudes for One or More Refineries
    api_response = client.simulations.v1_simulations_id_refineries_units_bias_patch(id, body=req)
    if api_response.success:
        print(api_response)
