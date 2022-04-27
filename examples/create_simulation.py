from initialization import RefineryCalc


def create_simulation(self, name: str):
    req = create_simulation()
    req.refineries = self.refineries
    req.data_source = 0
    req.name = name
    req.is_time_series = False
    response = self.api.v1_simulations_post(body=req)
    if response.success:
        return response.simulation_id
    return None

if __name__ == "__main__":
    refs = [7, 8, 9, 10]
    client = RefineryCalc(refs)
    simulation_id = client.create_simulation("sam simulation")
    if simulation_id is not None:
        client.run_simulation(simulation_id)
