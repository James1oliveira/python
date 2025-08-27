# --- Part 1: Using *toppings to accept any number of arguments ---
print("\n\tPart 1")

# Define a function that accepts any number of toppings
def make_pizza(*toppings):
    """Print the list of toppings that have been requested."""
    print("\nMaking a pizza with the following toppings:")
    # Here, toppings is stored as a tuple
    print(toppings)

# Call the function with one topping
make_pizza('pepperoni')

# Call the function with multiple toppings
make_pizza('mushrooms', 'green peppers', 'extra cheese')


# --- Part 2: Looping through toppings to display them nicely ---
print("\n\tPart 2")

# Define the function again, this time looping through toppings
def make_pizza(*toppings):
    """Summarize the pizza we are about to make."""
    print("\nMaking a pizza with the following toppings:")
    # Loop through each topping and print it
    for topping in toppings:
        print(f"- {topping}")

# Call the function with one topping
make_pizza('pepperoni')

# Call the function with multiple toppings
make_pizza('mushrooms', 'green peppers', 'extra cheese')


# --- Part 3: Adding a required parameter before *toppings ---
print("\n\tPart 3")

# Here, 'size' is a required parameter, followed by any number of toppings
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    # Print pizza size first
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    # Then list all toppings
    for topping in toppings:
        print(f"- {topping}")

# Call the function with size and one topping
make_pizza(16, 'pepperoni')

# Call the function with size and multiple toppings
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# --- Part 4: Same as Part 3 but with slightly different formatting ---
print("\n\tPart 4")

# This version is functionally the same as Part 3
def make_pizza(size, *toppings):
    """Summarize the pizza we are about to make."""
    print(f"\nMaking a {size}-inch pizza with the following toppings:")
    for topping in toppings:
        print(f"- {topping}")  # ✅ Added the missing }

