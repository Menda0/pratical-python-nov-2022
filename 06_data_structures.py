
## List(Array)

## Empty list
list1 = []
print("type(list1) =", type(list1))

list2 = [1,2,3,4,5,6,7,8,9]
# [0] -> 1
# [1] -> 2
# [3] -> 4
# [7] -> 8
# [8] -> 9 (last element of the array, length-1)
# [10] -> Index out of range
# [9] -> Index out of range
print("list[3] =",list2[3])

# List can have multiple type
list3 = ["Marco", 32, 1.75]

print("list3[2] =",list3[2])

# Concat list
list4 = list2 + list3

print("list4 =", list4)

list5 = ["Pedro"]

# Explode
list6 = list5 * 3

print("list6 =", list6)

is_pedro_in_list = "Pedro" in list6

print("is_pedro_in_list =", is_pedro_in_list)

is_hugo_in_list = "Hugo" in list6

print("is_hugo_in_list =", is_hugo_in_list)

# Add to last element of the list
list6.append("Hugo")

is_hugo_in_list = "Hugo" in list6

print("list6 =", list6)
print("is_hugo_in_list =", is_hugo_in_list)

# Add element to index
list6.insert(1, "Jose")

print("list6 =", list6)

# Remove last added element to the list
list6.pop()

print("list6 =", list6)

## Remove Pedro from the list
list6.remove("Pedro")
print("list6 =", list6)

## Reverse order of the list
list6.reverse()
print("list6 =", list6)

## Sub list of list6[<first_index>:<last_index>]
list7 = list6[0:2]

print("list7 =",list7)

# [:<last_index>] == [0:<last_index>]
list8 = list6[:2]

print("list8 =", list8)

list9 = list6[2:3]

print("list9 =",list9)

list10 = list6[2:]

print("list10 =", list10)

size = len(list6)

print("size =", size)

# Tuple
tuple1 = ()

print("type(tuple1) =", type(tuple1))

tuple2 = (1,2,3,4,5)
# 0 -> 1
# 4 -> 5
# 10 -> Out of bounds
print("tuple2[3] =", tuple2[3])

# Tuple can have multiple types
tuple3 = ("Marco", 32, 1.74)

list11 = ["Ricardo", 24, 1.80]

list11[1] = 34

print("list11 =", list11)

tuple4 = ("Diogo", 27, 2.5)

# Tuple does not support item assingment (Not editable)
# tuple4[2] = 1.82 

# Dictionaries
dict1 = {}

print("type(dict1) =", type(dict1))

dict2 = {
    "name": "Mirtes",
    "age": 24,
    "height": 1.68
}

# name -> Mirtes
# age -> 24
# height - 1.68

print("dict2['name'] =", dict2["name"])
print("dict2['age']", dict2["age"])

dict2["age"] = 32

print(dict2)

# Remove key
del dict2["height"]

print(dict2)

values = list(dict2.values())

# Casting to list beacause the return of .values() is type dict_values
print("type(values) =", type(values))
print(values)

# Casting to list beacause the return of .keys() is type dict_keys
keys = list(dict2.keys())

print("type(keys) =",type(keys))
print("keys =", keys)

subjects = ["Python", "Linux", "Javascript"]

# Add a new key
dict2["subjects"] = subjects

print("dict2 =", dict2)

print("dict2['subjects'][0] =",dict2["subjects"][0])

dict3 = {
    "name": "Hugo",
    "address":{
        "number": 20,
        "postal_code": 2900,
        "description": "Rua das flores"
    }
}

print(dict3["address"]["postal_code"])