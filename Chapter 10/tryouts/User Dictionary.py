from pathlib import Path
import json

# Path to the JSON file
path = Path("user_info.json")

try:
    # Try to read existing user information
    contents = path.read_text()
    user_info = json.loads(contents)
except FileNotFoundError:
    # If no file exists, ask the user for information
    print("We don't have your information yet. Please provide it below.")
    
    username = input("What is your name? ")
    age = input("How old are you? ")
    favorite_language = input("What is your favorite programming language? ")
    
    # Store the information in a dictionary
    user_info = {
        "name": username,
        "age": age,
        "favorite_language": favorite_language
    }
    
    # Save the dictionary to a JSON file
    path.write_text(json.dumps(user_info))
    print("\nThank you! Your information has been saved.\n")
else:
    print("We found your information!\n")

# Print a summary of what we remember about the user
print("Summary of your information:")
print(f"Name: {user_info['name']}")
print(f"Age: {user_info['age']}")
print(f"Favorite programming language: {user_info['favorite_language']}")
