# Define a function to return a neatly formatted full name with first and last name
def get_formatted_name(first_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {last_name}"
    return full_name.title()

# Call the function with two arguments
musician = get_formatted_name('jimi', 'hendrix')
print(musician)  # Output: Jimi Hendrix

# Redefine the function to include a required middle name
def get_formatted_name(first_name, middle_name, last_name):
    """Return a full name, neatly formatted."""
    full_name = f"{first_name} {middle_name} {last_name}"
    return full_name.title()

# Call the new version of the function with three arguments
musician = get_formatted_name('john', 'lee', 'hooker')
print(musician)  # Output: John Lee Hooker

# Redefine the function again — now the middle name is optional (default is an empty string)
def get_formatted_name(first_name, last_name, middle_name=''):
    """Return a full name, neatly formatted."""
    if middle_name:
        # If middle_name is provided, include it in the full name
        full_name = f"{first_name} {middle_name} {last_name}"
    else:
        # If no middle_name, just use first and last
        full_name = f"{first_name} {last_name}"
    return full_name.title()

# Call the final version with two arguments (middle name omitted)
musician = get_formatted_name('jimi', 'hendrix')
print(musician)  # Output: Jimi Hendrix

# Call the final version with all three names
musician = get_formatted_name('john', 'hooker', 'lee')
print(musician)  # Output: John Lee Hooker

def get_formatted_name(first_name, last_name):
 """Return a full name, neatly formatted."""
 full_name = f"{first_name} {last_name}"
 return full_name.title()
# This is an infinite loop!
while True:
 print("\nPlease tell me your name:")
 f_name = input("First name: ")
 l_name = input("Last name: ")
 formatted_name = get_formatted_name(f_name, l_name)
 print(f"\nHello, {formatted_name}!")

def get_formatted_name(first_name, last_name):
 """Return a full name, neatly formatted."""
 full_name = f"{first_name} {last_name}"
 return full_name.title()
while True:
 print("\nPlease tell me your name:")
 print("(enter 'q' at any time to quit)")
 f_name = input("First name: ")
 if f_name == 'q':
     break
 l_name = input("Last name: ")
 if l_name == 'q':
     break
 formatted_name = get_formatted_name(f_name, l_name)
 print(f"\nHello, {formatted_name}!")