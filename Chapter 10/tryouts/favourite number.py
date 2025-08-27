from pathlib import Path
import json

# Prompt the user for their favorite number
favorite_number = input("What is your favorite number? ")

# Convert the input to an integer (optional, ensures number is stored as a number)
try:
    favorite_number = int(favorite_number)
except ValueError:
    print("Please enter a valid number next time.")
    exit()

# Create a Path object for the file
path = Path("favorite_number.json")

# Store the number in JSON format
path.write_text(json.dumps(favorite_number))

print(f"Your favorite number ({favorite_number}) has been saved!")
