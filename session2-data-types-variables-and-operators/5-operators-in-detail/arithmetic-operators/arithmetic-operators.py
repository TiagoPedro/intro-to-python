# Calculate concrete volume needed for 10 columns
height_1 = 3.2  # meters
width_1 = 0.4
depth_1 = 0.4

height_2 = 1
width_2 = 0.1
depth_2 = 0.1

num_columns_1 = 5
num_columns_2 = 5

volume_per_column_1 = round(height_1 * width_1 * depth_1, 3)
volume_per_column_2 = round(height_2 * width_2 * depth_2, 3)
total_volume_1 = volume_per_column_1 * num_columns_1

total_volume_of_col1_and_col2 = volume_per_column_1 + volume_per_column_2

print("Volume of column of type 1: ", volume_per_column_1)
print("Volume of column of type 2: ", volume_per_column_2)
print("Total volume of one column of type 1 plus one column of type 2:", total_volume_of_col1_and_col2)