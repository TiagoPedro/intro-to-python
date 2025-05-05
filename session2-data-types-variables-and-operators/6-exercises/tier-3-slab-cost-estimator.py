# Variable definitions with correct naming and casting
project_name = "West Wing"
slab_length = float("10.0")
slab_width = float("12")
cost_per_m2 = float("40.5")
has_reinforcement = True  # manually changed from "yes" to a boolean

# Area calculation
total_area = slab_length * slab_width

# Reinforcement multiplier logic (1.2 if True, 1.0 if False)
reinforcement_multiplier = 1.2 * has_reinforcement + 1.0 * (not has_reinforcement)

# Total cost calculation
total_cost = total_area * cost_per_m2 * reinforcement_multiplier

# Output
print("Project:", project_name)
print("Total area:", total_area, "m2")
print("Reinforcement included:", has_reinforcement)
print("Total cost: €" + str(total_cost))