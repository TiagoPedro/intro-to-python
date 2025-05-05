floor_areas = [30.0, -5.0, 60.0]
costs_per_m2 = [25.0, 30.0, 22.0]

for i, area in enumerate(floor_areas):
    cost = costs_per_m2[i]
    floor_num = i + 1
    
    if area > 0 and cost > 0:
        total_cost = area * cost
        print("Floor", floor_num, "- Total Cost: €", total_cost)
    else:
        print("Floor", floor_num, "- Invalid input")
