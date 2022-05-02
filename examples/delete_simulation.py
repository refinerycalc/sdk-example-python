from initialization import RefineryCalc

if __name__ == "__main__":
    client = RefineryCalc()
    response = client.simulations.v1_simulations_id_delete("fdbc00ff-2d81-4151-98e5-0593db6c52b7")
    if response.success:
        print("delete success")
    else:
        print("delete failed with error: " + response.message)