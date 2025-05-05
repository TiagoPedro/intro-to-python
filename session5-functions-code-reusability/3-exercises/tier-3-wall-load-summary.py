def calculate_wall_weight(area, is_load_bearing, density):
    # return area * density if is_load_bearing else 0.0
    if is_load_bearing:
        return area * density
    else:
        return 0.0
    
def format_wall_summary(index, is_load_bearing, weight):
    base_summary = "Wall " + str(index + 1) + " - Load-bearing: " + str(is_load_bearing)
    if is_load_bearing:
        summary = base_summary + (" | Weight: " + str(weight) + " kg")
    else:
        summary = base_summary
    return summary
  

def summarize_wall(index, area, is_load_bearing, density):
    weight = calculate_wall_weight(area, is_load_bearing, density)
    summary = format_wall_summary(index, is_load_bearing, weight)
    print(summary)

wall_areas = [12.0, 10.0, 15.5]
is_load_bearing = [True, False, True]
density = 50.0

for i in range(len(wall_areas)):
    summarize_wall(i, wall_areas[i], is_load_bearing[i], density)