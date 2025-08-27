# Create a dictionary to store people's favorite numbers
favorite_numbers = {
    'alice': 7,
    'bob': 12,
    'charlie': 3,
    'diana': 9,
    'eric': 21,
}

# Loop through the dictionary to print each person's favorite number
for name, number in favorite_numbers.items():
    print(f"{name.title()}'s favorite number is {number}.")

# Create a dictionary where each person has a list of favorite numbers
favorite_numbers = {
    'alice': [7, 14],
    'bob': [12, 22],
    'charlie': [3],
    'diana': [9, 5, 11],
    'eric': [21, 8],
}

# Loop through the dictionary and print each person's favorite numbers
for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite numbers are:")
    
    # Loop through the list of numbers and print each one
    for number in numbers:
        print(f"\t{number}")
