# The commented-out block below was an example of handling division by zero:
# try:
#     print(5/0)
# except ZeroDivisionError:
#     print("You can't divide by zero!")

print("Give me two numbers, and I'll divide them.")  # Inform the user about the program
print("Enter 'q' to quit.")  # Tell the user how to exit the program

while True:  # Start an infinite loop to keep asking for input until the user quits
    first_number = input("\nFirst number: ")  # Prompt user to enter the first number
    if first_number == 'q':  # Check if user wants to quit
        break  # Exit the loop if 'q' is entered
    
    second_number = input("Second number: ")  # Prompt user for the second number
    if second_number == 'q':  # Check if user wants to quit
        break  # Exit the loop if 'q' is entered
    
    try:
        # Try to convert inputs to integers and perform division
        answer = int(first_number) / int(second_number)
    except ZeroDivisionError:
        # Handle case where second number is zero to avoid crashing
        print("You can't divide by 0!")
    else:
        # If no exception occurs, print the result
        print(answer)

# The commented-out line below was a direct division without exception handling
# answer = int(first_number) / int(second_number)
