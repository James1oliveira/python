# Prompt message
prompt = "\nEnter a pizza topping (or type 'quit' to finish): "

# Loop until the user enters 'quit'
while True:
    topping = input(prompt)

    if topping.lower() == 'quit':
        print("Finished making your pizza!")
        break
    else:
        print(f"I'll add {topping} to your pizza.")
