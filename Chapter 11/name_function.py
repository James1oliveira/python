def get_formatted_name(first, last):
    """
    Generate a neatly formatted full name.
    
    Arguments:
    first -- the person's first name (string)
    last -- the person's last name (string)
    
    Returns:
    A string containing the full name in title case.
    """
    
    # Combine the first and last name into one string with a space in between
    full_name = f"{first} {last}"
    
    # Convert the combined name into title case (capitalizes the first letter of each word)
    return full_name.title()
