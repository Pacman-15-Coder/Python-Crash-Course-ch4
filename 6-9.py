"""
Make a dictionary called favorite_places. Think of three names to use as
 keys in the dictionary, and store one to three favorite places for each
  person. To make this exercise a bit more interesting, ask some friends
  to name a few of their favorite places. Loop through the dictionary,
  and print each person's name and their favorite places.
"""
#Create dictonary with multiple values per key

favorite_places = {
    "Alice": ["Paris", "New York", "Tokyo"],
    "Bob": ["London", "Sydney"],
    "Charlie": ["Rome", "Barcelona", "Amsterdam"]
}

for person, places in favorite_places.items():
    print(f"\n{person.title()}'s favorite places:")
    for place in places:
        print(f"\n\t-{place.title()}")
