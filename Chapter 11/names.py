from name_function import get_formatted_name  # Import the get_formatted_name function from the name_function module

print("Enter 'q' at any time to quit.")  # Let the user know how to exit the program

# Start an infinite loop to continuously ask for user input
while True:
    # Ask for the user's first name
    first = input("\nPlease give me a first name: ")
    if first == 'q':  # If the user types 'q', break out of the loop
        break
    
    # Ask for the user's last name
    last = input("Please give me a last name: ")
    if last == 'q':  # If the user types 'q', break out of the loop
        break
    
    # Call the function to format the full name neatly
    formatted_name = get_formatted_name(first, last)
    
    # Display the neatly formatted name
    print(f"\n\tNeatly formatted name: {formatted_name}.")
