room_areas = [8.5, 14.0, 25.0]

for i in range(3):
    if room_areas[i] < 10:
        print("Small room")
    elif room_areas[i] < 20:
        print("Medium room")
    else:
        print("Large room")
