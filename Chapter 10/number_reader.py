from pathlib import Path
import json

# Create a Path object for the JSON file we want to read
path = Path('numbers.json')

# Read the entire file content as a string
contents = path.read_text()

# Convert the JSON string back into a Python object (list in this case)
numbers = json.loads(contents)

# Print the list of numbers
print(numbers)
