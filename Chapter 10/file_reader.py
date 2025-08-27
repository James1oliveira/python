from pathlib import Path  # Import Path class to work with filesystem paths

# Define the path to the file containing pi digits
path = Path('pi_digits.txt')

# Read the entire content of the file as a single string
contents = path.read_text()

# Print the whole content of the file at once
print(contents)

# Split the content into a list of lines (each line without newline characters)
lines = contents.splitlines()

# Loop through each line and print it individually
for line in lines:
    print(line)
