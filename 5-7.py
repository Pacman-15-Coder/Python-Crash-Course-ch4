"""
Make a list of your favorite fruits, and then write a series of
independent if statements that check certain fruits in your list.

Make a list of your three favorite fruits in your list.

Write five if statements. Each should check whether a certain kind of
fruit is in your list. If the fruit is in your list, the if block should
 print a statement, such as 'You really like bananas!'
 """

fruits = [
    "Apple",
    "Banana",
    "Mango",
    "Orange",
    "Grapes",
    "Pineapple",
    "Strawberry",
    "Watermelon",
    "Papaya",
    "Kiwi"
]

for f in fruits:
    if f == "apple":
        print("You really like apples!")
    elif f == "banana":
        print("You really like bananas!")
    elif f == "orange":
        print("You really like oranges!")
    elif f == "strawberry":
        print("You really like strawberries!")
    elif f == "dragonfruit":
        print("You really don't like dragonfruit!")