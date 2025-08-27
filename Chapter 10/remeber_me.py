from pathlib import Path
import json

# Ask the user for their name
username = input("What is your name? ")

# Create a Path object for the file where we'll store the name
path = Path('username.json')

# Convert the username (a Python string) into JSON format
contents = json.dumps(username)

# Write the JSON string to the file
path.write_text(contents)

# Confirm to the user that their name has been saved
print(f"We'll remember you when you come back, {username}!")
