
# 1. Create a list of 6 people
# Example jonh = ...
# 2. People mas have the following attributes
# Example: {name:"Jonh Doe", size: 1.34, age:18}
# 3. Iterate over the list of people and create a new list with the people over 18 years old
# Example: adults = [...] if age >= 18
# 4. Iterate over the list of people and a create 3 lists, short_people, average_people and tall people
# Example: short_people = [...] if size < 1.6
# 5. Print all the list created
# Example: print(short_people)

### Provided by Pedro Almeida ###

# 1. Create a list of 6 people
# Example john = ...
# 2. People must have the following attributes
# Example: {name:"John Doe", size:1.34, age:18}
augusto = {"name":"Augusto", "age": 30,"size":1.90}
fonseca = {"name":"Fonseca", "age": 18,"size":1.55}
mirtes = {"name":"Mirtes", "age": 22,"size":2.10}
marco = {"name":"Marco", "age": 55,"size":1.60}
pedro = {"name":"Pedro", "age": 16,"size":1.72}
diogo = {"name":"Diogo", "age": 12,"size":1.35}

people = [augusto, fonseca, mirtes, marco, pedro, diogo]
# 3. Iterate over the list of people to create a new list with the people over 18 years old
adults = []
for p in people:
    if p["age"]>=18:
        adults.append(p)

# Example: adults = [ ... ] if age>= 18
# 4. Iterate over the list of people and create 3 lists, short_people, average_people, tall_people
# Example: short_people=[ ... ] if size < 1.6
short_people=[]
average_people=[]
tall_people =[]

for p in people:  
    if p["size"]<1.60:
        short_people.append(p)
    elif p["size"]>=1.60 and p["size"]<2:
        average_people.append(p)
    else:
        tall_people.append(p)

# 5. Print all the lists created 

print("People: ",people)
print("Adults: ",adults)
print("short_people: ",short_people)
print("average_people: ",average_people)
print("tall_people: ",tall_people)