# Create a prompt message to ask the user for their name
prompt = "If you share your name, we can personalize the messages you see."
prompt += "\nWhat is your first name? "  # Add a second line to the prompt

# Ask the user to input their name and store it in the variable 'name'
name = input(prompt)

# Greet the user with a personalized message
print(f"\nHello, {name}!")
