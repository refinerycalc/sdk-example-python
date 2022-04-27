from initialization import RefineryCalc
import time

if __name__ == "__main__":
    client = RefineryCalc()
    simulation_id = "10aef717-d138-4a01-b366-2afc8cdf077a"
    response = client.api.v1_simulations_id_run_post(simulation_id)
    if response.success:
        print(f"running simulation with id {simulation_id}")
        done = False
        while not done:
            status = client.api.v1_simulations_id_run_status_get(simulation_id)
            done = (status.is_solved or status.is_cancelled) and not status.is_solving
            if done or status.is_solved:
                break
            print(f"status ({round(status.percent_solved, 2)}%): {status.solve_status}")
            time.sleep(5)
        print("success")
    else:
        print(" run failed with error: " + response.message)