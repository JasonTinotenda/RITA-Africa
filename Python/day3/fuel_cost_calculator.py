trip_distance = float(input("Enter the distance of the trip: "))
cost_of_fuel = float(input("Enter the cost of fuel per litre: "))
standard_fuel_consumption = 0.08
# Calculate the cost of the trip
total_fuel_cost = (trip_distance*cost_of_fuel*standard_fuel_consumption)
print(
    f"The total cost of the fuel is ${total_fuel_cost:.2f}."
)