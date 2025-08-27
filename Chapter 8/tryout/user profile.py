def build_profile(first, last, **user_info):
    """
    Build a dictionary containing everything we know about a user.
    Accepts first and last name, plus any number of keyword arguments.
    """
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

# Build a profile for yourself with three additional key-value pairs
my_profile = build_profile(
    'James', 'Oli',
    location='South Africa',
    profession='Software Developer',
    favorite_language='Python'
)

# Print the profile dictionary
print(my_profile)
