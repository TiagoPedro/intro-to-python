element_name = "Room_101"
placeholder_name = "Room_{}_{}"

splitted_name = element_name.split("_") # We get "Room" and "101". The "_" disappears.
replaced_name = element_name.replace("_", " ") # "Room 101". The "_" is replaced by " ".
formatted_name = placeholder_name.format("Limsen", True) # "Room Limsen". The placeholder is replaced by the value of the variable.
upper_cased_name = element_name.upper() # "ROOM_101"
lower_cased_name = element_name.lower() # "room_101"

print("Split name:", splitted_name)
print("Replaced name:", replaced_name)
print("Formatted name:", formatted_name)
print("Upper case name:", upper_cased_name)
print("Lower case name:", lower_cased_name)
