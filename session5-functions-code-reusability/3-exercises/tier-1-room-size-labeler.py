def label_room_size(area):
    if area < 10:
        return "Small room"
    elif area < 20:
        return "Medium room"
    else:
        return "Large room"

room_areas = [8.5, 14.0, 25.0]

for area in room_areas:
    room_label = label_room_size(area)
    print(room_label)