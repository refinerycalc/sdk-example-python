from python.refinerycalc.api.simulations_api import SimulationsApi
from python.refinerycalc.api_client import ApiClient
from python.refinerycalc import Configuration
import os


class RefineryCalc:
    def __init__(self):
        config = Configuration()
        config.api_key = os.environ["RefineryCalc_Api_Key"]
        config.host = os.environ["RefineryCalc_Api_Url"]
        self.__apiClient = ApiClient(configuration=config, header_name="x-api-key", header_value=config.api_key)
        self.api = SimulationsApi(self.__apiClient)
