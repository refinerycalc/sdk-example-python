from python.refinerycalc.models.create_simulation_request import CreateSimulationRequest
from python.refinerycalc.models.time_series_day import TimeSeriesDay
from python.refinerycalc.models.timeseries_crudes import TimeseriesCrudes
from python.refinerycalc.models.timeseries_crude_reference import TimeseriesCrudeReference
from python.refinerycalc.models.timeseries_product_prices import TimeseriesProductPrices
from python.refinerycalc.models.timeseries_advanced_options import TimeseriesAdvancedOptions
from initialization import RefineryCalc

client = RefineryCalc()


def get_product_prices(days: int):
    prices = client.productPrices.v1_product_prices_get()
    price = TimeseriesProductPrices()
    for p in prices:
        if p.name == "Natural Gas":
            price.natural_gas = p.value
        elif p.name == "Refinery Gas":
            price.refinery_gas = p.value
        elif p.name == "H2 Product":
            price.h2_prod = p.value
        elif p.name == "H2 Fuel":
            price.h2_fuel = p.value
        elif p.name == "Propane":
            price.propane = p.value
        elif p.name == "Butane":
            price.butane = p.value
        elif p.name == "Regular Gasoline":
            price._reg_gasoline = p.value
        elif p.name == "Premium Gasoline":
            price._prem_gasoline = p.value
        elif p.name == "Kerosene":
            price.kerosene = p.value
        elif p.name == "Ultra Low Sulphur Diesel":
            price.ulsd = p.value
        elif p.name == "Heating Oil":
            price.heating_oil = p.value
        elif p.name == "Heavy Fuel Oil":
            price.heavy_fuel_oil = p.value
        elif p.name == "Asphalt":
            price.asphalt = p.value
        elif p.name == "Lubes":
            price.lubes = p.value
        elif p.name == "Benzene":
            price.benzene = p.value
        elif p.name == "Xylene":
            price.xylene = p.value
        elif p.name == "Pitch":
            price.pitch = p.value
        elif p.name == "Naphtha":
            price.naphtha = p.value
        elif p.name == "Coke":
            price.coke = p.value
        elif p.name == "Sulfur":
            price.sulfur = p.value
        elif p.name == "Sour Diesel":
            price.sour_diesel = p.value
        elif p.name == "Gas Oil":
            price.gas_oil = p.value
        elif p.name == "Methanol":
            price.methanol = p.value
        elif p.name == "MTBE":
            price.mtbe = p.value
        elif p.name == "Cumene":
            price.cumene = p.value
        elif p.name == "Sour Gas Oil":
            price.sour_gas_oil = p.value
        elif p.name == "Sour Resid":
            price.sour_resid = p.value
        elif p.name == "Alkylate":
            price.alkylate = p.value
        elif p.name == "Toluene":
            price.toluene = p.value
    # use the same product price for each day
    return [price for i in range(days)]


def get_crude_by_refinery_id(refinery_id: int, days: int):
    # refinery_crude = client.refineries.v1_refineries_crude_id_get(refinery_id)
    crude = TimeseriesCrudes()

    crude1 = TimeseriesCrudeReference()
    crude1.name = "EagleFord"
    crude1.id  = 286
    crude1.price = 102.59
    crude1.percentage = .2

    crude2 = TimeseriesCrudeReference()
    crude2.name = "HLS"
    crude2.id = 293
    crude2.price = 104.9163602144
    crude2.percentage = .2

    crude3 = TimeseriesCrudeReference()
    crude3.name = "LLS"
    crude3.id = 267
    crude3.price = 107.07
    crude3.percentage = .2

    crude4 = TimeseriesCrudeReference()
    crude4.name = "Mars"
    crude4.id = 265
    crude4.price = 103.24
    crude4.percentage = .2

    crude5 = TimeseriesCrudeReference()
    crude5.name = "Mars"
    crude5.id = 265
    crude5.price = 103.24
    crude5.percentage = .2

    crude.crude1 = crude1
    crude.crude2 = crude2
    crude.crude3 = crude3
    crude.crude4 = crude4
    crude.crude5 = crude5

    return [[crude] for i in range(days)]

def create_time_series_simulation():
    # you can get refinery ids with a separate call.
    # hardcoded here for convenience
    refineryId = 121
    refs = [refineryId]
    req = CreateSimulationRequest()
    req.refineries = refs
    # 0 is default datasource and 1 for IIR
    req.data_source = 0
    req.name = "time series simulation"
    req.is_time_series = True
    num_of_days = 365
    timeSeriesDays = []
    crude_list = get_crude_by_refinery_id(refineryId, num_of_days)
    run_modes = [0 for i in range(num_of_days)]
    product_prices = get_product_prices(num_of_days)
    for i in range(num_of_days):
        day = TimeSeriesDay()
        advancedOptions = TimeseriesAdvancedOptions()
        advancedOptions.purchase_vgo = 6
        day.advanced_options = advancedOptions
        day.crudes = crude_list
        day.product_prices = product_prices
        timeSeriesDays.append(day)
    req.time_series_days = timeSeriesDays
    response = client.simulations.v1_simulations_post(body=req)
    if response.success:
        print(response.simulation_id)


if __name__ == "__main__":
    create_time_series_simulation()
