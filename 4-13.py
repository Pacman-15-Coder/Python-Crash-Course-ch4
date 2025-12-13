menu_items = (
    "Margherita Pizza",
    "Pasta Alfredo",
    "Caesar Salad",
    "Garlic Bread",
    "Tomato Soup"
)

print ("McPython's ORIGINAL Items:")

for item in menu_items:
    print(f"\t{item.title()} is very tasty and cheap")
# Up to now ive checked everything out with PEP guidelines seems fine but i want to test the for loop a bit.

menu_items = (
    "Margherita Pizza",
    "Pasta Alfredo",
    "Orange Chicken",
    "Spicy Bread",
    "Biriyani"
)

print ("McPython's MODIFIED Items:")

for item in menu_items:
    print(f"\t{item.title()} is very tasty and cheap \n BUT NOT TASTIER THAN ORIGINALS")

#I wanna finish this chapter quick to start if statements