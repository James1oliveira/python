class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=40):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 40:
            range_miles = 150
        elif self.battery_size == 65:
            range_miles = 225
        else:
            range_miles = 0  # Unknown battery size

        print(f"This car can go about {range_miles} miles on a full charge.")

    def upgrade_battery(self):
        """
        Upgrade the battery to 65 kWh if it isn't already.
        """
        if self.battery_size < 65:
            print("Upgrading the battery from "
                  f"{self.battery_size} to 65 kWh.")
            self.battery_size = 65
        else:
            print("Battery is already upgraded to 65 kWh or higher.")


class ElectricCar:
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, make, model, year):
        """Initialize attributes of the parent class and battery."""
        self.make = make
        self.model = model
        self.year = year
        self.battery = Battery()  # Default battery size 40

    def get_descriptive_name(self):
        """Return a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()


# Testing the upgrade_battery method

my_tesla = ElectricCar('tesla', 'model s', 2024)

print(my_tesla.get_descriptive_name())

# Check the range before upgrade
my_tesla.battery.get_range()

# Upgrade the battery
my_tesla.battery.upgrade_battery()

# Check the range after upgrade
my_tesla.battery.get_range()
