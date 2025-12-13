"""
Make a list of five or more usernames, including the name 'admin.'
Imagine you are writing code that will print a greeting to each user
after they log in to a website. Loop through the list, and print a
greeting to each user.

If the username is 'admin', print a special greeting, such as Hello
admin, would you like to see a status report?

Otherwise, print a generic greeting, such as Hello Jaden, thank you for
logging in again.
"""

usernames = ['admin', 'user1', 'user2', 'user3', 'user4']

if 'admin' in usernames:
    print("Hello admin, you are now logged in!\t\n would you like to see a status report?")
if 'user1' or 'user2' or 'user3' or 'user4' in  usernames[1:4]:
    print("Hello User , you are logged in now!")