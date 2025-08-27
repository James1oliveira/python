# Create a nested dictionary with information about multiple users
users = {
    'aeinstein': {
        'first': 'albert',
        'last': 'einstein',
        'location': 'princeton',
    },

    'mcurie': {
        'first': 'marie',
        'last': 'curie',
        'location': 'paris',
    },
}

# Loop through each username and their corresponding info
for username, user_info in users.items():
    # Print the username
    print(f"\nUsername: {username}")

    # Combine first and last names into a full name
    full_name = f"{user_info['first']} {user_info['last']}"

    # Get the user's location
    location = user_info['location']
    
    # Print the full name and location with proper formatting
    print(f"\tFull name: {full_name.title()}")
    print(f"\tLocation: {location.title()}")
