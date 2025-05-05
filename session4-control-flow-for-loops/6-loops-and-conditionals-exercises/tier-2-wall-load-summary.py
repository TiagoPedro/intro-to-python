wall_areas = [12.0, 10.0, 15.5]
is_load_bearing = [True, False, True]
density = 50.0  # kg/m²

for i in range(len(wall_areas)):
    area = wall_areas[i]
    load_bearing = is_load_bearing[i]
    if load_bearing:
      weight = area * density
    else:
      weight = 0.0
    print("Wall", i + 1, "- Load-bearing:", load_bearing, "| Weight:", weight, "kg")