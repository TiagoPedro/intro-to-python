# Vehicle Details
fuel_efficiency = 8.5       # liters per 100km
fuel_price = 1.85           # price per liter

# Journey Details
distance = 750              # kilometers
passengers = 4
avg_speed = 90              # km/h
rest_stops = 2              # number of planned stops
rest_time = 0.5             # hours per stop

# Additional Costs
toll_price = 15             # per toll station
toll_stations = 4           # number of stations
parking_rate = 2.5          # per hour at destination
parking_hours = 48          # hours parked at destination

# Calculate fuel consumption
total_fuel_needed = (distance / 100) * fuel_efficiency
fuel_cost = total_fuel_needed * fuel_price

# Calculate time-related costs
driving_time = distance / avg_speed
stop_time = rest_stops * rest_time  # 30 mins per stop
total_journey_time = driving_time + stop_time

# Calculate total costs
toll_cost = toll_price * toll_stations
parking_cost = parking_rate * parking_hours
total_trip_cost = fuel_cost + toll_cost + parking_cost
cost_per_person = total_trip_cost / passengers

# Print the results
print(f"Total Fuel Cost: {fuel_cost:.2f} €")
print(f"Total Toll Cost: {toll_cost:.2f} €")
print(f"Total Parking Cost: {parking_cost:.2f} €")
print(f"Total Trip Cost: {total_trip_cost:.2f} €")
print(f"Cost per Person: {cost_per_person:.2f} €")