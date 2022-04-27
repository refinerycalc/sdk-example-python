from python.refinerycalc.api.simulations_api import SimulationsApi
from python.refinerycalc.api_client import ApiClient
from python.refinerycalc.models.simulation_rename_request_model import SimulationRenameRequestModel
from python.refinerycalc import Configuration
import os


class RefineryCalc:
    def __init__(self):
        config = Configuration()
        config.api_key = os.environ["RefineryCalc_Api_Key"]
        config.host = os.environ["RefineryCalc_Api_Url"]
        self.__apiClient = ApiClient(configuration=config, header_name="x-api-key", header_value=config.api_key)
        self.api = SimulationsApi(self.__apiClient)

    def rename_simulation(self, new_name: str):
        req = SimulationRenameRequestModel()
        req.name = new_name
        response = self.api.v1_simulations_id_rename_patch(body=req)
        if response.success:
            return response.new_name
        return "fail"