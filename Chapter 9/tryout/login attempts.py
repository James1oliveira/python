class User:
    """A simple class to represent a user profile."""

    def __init__(self, first_name, last_name, age, location, email):
        """Initialize attributes to describe a user."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.email = email
        self.login_attempts = 0  # New attribute to track login attempts

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

    def increment_login_attempts(self):
        """Increment the value of login_attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset the value of login_attempts to 0."""
        self.login_attempts = 0


# Create an instance of User
user = User("Diana", "Prince", 30, "Themyscira", "diana@example.com")

# Simulate some login attempts
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()

# Print the number of login attempts
print(f"Login attempts: {user.login_attempts}")

# Reset the login attempts
user.reset_login_attempts()

# Print login attempts again to confirm reset
print(f"Login attempts after reset: {user.login_attempts}")
