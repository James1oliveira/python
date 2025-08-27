# Addition Calculator that keeps running until the user quits

print("Welcome to the addition calculator!")
print("Enter 'q' at any time to quit.")

while True:
    # Prompt the user for the first number
    first = input("Enter the first number: ")
    if first.lower() == 'q':
        break  # Exit the loop if the user types 'q'

    # Prompt the user for the second number
    second = input("Enter the second number: ")
    if second.lower() == 'q':
        break  # Exit the loop if the user types 'q'

    try:
        # Attempt to convert the input strings to integers
        num1 = int(first)
        num2 = int(second)
    except ValueError:
        # If conversion fails, print an error message and continue the loop
        print("Oops! You must enter numbers. Please try again.\n")
        continue

    # Calculate the sum and display it
    total = num1 + num2
    print(f"The sum of {num1} and {num2} is {total}.\n")
