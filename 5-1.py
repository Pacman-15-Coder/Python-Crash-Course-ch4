"""
Write a series of conditional tests. Print a statement describing each
test and your prediction for the results of each test. Your code should
look something like this:

car = 'subaru'
print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

Look closely at your results, and make sure you understand why each line
evaluates to True or False.

Create at least 10 tests. Have at least 5 tests evaluate to True and
another 5 tests evaluate to False.
"""

MOTORCYCLE = "Ducati"

if MOTORCYCLE.lower() == "ducati":
    print("Is your motorcycle Ducati I predict yes")

else:
    print("Is your motorcycle Ducati I predict no")

Days = 366

if Days >= 365:
    print("I sense this year is a leap year")

dictionary_owned = "Oxford Mini"

if dictionary_owned.lower() == "Oxford Mini" or "New American":
    print("This year you shall improve your grammar")

fake_list = []
length_FL = len(fake_list)

if length_FL > 0:
    print("This is a list that has purpose\nThis is not empty")
else:
    print ("This is a list that has no purpose\nThis is empty")