# --- Part 1: Printing models without functions ---

# Start with some designs that need to be printed
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Simulate printing each design until none are left
# Move each design to completed_models after printing
print("\nThe following models are not printed:")
while unprinted_designs:
    # Remove the last design from the list
    current_design = unprinted_designs.pop()
    # Simulate printing the model
    print(f"Printing model: {current_design}")
    # Store the completed model in another list
    completed_models.append(current_design)

# Display all completed models
print("\nThe following models have been printed:")
for completed_model in completed_models:
    print(completed_model)


# --- Part 2: Using functions for the same process ---

def print_models(unprinted_designs, completed_models):
    """
    Simulate printing each design until none are left.
    Move each design to completed_models after printing.
    """
    print("\nThe following models are to be printed:")
    while unprinted_designs:
        # Remove the last design from the list
        current_design = unprinted_designs.pop()
        # Simulate printing
        print(f"Printing model: {current_design}")
        # Add the completed model to the completed_models list
        completed_models.append(current_design)


def show_completed_models(completed_models):
    """Show all the models that were printed."""
    print("\nThe following models have been printed:")
    for completed_model in completed_models:
        print(completed_model)


# Prepare lists again for the function-based example
unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []

# Call the functions to simulate the process
print_models(unprinted_designs, completed_models)

# Use a copy of the completed_models list when displaying
# so the original list isn't accidentally modified
show_completed_models(completed_models[:])
