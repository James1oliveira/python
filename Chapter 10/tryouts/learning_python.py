from pathlib import Path

# Create the text for the file
learning_text = (
    "In Python you can store information in variables.\n"
    "In Python you can write functions to organize your code.\n"
    "In Python you can work with lists to store multiple items.\n"
    "In Python you can use loops to repeat actions.\n"
)

# Path to the file
path = Path("learning_python.txt")

# Write the text to the file
path.write_text(learning_text)

# --- First way: Read the entire file at once and print ---
print("=== Reading the whole file at once ===")
contents = path.read_text()  # Read all file contents into a single string
print(contents)

# --- Second way: Read the file line-by-line using a list ---
print("=== Reading line-by-line ===")
lines = path.read_text().splitlines()  # Returns a list of lines without newline characters

for line in lines:
    print(line)
