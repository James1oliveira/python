# Reuse the Restaurant class from Exercise 9-1
class Restaurant:
    """A simple attempt to model a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize the restaurant's name and cuisine type."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        """Print the restaurant's name and cuisine type."""
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        """Print a message indicating the restaurant is open."""
        print(f"{self.restaurant_name} is now open for business!")


# Create three different Restaurant instances
restaurant1 = Restaurant("Ocean Breeze", "Seafood")
restaurant2 = Restaurant("Spice Garden", "Indian Cuisine")
restaurant3 = Restaurant("Pasta Palace", "Italian")

# Call describe_restaurant() for each instance
restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()
