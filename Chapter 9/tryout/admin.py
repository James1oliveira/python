# Base User class from Exercise 9-3 / 9-5
class User:
    """A simple class to represent a user profile."""

    def __init__(self, first_name, last_name, age, location, email):
        """Initialize user attributes."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.email = email
        self.login_attempts = 0  # From Exercise 9-5

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

    def increment_login_attempts(self):
        """Increment the value of login_attempts by 1."""
        self.login_attempts += 1

    def reset_login_attempts(self):
        """Reset login_attempts to 0."""
        self.login_attempts = 0


# Admin subclass of User
class Admin(User):
    """Represent an administrator, a special kind of user."""

    def __init__(self, first_name, last_name, age, location, email):
        """Initialize attributes of the parent class."""
        super().__init__(first_name, last_name, age, location, email)
        self.privileges = [
            "can add post",
            "can delete post",
            "can ban user",
            "can moderate comments"
        ]

    def show_privileges(self):
        """Display the administrator's privileges."""
        print(f"\nAdmin Privileges for {self.first_name} {self.last_name}:")
        for privilege in self.privileges:
            print(f"- {privilege}")


# Create an instance of Admin
admin_user = Admin("Grace", "Hopper", 35, "Arlington", "grace@example.com")

# Call method to display admin privileges
admin_user.show_privileges()
