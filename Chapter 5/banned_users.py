# Create a list of users who are banned from posting
banned_users = ['andrew', 'carolina', 'david']

# Set the current user's name
user = 'marie'

# Check if the user is not in the list of banned users
if user not in banned_users:
    # If the user is not banned, allow them to post a response
    print(f"{user.title()}, you can post a response if you wish.")

    