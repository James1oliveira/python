# Define a class to represent a dog
class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes."""
        self.name = name    # Store the dog's name
        self.age = age      # Store the dog's age

    def sit(self):
        """Simulate a dog sitting in response to a command."""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command."""
        print(f"{self.name} rolled over!")


# --- Program execution ---

# Create an instance of Dog named Willie, age 6
my_dog = Dog('Willie', 6)

# Create another instance of Dog named Lucy, age 3
your_dog = Dog('Lucy', 3)

# Display the name and age of my_dog
print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")

# Command my_dog to sit
my_dog.sit()

# Display the name and age of your_dog
print(f"\nYour dog's name is {your_dog.name}.")
print(f"Your dog is {your_dog.age} years old.")

# Command your_dog to sit
your_dog.sit()
