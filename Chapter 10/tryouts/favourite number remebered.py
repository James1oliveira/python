from pathlib import Path
import json

# Path to the JSON file
path = Path("favorite_number.json")

try:
    # Try to read the stored favorite number
    contents = path.read_text()
    favorite_number = json.loads(contents)
except FileNotFoundError:
    # If the file doesn't exist, ask the user for their favorite number
    favorite_number = input("What is your favorite number? ")
    try:
        favorite_number = int(favorite_number)  # Convert to integer
    except ValueError:
        print("Please enter a valid number next time.")
        exit()
    # Save the favorite number to the file
    path.write_text(json.dumps(favorite_number))
    print(f"Your favorite number ({favorite_number}) has been saved!")
else:
    # If the file exists, greet the user with their stored number
    print(f"I know your favorite number! It's {favorite_number}.")
