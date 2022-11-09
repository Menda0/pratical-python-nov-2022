# If <condition> then <instruction> else <instruction>

augusto = {
    "name": "Augusto",
    "age": 40,
    "size": 1.75
}

pedro = {
    "name": "Pedro",
    "age": 13,
    "size": 1.40
}

person = pedro

if person["age"] >= 18:
    # print(person["name"] + " is an adult")
    # Formated string can access variables
    print(f"{person['name']} Is an adult")
else:
    print(f"{person['name']} Is a child")
    print("he cannot play")

if person["size"] >= 2:
    print(f"{person['name']} is tall")
elif person["size"] >= 1.6 and person["size"] < 2:
    print(f"{person['name']} is average")
else:
    print(f"{person['name']} is short")