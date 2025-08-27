# Create a dictionary representing an alien with two key-value pairs
alien_0 = {'color': 'green', 'speed': 'slow'}

# Try to access the value for the key 'points'
# If the key doesn't exist, return the default message instead of causing an error
point_value = alien_0.get('points', 'No point value assigned.')

# Print the result (either the actual value or the default message)
print(point_value)
