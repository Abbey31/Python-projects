def calculate_bake_time(expected_bake_time,remaining_bake_time):
    EXPECTED_BAKE_TIME = expected_bake_time - remaining_bake_time
    return EXPECTED_BAKE_TIME



print(calculate_bake_time(20,10))