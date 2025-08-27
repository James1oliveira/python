from pathlib import Path

# Path to the guest book file
path = Path("guest_book.txt")

# Create an empty list to store all names
guest_names = []

print("Enter 'q' at any time to quit.")

# Start a while loop to collect names
while True:
    name = input("Please enter your name: ")
    if name.lower() == 'q':  # Exit the loop if the user types 'q'
        break
    guest_names.append(name)  # Add the name to the list

# Write all collected names to the file, each on a new line
# '\n'.join(guest_names) joins the list into a single string with line breaks
path.write_text('\n'.join(guest_names))

print(f"Thank you! All names have been saved to {path}.")
