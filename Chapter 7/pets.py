# Create a list of pets with some duplicate entries
pets = ['dog', 'cat', 'dog', 'goldfish', 'cat', 'rabbit', 'cat']

# Print the original list of pets
print(pets)

# Use a while loop to remove all instances of both 'cat' and 'dog'
# This loop continues as long as both 'cat' and 'dog' are still in the list
while 'cat' and 'dog' in pets:
    # Remove one instance of 'cat' from the list
    pets.remove('cat')
    # Remove one instance of 'dog' from the list
    pets.remove('dog')

# Print the updated list after all 'cat' and 'dog' entries have been removed
print(pets)
