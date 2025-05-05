def calculate_area(width, length):
    area = width * length
    return area

bathroom_width = 2.0
bathroom_length = 3.5

office_width = 4.0
office_length = 6.4

room_widths = [2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5, 10.0, 10.5, 11.0, 11.5]
room_lengths = [3.0, 3.2, 3.4, 3.6, 3.8, 4.0, 4.2, 4.4, 4.6, 4.8, 5.0, 5.2, 5.4, 5.6, 5.8, 6.0, 6.2, 6.4, 6.6, 6.8]
room_areas = [0] * 20

for i in range(20):
    room_area = calculate_area(room_widths[i], room_lengths[i])
    room_areas[i] = room_area

print(room_areas)

# bathroom_area = calculate_area(bathroom_width, bathroom_length)
# office_area = calculate_area(office_width, office_length)
