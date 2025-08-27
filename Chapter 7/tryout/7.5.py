# Prompt message
prompt = "\nEnter your age (or type 'quit' to exit): "

# Loop to keep asking for age until user quits
while True:
    age_input = input(prompt)

    if age_input.lower() == 'quit':
        print("Thank you! Enjoy your movie.")
        break

    age = int(age_input)

    if age < 3:
        print("Your ticket is free!")
    elif age <= 12:
        print("Your ticket costs $10.")
    else:
        print("Your ticket costs $15.")
