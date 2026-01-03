"""
Write different versions of either exercise 7.04 or 7.05 that do each of
 the following at least once:

 Use a conditional test in the while statement to stop the loop.

 Use an active variable to control how long the loop runs.

 Use a break statement to exit the loop when the user enters a 'quit'
 value.
 """

while True:
    age = (input("Enter your age(enter quit if you would like to leave): "))

    if age.lower() == "quit":
        print("Goodbye!")
        break


    int(age)

    if age < 3:
        print("Your ticket costs 0$")
    elif age >= 3 and age < 12:
        print("Your ticket costs 10$")
    elif age > 12:
        print("Your ticket costs 15$")


# This is is a example of 7.5 and not 7.4