# Base Restaurant class from Exercise 9-4
class Restaurant:
    """A simple attempt to represent a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name, cuisine type, and customers served."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0  # default value

    def describe_restaurant(self):
        """Print the restaurant's name and cuisine type."""
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        """Print a message indicating the restaurant is open."""
        print(f"{self.restaurant_name} is now open!")

    def set_number_served(self, number):
        """Set the number of customers served."""
        if number >= 0:
            self.number_served = number
        else:
            print("Number served can't be negative.")

    def increment_number_served(self, additional_customers):
        """Increment the number of customers served."""
        if additional_customers >= 0:
            self.number_served += additional_customers
        else:
            print("Additional customers can't be negative.")


# IceCreamStand class inherits from Restaurant
class IceCreamStand(Restaurant):
    """Represent aspects of a restaurant specific to an ice cream stand."""

    def __init__(self, restaurant_name, cuisine_type="Ice Cream"):
        """
        Initialize attributes of the parent class.
        Set default cuisine_type to 'Ice Cream' if not specified.
        """
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []  # List to store ice cream flavors

    def display_flavors(self):
        """Display the list of available ice cream flavors."""
        if self.flavors:
            print(f"\n{self.restaurant_name} offers the following flavors:")
            for flavor in self.flavors:
                print(f"- {flavor}")
        else:
            print(f"\n{self.restaurant_name} currently has no flavors listed.")


# Create an IceCreamStand instance
ice_cream_stand = IceCreamStand("Sweet Treats")

# Add some flavors
ice_cream_stand.flavors = ["Vanilla", "Chocolate", "Strawberry", "Mint Chocolate Chip"]

# Call the method to display flavors
ice_cream_stand.display_flavors()
