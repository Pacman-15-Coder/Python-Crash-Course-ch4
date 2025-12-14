"""
Modify your program from exercise 6.2 so each person can have more than
one favorite number. Then print each person's name along with their
favorite numbers.
"""
favorite_numbers = {'alice': [7, 14],
                    'bob': [12, 24],
                    'claire': [3, 6],
                    'david': [42, 5],
                    'emily': [17, 4]
                    }

for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()}'s favorite numbers:")

    for number in numbers:
        print(f"\t\n*{number}")