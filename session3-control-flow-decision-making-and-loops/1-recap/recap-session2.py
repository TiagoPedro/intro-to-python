floor_area = 30
cost_per_m2 = 25
has_reinforcement = True

# Using arithmetic and logical operators with logical AND
reinforcement_multiplier = 1.0 + (0.2 * has_reinforcement)

# Relational operators
is_large_floor = floor_area > 25  # Greater than
is_medium_floor = floor_area == 30  # Equal to

total_cost = floor_area * cost_per_m2 * reinforcement_multiplier

print("Total Cost:", total_cost)

# Logical operators with OR
has_heating = True
has_cooling = True

has_climate_control = has_heating and has_cooling

print("Has climate control:", has_climate_control)
