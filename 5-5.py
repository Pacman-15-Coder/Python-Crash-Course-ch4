"""
Turn your if-else chain from exercise 5.4 into an if-elif-else chain.

If the alien is green, print a message that the player earned 5 points.

If the alien is yellow, print a message that the player earned 10.

If the alien is red, print a message that the player earned 15.

Write three versions of this program, making sure each message is
printed for the appropriate color alien.
"""

alien_color = 'green'
if alien_color == 'green':
    print("You earned 5 points.")

alien_color = 'yellow'
if alien_color == 'yellow':
    print("You earned 10 points.")

alien_color = 'red'
if alien_color == 'red':
    print("You earned 15 points.")

# ver1 above

if alien_color == 'green':
    print("You earned 5 points.")

elif alien_color == 'yellow':
    print("You earned 10 points.")

elif alien_color == 'red':
    print("You earned 15 points.")

#ver2 above

alien_color = [
    'green',
    'yellow',
    'red'
]

for c in alien_color:
    if c == 'green':
        print("You earned 5 points.")
        break

    if c == 'yellow':
        print("You earned 10 points.")
        break

    if c == 'red':
        print("You earned 15 points.")
        break

# ver 3 above
# I've written 3 versions as he specified to write 3 versions so idk