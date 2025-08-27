from pathlib import Path
import json

# A list of numbers we want to store in a file
numbers = [2, 3, 5, 7, 11, 13]

# Create a Path object for the JSON file
path = Path('numbers.json')

# Convert the Python list into a JSON-formatted string
contents = json.dumps(numbers)

# Write the JSON string to the file
path.write_text(contents)
