area = 10.0
room_list = ["Office", "Bathroom", "Kitchen"]

for room_type in room_list:
    if room_type == "Bathroom":
      if area <= 4:
        classification = "Too small"
      elif 4 < area <= 6:
        classification = "Acceptable"
      elif area > 6:
        classification = "Spacious"

    elif room_type == "Office":
      if area < 8:
        classification = "Too small"
      elif area <= 12:
        classification = "Acceptable"
      else:
        classification = "Spacious"

    elif room_type == "Living Room":
      if area < 12:
        classification = "Too small"
      elif area <= 20:
        classification = "Acceptable"
      else:
        classification = "Spacious"
    
    print(f"{room_type} of {area}m² is considered: {classification}")
    

# first iteration: room_type = "Office", classifcation = "Acceptable"
# second iteration: room_type = "BAthroom", classifcation = "Spacious"
# third iteration: room_type = "Kitchen", classifcation = "Spacious"
