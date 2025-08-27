from pathlib import Path

# Prompt the user for their name
name = input("What is your name? ")

# Create a Path object for the file guest.txt
path = Path("guest.txt")

# Write the user's name to the file
path.write_text(name)

# Confirm to the user that their name has been saved
print(f"Hello, {name}! Your name has been saved to {path}.")
