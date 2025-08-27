# Define a function that greets each user in a list
def greet_users(names):
    """Print a simple greeting to each user in the list."""
    # Loop through each name in the list 'names'
    for name in names:
        # Create a greeting message with the name capitalized
        msg = f"Hello, {name.title()}!"
        # Print the greeting message
        print(msg)

# Create a list of usernames
usernames = ['hannah', 'ty', 'margot']

# Call the function to greet each user in the list
greet_users(usernames)
