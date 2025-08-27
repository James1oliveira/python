from pathlib import Path
import json

# Create a Path object for the file containing the stored username
path = Path('username.json')

# Read the file contents as a string
contents = path.read_text()

# Convert the JSON string back into a Python string (username)
username = json.loads(contents)

# Greet the returning user
print(f"Welcome back, {username}!")
