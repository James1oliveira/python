class User:
    """A simple class to represent a user profile."""

    def __init__(self, first_name, last_name, age, location, email):
        """Initialize attributes to describe a user."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.email = email

    def describe_user(self):
        """Print a summary of the user's information."""
        print(f"\nUser Profile:")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Location: {self.location}")
        print(f"Email: {self.email}")

    def greet_user(self):
        """Print a personalized greeting to the user."""
        print(f"Hello, {self.first_name}! Welcome back.")


# Create several instances of User
user1 = User("Alice", "Johnson", 28, "New York", "alice@example.com")
user2 = User("Bob", "Smith", 35, "Los Angeles", "bob@example.com")
user3 = User("Charlie", "Brown", 22, "Chicago", "charlie@example.com")

# Call describe_user() and greet_user() for each user
for user in (user1, user2, user3):
    user.describe_user()
    user.greet_user()
