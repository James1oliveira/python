def make_sandwich(*items):
    """
    Accept a list of items a person wants on a sandwich,
    then print a summary of the sandwich order.
    """
    print("\nMaking a sandwich with the following items:")
    for item in items:
        print(f"- {item}")

# Call the function three times with different numbers of arguments
make_sandwich('ham', 'cheese', 'lettuce')
make_sandwich('turkey', 'bacon')
make_sandwich('peanut butter', 'jelly', 'banana', 'honey')
