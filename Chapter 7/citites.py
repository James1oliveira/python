# Create a prompt message that asks the user for a city they've visited
# Also lets them know how to exit the loop
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

# Start an infinite loop that keeps asking the user for input
while True:
    # Get input from the user and store it in the variable 'city'
    city = input(prompt)

    # Check if the user wants to quit
    if city == 'quit':
        # Exit the loop
        break
    else:
        # Print a message including the city name with proper capitalization
        print(f"I'd love to go to {city.title()}!")
