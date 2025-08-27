from pathlib import Path  # Import Path class to handle file system paths

# Define the path to the file containing pi digits
path = Path('pi_digits.txt')

# Alternative file path (currently commented out)
# path = Path('H:\\CodeCollege\\WebDev\\Python\\python_work\\classwork\\chap10\\message.txt')

# Read the entire content of the file as a single string
contents = path.read_text()

# Split the content into a list of lines (removes newline characters)
lines = contents.splitlines()

pi_string = ''  # Initialize an empty string to store processed pi digits

# Loop through each line in the file
for line in lines:
    pi_string += line.lstrip()  # Add the line with leading whitespace removed
    pi_string += line           # Add the original line again (with whitespace)

# Print the length of the combined string pi_string
print(len(pi_string))

# Print the length again with ellipsis for clarity or formatting
print(f"{len(pi_string)}...")
