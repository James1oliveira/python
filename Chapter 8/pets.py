# --- First version of the function: no default parameters ---
def describe_pet(animal_type, pet_name):
    """Display information about a pet."""
    # Print the type of pet
    print(f"\nI have a {animal_type}.")
    # Print the pet's name, with the first letter of each word capitalized
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# Calling the function with positional arguments
describe_pet('dog', 'brock lesnar')
describe_pet('dog', 'willie')

# Calling the function with keyword arguments (order doesn't matter)
describe_pet(animal_type='hamster', pet_name='harry')


# --- Second version of the function: with a default parameter ---
def describe_pet(pet_name, animal_type='dog'):
    """Display information about a pet."""
    # Print the type of pet
    print(f"\nI have a {animal_type}.")
    # Print the pet's name, formatted with title case
    print(f"My {animal_type}'s name is {pet_name.title()}.")

# Calling the function with only the pet's name (animal_type defaults to 'dog')
describe_pet(pet_name='willie')

# Calling the function with both arguments using keyword arguments
describe_pet(animal_type='hamster', pet_name='harry')

# Calling the function with both arguments in reverse order (keyword arguments allow flexibility)
describe_pet(pet_name='harry', animal_type='hamster')

# ❌ This will cause an error because 'pet_name' is required and no value is provided
describe_pet()
