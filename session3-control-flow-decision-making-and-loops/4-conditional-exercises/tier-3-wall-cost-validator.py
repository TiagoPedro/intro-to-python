wall_area = 35.0
cost_per_m2 = 25.0
is_load_bearing = True

if wall_area <= 0 or cost_per_m2 <= 0:
    print("Invalid input values.")
else:
    if is_load_bearing:
        multiplier = 1.2
    else:
        multiplier = 1.0

    total_cost = wall_area * cost_per_m2 * multiplier
    print("Total cost:", total_cost)