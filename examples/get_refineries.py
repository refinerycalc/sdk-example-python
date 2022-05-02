from python.refinerycalc.api import refineries_api
from initialization import RefineryCalc

if __name__ == "__main__":
    client = RefineryCalc()
    response = client.refineries.v1_refineries_get()
    if response.success:
        print("success")
    else:
        print("failed with error: " + response.message)