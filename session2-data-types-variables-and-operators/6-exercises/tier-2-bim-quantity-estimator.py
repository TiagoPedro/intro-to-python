# Wall 1
length1 = 4.0
height1 = 3.0
material_density1 = 20.0  # kg per m²
is_load_bearing1 = True

area1 = length1 * height1
weight1 = area1 * material_density1 * is_load_bearing1  # Multiplies by 1 if True, 0 if False

# Wall 2
length2 = 5.0
height2 = 2.0
material_density2 = 18.0
is_load_bearing2 = False

area2 = length2 * height2
weight2 = area2 * material_density2 * is_load_bearing2

# Wall 3
length3 = 6.0
height3 = 2.5
material_density3 = 22.0
is_load_bearing3 = True

area3 = length3 * height3
weight3 = area3 * material_density3 * is_load_bearing3

# Output
print("Wall 1 - Area:", area1, "m² | Load-bearing:", is_load_bearing1, "| Weight:", weight1, "kg")
print("Wall 2 - Area:", area2, "m² | Load-bearing:", is_load_bearing2, "| Weight:", weight2, "kg")
print("Wall 3 - Area:", area3, "m² | Load-bearing:", is_load_bearing3, "| Weight:", weight3, "kg")