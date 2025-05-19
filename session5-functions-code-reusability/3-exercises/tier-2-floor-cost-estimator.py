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
index_list = [0, 1, 2]

for i in index_list:
    area = floor_areas[i] # i = 0 then area = 30.0
    cost = costs_per_m2[i]
    print_floor_cost(i, area, cost)




# for i, (area, cost) in enumerate(zip(floor_areas, costs_per_m2)):
#     print_floor_cost(i, area, cost)
    
# for i, area in enumerate(floor_areas):
#     print_floor_cost(i, area, 10)
    
# 1st iteration:
# i = 0
# area = 30.0
# cost = 25.0
# print_floor_cost(0, 30.0, 25.0)

#2nd iteration:
# i = 1
# area = -5.0
# print_floot_cost(1, -5.0, 10)

#3d iteration:
# i = 2
# area = 60.0
# print_floot_cost(2, 60.0, 10)