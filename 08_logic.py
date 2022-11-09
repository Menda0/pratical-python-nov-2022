# If <condition> then <login> else <logic>

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


# 1
# 2
# 3
# 4
# 5
# ...

# Haja paciencia
# Do not use, use a loop instead
print("1")
print("2")
print("3")
print("4")
print("5")


## Loops

# while <Condition> do <logic>
count = 1
while count <= 10:
    print(count)
    count = count + 1

## While True, suggest by Fernando Paz
while True:
    print(count)
    count = count + 1
    if count >= 10:
        break

people = [pedro, augusto, pedro]

i = 0

while i < len(people):
    current_person = people[i]
    print(f"people[{i}] =",current_person["name"])
    i += 1

# 1 IT 
# i - 0
# current_person = people[0] = pedro

# 2 IT
# i - 1
# current_person = people[1] = augusto

# 3 IT
# i - 2
# i < len(people) = 2 < len(people) = False = Break Loop

# for <current_iteration> in <list_of_values>

for current_person in people:
    print(current_person["name"])

# IT 1
# current_person = pedro

# IT 2
# current_person = augusto