# user_admin.py

class User:
    """A simple class to represent a user profile."""

    def __init__(self, first_name, last_name, age, location, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.location = location
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        print(f"\nUser Profile:")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Location: {self.location}")
        print(f"Email: {self.email}")

    def greet_user(self):
        print(f"Hello, {self.first_name}! Welcome back.")


class Privileges:
    """A class to store and display an admin's privileges."""

    def __init__(self, privileges=None):
        if privileges is None:
            self.privileges = []
        else:
            self.privileges = privileges

    def show_privileges(self):
        print("\nAdmin Privileges:")
        if self.privileges:
            for privilege in self.privileges:
                print(f"- {privilege}")
        else:
            print("This admin has no privileges assigned.")


class Admin(User):
    """Represent an administrator, a special kind of user."""

    def __init__(self, first_name, last_name, age, location, email):
        super().__init__(first_name, last_name, age, location, email)
        self.privileges = Privileges([
            "can add post",
            "can delete post",
            "can ban user",
            "can moderate comments"
        ])
