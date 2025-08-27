# Import the ElectricCar class from the electric_car module
from electric_car import ElectricCar

# Create an instance of ElectricCar representing a 2024 Nissan Leaf
my_leaf = ElectricCar('nissan', 'leaf', 2024)

# Print a descriptive name for the car (e.g., "2024 Nissan Leaf")
print(my_leaf.get_descriptive_name())

# Call the battery's method to describe the battery size/capacity
my_leaf.battery.describe_battery()

# Call the battery's method to display the range based on battery size
my_leaf.battery.get_range()
