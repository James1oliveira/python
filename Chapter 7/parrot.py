# Prompt the user to enter a message
# The message will be repeated back until the user types 'quit'
prompt = "\nTell me something, and I will repeat it back to you:"
prompt += "\nEnter 'quit' to end the program. "

# Use a flag variable to keep track of whether the loop should keep running
active = True

# Start a while loop that runs as long as 'active' is True
while active:
    # Ask the user for input
    message = input(prompt)

    # If the user enters 'quit', set 'active' to False to stop the loop
    if message == 'quit':
        active = False
    else:
        # Otherwise, print the message back to the user
        print(message)
