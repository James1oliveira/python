# List of toppings that are available at the pizza shop
available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']

# List of toppings the customer has requested
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

# Loop through each topping the customer requested
for requested_topping in requested_toppings:
    # Check if the requested topping is available
    if requested_topping in available_toppings:
        # If available, add the topping
        print(f"Adding {requested_topping}.")
    else:
        # If not available, show a message of apology
        print(f"Sorry, we don't have {requested_topping}.")

# Print a message indicating the pizza is ready
print("\nFinished making your pizza!")
