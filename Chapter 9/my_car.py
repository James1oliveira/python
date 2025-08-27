# Import the Car class from the car module
from car import Car

# Import the Car and ElectricCar classes from the electric_car module
from electric_car import Car, ElectricCar

# Import the entire car module so we can access its classes via car.ClassName syntax
import car

# Create a Car object representing a 2024 Ford Mustang
my_mustang = Car('ford', 'mustang', 2024)

# Print the descriptive name of the Mustang
print(my_mustang.get_descriptive_name())

# Create an ElectricCar object representing a 2024 Nissan Leaf
my_leaf = ElectricCar('nissan', 'leaf', 2024)

# Print the descriptive name of the Leaf
print(my_leaf.get_descriptive_name())

# Create another Car object representing a 2024 Audi A4
my_new_car = Car('audi', 'a4', 2024)

# Print the descriptive name of the Audi
print(my_new_car.get_descriptive_name())

# Manually set the odometer reading of the Audi to 23
my_new_car.odometer_reading = 23

# Display the current odometer reading
my_new_car.read_odometer()

# Create a Ford Mustang object using the Car class accessed from the imported car module
my_mustang = car.Car('ford', 'mustang', 2024)

# Print the descriptive name of the Mustang
print(my_mustang.get_descriptive_name())

# Create a Nissan Leaf object using the ElectricCar class accessed from the imported car module
my_leaf = car.ElectricCar('nissan', 'leaf', 2024)

# Print the descriptive name of the Leaf
print(my_leaf.get_descriptive_name())
