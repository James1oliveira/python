# Import the Path class from the pathlib module (used for working with file paths)
from pathlib import Path

# Create a Path object that points to the file 'alice.txt'
path = Path('alice.txt')

try:
    # Try to read the entire contents of the file as a string, using UTF-8 encoding
    contents = path.read_text(encoding='utf-8')
except FileNotFoundError:
    # If the file is not found, display an error message
    print(f"Sorry, the file {path} does not exist.")
else:
    # If the file was read successfully, split the text into a list of words
    words = contents.split()  # Splits the text at spaces to get each word
    num_words = len(words)    # Count the number of words
    # Display the word count to the user
    print(f"The file {path} has about {num_words} words.")
