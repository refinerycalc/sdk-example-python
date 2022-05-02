from python.refinerycalc.api.simulations_api import SimulationsApi
from python.refinerycalc.api.refineries_api import RefineriesApi
from python.refinerycalc.api_client import ApiClient
from python.refinerycalc import Configuration
from python.refinerycalc.api.product_prices_api import ProductPricesApi
import os

class RefineryCalc:
    def __init__(self):
        config = Configuration()
        config.api_key = os.environ["RefineryCalc_Api_Key"]
        config.host = os.environ["RefineryCalc_Api_Url"]
        self.__apiClient = ApiClient(configuration=config, header_name="x-api-key", header_value=config.api_key)
        self.simulations = SimulationsApi(self.__apiClient)
        self.refineries = RefineriesApi(self.__apiClient)
        self.productPrices = ProductPricesApi(self.__apiClient)
