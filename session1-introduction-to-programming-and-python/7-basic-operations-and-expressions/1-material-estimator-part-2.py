# Part 1
# Step 1: Define the variables
project_name = "Central Library"
floor_area = 350.5              # in square meters
material_name = "Concrete"
material_unit_cost = 75        # per m2
coverage_per_unit = 1.5        # in m2 per unit
waste_percentage = 0.1  # 10% waste factor

# Step 2: Print the variables
print("Project:", project_name)
print("Floor Area:", floor_area, "m²")
print("Material:", material_name)
print("Unit Cost:", material_unit_cost, "€/m²")
print("Waste Percentage:", waste_percentage)

# Step 3: Check the data types of the variables
print(type(project_name))
print(type(floor_area))
print(type(material_name))
print(type(material_unit_cost))
print(type(waste_percentage))

# Part 2
# Step 1: Calculate the units needed
base_units_needed = floor_area / coverage_per_unit

# Step 2: Apply waste factor if included
units_needed = base_units_needed * (1 + waste_percentage)
print("Units Needed:", units_needed)

# Step 3: Calculate the final cost
final_cost = units_needed * material_unit_cost
print("Final Estimated Cost:", final_cost, "€")