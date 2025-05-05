project_name = "Central Library"

lobby_name = "Lobby"
office_name = "Office"
kitchen_name = "Kitchen"

lobby_length = 5
office_length = 4.5
kitchen_length = 4

lobby_width = 5
office_width = 3
kitchen_width = 5.5

lobby_area = lobby_length * lobby_width
office_area = office_length * office_width
kitchen_area = kitchen_length * kitchen_width

print("Room Lobby: " + str(float(lobby_area)) + " m2")
print("Office Lobby: " + str(float(office_area)) + " m2")
print("Kitchen Lobby: " + str(float(kitchen_area)) + " m2")

total_area = lobby_area + office_area + kitchen_area

print("Total area: " + str(float(total_area)) + " m2")