anony234 = {
    'First Name': 'Anonymous',
    'Last Name': 'Hat',
    'Age': 34,
    'Speciality': 'Hacking',
    'City': 'San Francisco'
}

physein = {
    'First Name': 'Albert',
    'Last Name': 'Einstein',
    'Age': 78,
    'Speciality': 'Physics',
    'City': 'Berlin'
}

openpty = {
    'First Name': 'Julius',
    'Last Name': 'Oppenheimer',
    'Age': 45,
    'Speciality': 'Nuclear',
    'City': 'Nevada'
}

users: list[dict[str, str | int]] = [anony234, physein, openpty]

for u in users:
    print(
        f"first name: {u['First Name']}, "
        f"last name: {u['Last Name']}, "
        f"age: {u['Age']}, "
        f"speciality: {u['Speciality']}, "
        f"city: {u['City']}"
    )
