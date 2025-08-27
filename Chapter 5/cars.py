# Create a list of car brand names
cars = ['audi', 'bmw', 'subaru', 'toyota']

# Loop through each car in the list
for car in cars:
    # Check if the current car is 'bmw'
    if car == 'bmw':
        # If it is 'bmw', print the name in all uppercase letters
        print(car.upper())
    else:
        # Otherwise, print the car name in title case (first letter capitalized)
        print(car.title())

        