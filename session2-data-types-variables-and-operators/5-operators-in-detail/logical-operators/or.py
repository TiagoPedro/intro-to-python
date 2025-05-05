# Check if a room needs ventilation
co2_level_high = True     # CO2 level exceeds threshold
temp_too_high = False     # Temperature is within normal range

needs_ventilation = co2_level_high or temp_too_high
print("Room needs ventilation:", needs_ventilation)  # True (because CO2 is high)
