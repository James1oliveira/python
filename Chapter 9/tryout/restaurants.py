# Define a Restaurant class
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


# Create an instance of Restaurant
restaurant = Restaurant("Ocean Breeze", "Seafood")

# Print the two attributes individually
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

# Call both methods
restaurant.describe_restaurant()
restaurant.open_restaurant()
