from pathlib import Path
import json

# Path to store the username
path = Path("username.json")

def get_new_username():
    """Prompt the user for a new username and save it to a file."""
    username = input("What is your name? ")
    path.write_text(json.dumps(username))
    return username

def greet_user():
    """Greet the user, verifying the username if already stored."""
    try:
        # Try to read the stored username
        contents = path.read_text()
        stored_username = json.loads(contents)
    except FileNotFoundError:
        # If no username is stored, get a new one
        username = get_new_username()
    else:
        # Ask the user if the stored username is correct
        response = input(f"Are you {stored_username}? (y/n) ")
        if response.lower() == 'y':
            username = stored_username
        else:
            # If it's not the correct user, get a new username
            username = get_new_username()
    
    # Greet the user
    print(f"Welcome back, {username}!")

# Run the program
greet_user()

