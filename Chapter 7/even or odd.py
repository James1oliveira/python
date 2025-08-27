# Ask the user to enter a number
number = input("Enter a number, and I'll tell you if it's even or odd: ")

# Convert the input (which is a string) to an integer
number = int(number)

# Check if the number is divisible by 2 (even)
if number % 2 == 0:
    print(f"\nThe number {number} is even.")
# If it's not divisible by 2, then it's odd
else:
    print(f"\nThe number {number} is odd.")
