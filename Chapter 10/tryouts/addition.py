# Program to add two numbers entered by the user

print("This program adds two numbers.")
print("Enter 'q' at any time to quit.")

while True:
    # Prompt the user for the first number
    first = input("Enter the first number: ")
    if first.lower() == 'q':
        break

    # Prompt the user for the second number
    second = input("Enter the second number: ")
    if second.lower() == 'q':
        break

    try:
        # Try converting the inputs to integers
        num1 = int(first)
        num2 = int(second)
    except ValueError:
        # If conversion fails, print an error message and continue the loop
        print("Oops! You must enter numbers. Please try again.")
        continue

    # Add the numbers and display the result
    total = num1 + num2
    print(f"The sum of {num1} and {num2} is {total}.\n")
