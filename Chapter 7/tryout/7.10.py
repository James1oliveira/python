# Create an empty dictionary to store responses
responses = {}

# Set a flag to indicate that polling is active
polling_active = True

# Start the poll
while polling_active:
    # Ask for the person's name
    name = input("What is your name? ")

    # Ask their dream vacation destination
    vacation = input("If you could visit one place in the world, where would you go? ")

    # Store the response in the dictionary
    responses[name] = vacation

    # Ask if anyone else wants to take the poll
    repeat = input("Would you like to let someone else respond? (yes/no) ")

    # Stop the loop if the answer is 'no'
    if repeat.lower() == 'no':
        polling_active = False

# Polling is complete, show the results
print("\n--- Poll Results ---")
for name, vacation in responses.items():
    print(f"{name.title()} would like to visit {vacation.title()}.")
