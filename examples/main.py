from initialization import RefineryCalc

if __name__ == "__main__":
    refs = [7, 8, 9, 10]
    client = RefineryCalc(refs)
    simulation_id = client.create_simulation("trend simulation")
    if simulation_id is not None:
        client.run_simulation(simulation_id)
        client.rename_simulation("Justman")
