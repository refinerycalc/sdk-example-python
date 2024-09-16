from refinerycalc.api import refineries_api
from initialization import RefineryCalcExampleClient

if __name__ == "__main__":
    client = RefineryCalcExampleClient()
    response = client.refineries.v1_refineries_get()
    if response.success:
        print("success")
    else:
        print("failed with error: " + response.message)