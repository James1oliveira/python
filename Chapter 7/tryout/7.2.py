# Ask the user how many people are in their dinner group
group_size = int(input("How many people are in your dinner group? "))

# Check if the group has more than 8 people
if group_size > 8:
    print("Sorry, you'll have to wait for a table.")
else:
    print("Your table is ready!")
