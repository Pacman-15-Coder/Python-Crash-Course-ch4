"""
A movie theater charges different ticket prices depending on a person's
age. If a person is under the age of 3, the ticket is free; if they
are between 3 and 12, the ticket is $10; and if they are over age 12,
the ticket is $15. Write a loop in which you ask users their age, and
then tell them the cost of their movie ticket.
"""

while True:
    age = (input("Enter your age(enter quit if you would like to leave): "))
# I have not added a quit statement as it would both be complex and he didnt specify for it
    int(age)

    if age < 3:
        print("Your ticket costs 0$")
    elif age >= 3 and age < 12:
        print("Your ticket costs 10$")
    elif age > 12:
        print("Your ticket costs 15$")


# the above code checks age using the if-elif chain