# Check if a door is accessible for wheelchairs
door_width = 0.9   # meters
has_ramp = True
wheelchair_accessible = (door_width >= 0.8) and has_ramp
print("Door is wheelchair accessible:", wheelchair_accessible)  # True