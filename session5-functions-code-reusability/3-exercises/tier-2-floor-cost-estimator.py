def estimate_cost(area, cost_per_m2):
    if area > 0 and cost_per_m2 > 0:
        return area * cost_per_m2
    else:
        return None

def print_floor_cost(index, area, cost_per_m2):
    cost = estimate_cost(area, cost_per_m2)
    if cost is not None:
        print(f"Floor {index + 1} - Total Cost: €{cost}")
    else:
        print(f"Floor {index + 1} - Invalid input")

floor_areas = [30.0, -5.0, 60.0]
costs_per_m2 = [25.0, 30.0, 22.0]

for i, (area, cost) in enumerate(zip(floor_areas, costs_per_m2)):
    print_floor_cost(i, area, cost)