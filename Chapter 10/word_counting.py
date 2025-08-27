from pathlib import Path

def count_words(path):
    """Count the approximate number of words in a file."""
    try:
        # Try to read the entire file content as a string
        contents = path.read_text(encoding='utf-8')
    except FileNotFoundError:
        # If the file is not found, display an error message
        print(f"Sorry, the file {path} does not exist.")
    else:
        # Split the content into words using spaces as separators
        words = contents.split()
        # Count the number of words
        num_words = len(words)
        # Print the result
        print(f"The file {path} has about {num_words} words.")

# Create a Path object for 'alice.txt' and call the function
path = Path('alice.txt')
count_words(path)

# List of multiple filenames to check
filenames = [
    'alice.txt',
    'siddhartha.txt',
    'moby_dick.txt',
    'little_women.txt'
]

# Loop through each file in the list and count the words
for filename in filenames:
    path = Path(filename)
    count_words(path)
