from pathlib import Path  # Import Path to work with file paths

# Define the path to the file containing pi digits
path = Path('pi_digits.txt')

# Read the entire content of the file as a single string
contents = path.read_text()

# Print the contents of the file (pi digits)
print(contents)

# Split the contents into individual lines (removes newline characters)
lines = contents.splitlines()

pi_string = ''  # Initialize an empty string to store pi digits without spaces or newlines

# Loop through each line, strip leading/trailing whitespace, and add it to pi_string
for line in lines:
    pi_string += line.strip()

# Ask the user to input their birthday in the format mmddyy
birthday = input("Enter your birthday, in the form mmddyy: ")

# Check if the birthday string appears anywhere in the pi digits string
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi.")
