# Define a function that accepts first and last name,
# plus any number of additional keyword arguments (**user_info)
def build_profile(first, last, **user_info):
    """
    Build a dictionary containing everything we know about a user.
    **user_info collects all extra key-value pairs into a dictionary.
    """
    # Add first name to the dictionary
    user_info['first_name'] = first
    # Add last name to the dictionary
    user_info['last_name'] = last
    # Return the completed dictionary
    return user_info

# Call the function with required first & last names
# and extra keyword arguments (location and field)
user_profile = build_profile(
    'albert', 'einstein',
    location='princeton',
    field='physics'
)

# Print the resulting dictionary
print(user_profile)
