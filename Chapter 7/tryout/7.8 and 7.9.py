# List of sandwich orders
sandwich_orders = ['tuna', 'chicken', 'veggie', 'turkey']

# Empty list to hold finished sandwiches
finished_sandwiches = []

# Make each sandwich
for sandwich in sandwich_orders:
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)

# Print all the finished sandwiches
print("\nAll sandwiches made:")
for sandwich in finished_sandwiches:
    print(sandwich.title())

# Sandwich orders with 'pastrami' repeated 3 times
sandwich_orders = ['tuna', 'pastrami', 'chicken', 'pastrami', 'veggie', 'pastrami', 'turkey']
finished_sandwiches = []

# Inform customer pastrami is unavailable
print("Sorry, the deli has run out of pastrami.\n")

# Remove all 'pastrami' sandwiches
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

# Make the rest of the sandwiches
for sandwich in sandwich_orders:
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)

# List the sandwiches that were made
print("\nAll sandwiches made:")
for sandwich in finished_sandwiches:
    print(sandwich.title())
