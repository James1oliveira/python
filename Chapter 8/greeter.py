# Define a function that greets the user (no name required)
def greet_user():
    """Display a simple greeting."""
    # Print a general greeting
    print("Hello!")

# Call the function to display the greeting
greet_user()

# Define a new version of the greet_user function that accepts a name
def greet_user(username):
    """Display a simple greeting."""
    # Print a personalized greeting, with the first letter capitalized
    print(f"Hello, {username.title()}!")

# Call the function with a specific name
greet_user('lethabo')
