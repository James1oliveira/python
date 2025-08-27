# Set the age of the person
age = 12

# Check the age and determine the price of admission
if age < 4:
    price = 0  # Free admission for children under 4
elif age < 18:
    price = 25  # $25 for children between 4 and 17
elif age < 65:
    price = 40  # $40 for adults between 18 and 64
elif age >= 65:
    price = 20  # $20 for seniors 65 and older

# Print the final admission cost
print(f"Your admission cost is ${price}.")
