# Simulation's refineries set product price
# v1_simulations_id_refineries_product_prices_patch

from initialization import RefineryCalcExampleClient
from refinerycalc.models.save_refinery_product_price_request_model import SaveRefineryProductPriceRequestModel
from refinerycalc.models.refinery_product_price import RefineryProductPrice
from refinerycalc.models.refinery_product_price_item import RefineryProductPriceItem

client = RefineryCalcExampleClient()

def get_simulation_refinery_id(simulation_id):
    simulation_refineries = client.simulations.v1_simulations_id_refineries_get(simulation_id)
    return simulation_refineries.refineries[0].id
   
def get_simulation_refinery_price_id(simulation_id, refinery_id, price_index):
    simulation_refinery_products = client.simulations.v1_simulations_id_refineries_refinery_id_product_prices_get(simulation_id, refinery_id)
    print(simulation_refinery_products)
    return simulation_refinery_products[price_index].id

if __name__ == "__main__":
    # create an instance of the API class
    id = '<SIMULATION ID FROM RUN SIMULATION>' # str | simulation id
    req = SaveRefineryProductPriceRequestModel() # RefineryChangeUnitRequestModel |  (optional)
    simulation_refinery_id = get_simulation_refinery_id(id)
    refineries = []
    refinery =  RefineryProductPrice()
    refinery.apply_all = False
    refinery.refinery_id = simulation_refinery_id
    products = []
    product = RefineryProductPriceItem()
    product.price_id = get_simulation_refinery_price_id(id, simulation_refinery_id, 0)
    product.price = 5.10 # Need to change as per your need
    products.append(product)

    refinery.products = products
    refineries.append(refinery)
    req.refineries = refineries
    #Update Crudes for One or More Refineries
    api_response = client.simulations.v1_simulations_id_refineries_product_prices_patch(id, body=req)
    if api_response.success:
        print(api_response)
