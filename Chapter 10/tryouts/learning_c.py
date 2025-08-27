from pathlib import Path

# Path to the file created in 10-1
path = Path("learning_python.txt")

# Read all lines from the file into a list
lines = path.read_text().splitlines()

# Loop through each line, replacing "Python" with "C"
for line in lines:
    # Replace "Python" with "C" and print the modified line
    modified_line = line.replace("Python", "C")
    print(modified_line)
