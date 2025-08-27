class Restaurant:
    """A simple attempt to represent a restaurant."""

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize restaurant name, cuisine type, and number served."""
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0  # Default number of customers served

    def describe_restaurant(self):
        """Print the restaurant's name and cuisine type."""
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        """Print a message indicating the restaurant is open."""
        print(f"{self.restaurant_name} is now open!")

    def set_number_served(self, number):
        """Set the number of customers that have been served."""
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


# Create an instance of Restaurant
restaurant = Restaurant("Sunshine Diner", "American")

# Print the default number of customers served
print(f"Number served: {restaurant.number_served}")

# Change the number served and print it again
restaurant.number_served = 30
print(f"Number served after update: {restaurant.number_served}")

# Use set_number_served() method to set a new number
restaurant.set_number_served(50)
print(f"Number served after set_number_served(): {restaurant.number_served}")

# Use increment_number_served() method to add customers
restaurant.increment_number_served(20)
print(f"Number served after increment_number_served(): {restaurant.number_served}")
