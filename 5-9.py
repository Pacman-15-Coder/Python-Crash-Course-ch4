"""
Add an if test to hello_admin.py to make sure the list of users is not
empty.

If the list is empty, print the message We need to find some users!

Remove all of the usernames from your list, and make sure the correct
message is printed."""

usernames = []

if len(usernames) == 0:
    print("We need to find more users!")
else:
    for user in usernames:
        if user.lower() == 'admin':
            print("Hello Admin! \t\n Would you like to see a status report?")
        if user.lower() == 'user1' or 'user2' or 'user3' or 'user4':
            print("Hello User!")