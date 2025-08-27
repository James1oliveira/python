# User class (from previous exercises)
class User:
    """A simple class to represent a user profile."""

    def __init__(self, first_name, last_name, age, location, email):
        """Initialize user attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        """Print a summary of the user's information."""
        print(f"\nUser Profile:")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Location: {self.location}")
        print(f"Email: {self.email}")

    def greet_user(self):
        """Print a personalized greeting."""
        print(f"Hello, {self.first_name}! Welcome back.")


# Privileges class to manage privileges list and display
class Privileges:
    """A class to store and display an admin's privileges."""

    def __init__(self, privileges=None):
        """Initialize privileges attribute."""
        if privileges is None:
            self.privileges = []
        else:
            self.privileges = privileges

    def show_privileges(self):
        """Display the privileges."""
        print("\nAdmin Privileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print("This admin has no privileges assigned.")


# Admin class inherits from User and has a Privileges instance
class Admin(User):
    """Represent an administrator, a special kind of user."""

    def __init__(self, first_name, last_name, age, location, email):
        """Initialize attributes of the parent class."""
        super().__init__(first_name, last_name, age, location, email)
        # Create a Privileges instance as an attribute
        self.privileges = Privileges([
            "can add post",
            "can delete post",
            "can ban user",
            "can moderate comments"
        ])


# Create an Admin instance
admin_user = Admin("Ada", "Lovelace", 36, "London", "ada@example.com")

# Use the Privileges instance method to show privileges
admin_user.privileges.show_privileges()
