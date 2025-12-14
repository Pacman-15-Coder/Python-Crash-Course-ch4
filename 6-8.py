"""
Make several dictionaries, where each dictionary represents a different
pet. In each dictionary, include the kind of animal and the owner's
name. Store these dictionaries in a list called pets. Next, loop through
 your list and as you do, print everything you know about each pet.
"""

pet1 = {
    "name": "Tom",
    "animal_type": "Cat",
    "owner": "Jerry"
}

pet2 = {
    "name": "Scooby-Doo",
    "animal_type": "Dog",
    "owner": "Shaggy"
}

pet3 = {
    "name": "Tweety",
    "animal_type": "Bird",
    "owner": "Granny"
}

pet4 = {
    "name": "Pikachu",
    "animal_type": "Mouse Pokémon",
    "owner": "Ash"
}

pet5 = {
    "name": "Garfield",
    "animal_type": "Cat",
    "owner": "Jon"
}

# Store all pet dictionaries in a list
pets = [pet1, pet2, pet3, pet4, pet5]

for pet in pets:
    print(f"{pet['name']} is a \t{pet['animal_type']}\t owned by \t{pet['owner']}")
