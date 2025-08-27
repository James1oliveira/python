from pathlib import Path

# List of files to read
files = ["cats.txt", "dogs.txt"]

for filename in files:
    path = Path(filename)  # Create a Path object for each file
    try:
        # Try to read the contents of the file
        contents = path.read_text()
    except FileNotFoundError:
        # If the file does not exist, print a friendly message
        print(f"Sorry, the file {filename} does not exist.\n")
    else:
        # If the file exists, print its contents
        print(f"Contents of {filename}:")
        print(contents)
        print("-" * 30)  # Separator between files

