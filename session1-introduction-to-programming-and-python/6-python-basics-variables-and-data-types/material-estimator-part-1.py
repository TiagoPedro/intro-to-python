# Step 1: Define the variables
project_name = "123"
project_id = "id"
floor_area = 350.5              # in square meters
material_name = "Concrete"
material_unit_cost = 75        # per m2
is_renovation = False

project_name_id = project_name + " " + project_id

# Step 2: Print the variables
print("Project:", project_name)
print("Project name ID:", project_name_id)
print("Floor Area:", floor_area, "m²")
print("Material:", material_name)
print("Unit Cost:", material_unit_cost, "€/m²")
print("Renovation Project?", is_renovation)

# Step 3: Check the data types of the variables
print(type(project_name))
print(type(floor_area))
print(type(material_unit_cost))
print(type(is_renovation))
print(type(project_name_id))