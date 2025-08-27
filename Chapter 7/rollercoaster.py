# Ask the user for their height in centimeters
height = input("How tall are you, in centimeters? ")

# Convert the input (which is a string) to an integer
height = int(height)

# Check if the user's height is 144 cm or more
if height >= 144:
    # If the user is tall enough, print a positive message
    print("\nYou're tall enough to ride!")
else:
    # If the user is not tall enough, print a message saying they have to wait
    print("\nYou'll be able to ride when you're a little older.")
