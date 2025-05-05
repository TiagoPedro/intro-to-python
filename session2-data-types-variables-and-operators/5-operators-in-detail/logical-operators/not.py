# Check if a room meets minimum height requirements
current_height = 3.0  # meters
meets_min_height = current_height >= 2.4  # False (2.4m is minimum)
needs_redesign = not meets_min_height  # True (needs redesign since height requirement not met)
print("Room needs height redesign:", needs_redesign)
