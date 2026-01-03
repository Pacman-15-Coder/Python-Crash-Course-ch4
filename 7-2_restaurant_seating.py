"""
Write a program that asks the user how many people are in their dinner
group. If the answer is more than eight, print a message saying they'll
have to wait for a table. Otherwise, report that their table is ready.
"""

amount_of_people = int(input("How many people would be joining us today?: "))

if amount_of_people > 8:
    print("Dear Customer,\n\t You will have to wait for your table.")
elif amount_of_people <= 8:
    print("Dear Customer,\n\t You're table is ready.")
