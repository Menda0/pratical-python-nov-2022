
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