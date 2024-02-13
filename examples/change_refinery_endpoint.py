from python.refinerycalc.models.change_end_point_request import ChangeEndPointRequest
from initialization import RefineryCalc
from python.refinerycalc.models.refinery_end_point import RefineryEndPoint
from python.refinerycalc.models.refinery_end_point_item import RefineryEndPointItem

if __name__ == "__main__":
    # you can get refinery ids with a separate call.
    # hardcoded here for convenience
    simulation_id = "088534b8-f067-46d0-981b-c198d0d5c03f"

    endpoint1 = RefineryEndPointItem()
    endpoint1.value = 680
    endpoint1.end_point_id = 566530

    refinery1 = RefineryEndPoint()
    refinery1.refinery_id = 214260
    refinery1.apply_all = True
    refinery1.end_points = [endpoint1]

    refs = [refinery1]
    client = RefineryCalc()
    req = ChangeEndPointRequest()
    req.refineries = refs
    # 0 is default datasource and 1 for IIR
    req.data_source = 0
    req.name = "my first1 simulation"
    req.is_time_series = False
    response = client.simulations.v1_simulations_id_refinery_change_endpoint_post(id=simulation_id, body=req)
    if response.success:
        print(response.simulation_id)
