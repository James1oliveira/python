# Define a class to represent a general car
class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        """Initialize attributes to describe a car."""
        self.make = make                # Manufacturer name (e.g., 'Ford')
        self.model = model              # Model name (e.g., 'Mustang')
        self.year = year                # Manufacturing year (e.g., 2024)
        self.odometer_reading = 0       # Initial mileage (default is 0)

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()        # Capitalize the first letter of each word

    def read_odometer(self):
        """Print a statement showing the car's mileage."""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """
        Set the odometer reading to the given value.
        Reject the change if it tries to roll back the odometer.
        """
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading."""
        self.odometer_reading += miles


# Define a class to model a battery for an electric car
class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size  # Battery capacity in kWh (default is 40)

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            range = 150  # Approx. miles for a 40-kWh battery
        elif self.battery_size == 65:
            range = 225  # Approx. miles for a 65-kWh battery
        print(f"This car can go about {range} miles on a full charge.")


# Define a subclass for electric cars
class ElectricCar(Car):
    """Represent aspects of a car specific to electric vehicles."""

    def fill_gas_tank(self):
        """Electric cars don't have gas tanks."""
        print("This car doesn't have a gas tank!")

    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Also create a Battery instance as part of this electric car.
        """
        super().__init__(make, model, year)  # Initialize Car attributes
        self.battery_size = 40               # Default battery size in kWh
        self.battery = Battery()              # Create a Battery instance

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")


# --- Program execution ---

# Create an instance of ElectricCar representing a 2024 Nissan Leaf
my_leaf = ElectricCar('nissan', 'leaf', 2024)

# Print the descriptive name of the Leaf
print(my_leaf.get_descriptive_name())

# Describe the battery size using ElectricCar's own method
my_leaf.describe_battery()

# Describe the battery size using the Battery instance's method
my_leaf.battery.describe_battery()

# Display the driving range based on the battery size
my_leaf.battery.get_range()
