# Create an empty dictionary to store responses
responses = {}

# Set a flag to indicate that polling is active
polling_active = True

# Start a while loop that runs as long as polling_active is True
while polling_active:
    # Ask the person for their name
    name = input("\nWhat is your name? ")

    # Ask them which mountain they would like to climb
    response = input("Which mountain would you like to climb someday? ")

    # Store the response in the dictionary with the name as the key
    responses[name] = response

    # Ask if someone else wants to take the poll
    repeat = input("Would you like to let another person respond? (yes/ no) ")

    # If the answer is 'no', stop the loop
    if repeat == 'no':
        polling_active = False

# Polling is complete. Show the results.
print("\n--- Poll Results ---")
# Loop through the responses and print each person's answer
for name, response in responses.items():
    print(f"{name} would like to climb {response}.")
