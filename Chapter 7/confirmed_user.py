# Start with a list of users that need to be verified
unconfirmed_users = ['alice', 'brian', 'candace']

# Create an empty list to hold users once they are confirmed
confirmed_users = []

# Loop runs as long as there are unconfirmed users
while unconfirmed_users:
    # Remove the last user from the unconfirmed list and store them in current_user
    current_user = unconfirmed_users.pop()

    # Simulate the verification process (you can imagine checking their info here)
    print(f"Verifying user: {current_user.title()}")

    # Add the verified user to the confirmed list
    confirmed_users.append(current_user)

# Print a message after all users have been verified
print("\nThe following users have been confirmed:")

# Loop through the confirmed users and print each one
for confirmed_user in confirmed_users:
    print(confirmed_user.title())
