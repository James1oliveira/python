# --- Example 1: Import the whole 'pizza' module ---
import pizza

# Call the function using the module name and dot notation
pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# --- Example 2: Import only the 'make_pizza' function ---
from pizza import make_pizza

# Call the function directly (no need for 'pizza.' prefix)
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# --- Example 3: Import the whole module with an alias (shorter name) ---
import pizza as p

# Call the function using the alias
p.make_pizza(16, 'pepperoni')
p.make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')


# --- Example 4: Import the function with an alias ---
from pizza import make_pizza as mp

# Call the function using the alias
mp(16, 'pepperoni')
mp(12, 'mushrooms', 'green peppers', 'extra cheese')


# --- Example 5: Import everything from the module ---
from pizza import *

# Call the function directly (all functions/variables are in the current namespace)
make_pizza(16, 'pepperoni')
make_pizza(12, 'mushrooms', 'green peppers', 'extra cheese')
