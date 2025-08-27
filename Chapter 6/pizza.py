# Store information about a pizza being ordered using a dictionary
pizza = {
    'crust': 'thick',  # The type of crust
    'toppings': ['mushrooms', 'extra cheese'],  # A list of toppings
}

# Print a summary of the order, including the crust type
print(f"You ordered a {pizza['crust']}-crust pizza "
      "with the following toppings:")

# Loop through the list of toppings and print each one
for topping in pizza['toppings']:
    print(f"\t{topping}")  # Print each topping with a tab for indentation
