from name_function import get_formatted_name  # Import the get_formatted_name function from the name_function module

# ---------- TEST FUNCTIONS ----------

def test_first_last_name():
    """Test: Does the function work for names with only first and last names?"""
    formatted_name = get_formatted_name('janis', 'joplin')
    # Assert checks if the result matches the expected output
    assert formatted_name == 'Janis Joplin'

def test_first_last_middle_name():
    """Test: Does the function work for names with a first, middle, and last name?"""
    formatted_name = get_formatted_name(
        'wolfgang', 'mozart', 'amadeus')  # This will fail unless the function supports middle names
    assert formatted_name == 'Wolfgang Amadeus Mozart'


# ---------- INITIAL FUNCTION VERSION (without middle name support) ----------
def get_formatted_name(first, middle, last):
    """Generate a neatly formatted full name with a middle name."""
    full_name = f"{first} {middle} {last}"
    return full_name.title()


# ---------- UPDATED FUNCTION VERSION (middle name optional) ----------
def get_formatted_name(first, last, middle=''):
    """
    Generate a neatly formatted full name.
    
    Arguments:
    first -- first name (string)
    last -- last name (string)
    middle -- optional middle name (string)
    
    Returns:
    A string with the full name in title case.
    """
    if middle:  # If a middle name is provided
        full_name = f"{first} {middle} {last}"
    else:  # If no middle name is provided
        full_name = f"{first} {last}"
    return full_name.title()


# ---------- HOW TO RUN TESTS ----------
# In the terminal, run:
# python -m pytest test_name_function.py
# This will automatically find functions starting with "test_" and check if they pass.
