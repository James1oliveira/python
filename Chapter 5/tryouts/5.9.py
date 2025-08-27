# List of usernames, currently empty
usernames = []

# Check if the list is empty
if usernames:
    # If not empty, greet each user
    for username in usernames:
        if username == 'admin':
            print("Hello admin, would you like to see a status report?")
        else:
            print(f"Hello {username.title()}, thank you for logging in again.")
else:
    # If the list is empty, print this message
    print("We need to find some users!")
