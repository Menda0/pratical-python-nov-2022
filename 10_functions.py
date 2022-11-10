# Functions

# Function without input parameters without returned output
def say_hello_world():
    print("hello world")

say_hello_world()
say_hello_world()
say_hello_world()

# Function with input parameters without returned output
def say_hello_person(personName):
    print(f"hello {personName}!")

say_hello_person("Mirtes")
say_hello_person("Hugo")
say_hello_person("Diogo")

# Function with input parameters and with returned output
def is_pair(num):
    result = num % 2
    if result == 0:
        return True
    else:
        return False

def is_pair(num):
    return (num % 2) == 0

print("Is 10 pair", is_pair(10))
print("Is 3 pair =", is_pair(3))

# perimeter = 2 * pi * r
# r -> is a our parameter
# 2, pi -> constants

def circle_perimeter(r):
    pi = 3.14
    return 2 * pi * r

print("circle_perimeter(10) =", circle_perimeter(10))


# area = pi * r * r
# r -> is a our parameter
# pi -> constants
def circle_area(r):
    return 3.14 * r * r

print("circle_area(10) =", circle_area(10))

def calculate_circle_metrics(r):
    perimeter = circle_perimeter(r)
    area = circle_area(r)

    return perimeter, area

# 1! = 1
# 0! = 1
# 2! = 2*1 = 2
# 3! = 3*2*1  = 6
# 4! = 4*3*2*1 = 24
# 1! = 1 (constant)
# 0! = 1 (constant)
# 2 = 3 * 2! (calculated)
# 3 = 3 * 2! (calculated)
# 4! = 4 * 3! (calculated)
# n! = n * (n - 1)! (calculated)

# 1 * 2 * 3 * 4
# 4 * 3 * 2 * 1

# fact(4) = 24

# it 1
# n = 4
# result = 4
 
# result = result * (n-1)
# result = 4 * 3 = 12
# n-- = 3

# it 2
# n = 3
# result = 12

# result = result * (n-1)
# result = 12 * 2 = 24
# n-- = 2

# it 3
# n = 2
# result = 24
# result = 24 * 1  = 24
# n-- = 1

# it 4
# n = 1
# n > 1 = False -> escape loop

# Iteractive function
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = n
        while n > 2:
            result = result * (n-1)
            n -= 1
        return result

print("fact(1) =", fact(1))
print("fact(0) =", fact(0))
print("fact(4) =", fact(4))

# It 0
# n = 4
# result = 1

# result = 4 * 1 = 4

# IT 1
# n = 3
# result = 3 * 4

# n! = n * (n - 1)! (calculated)

def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = n * fact(n-1)
        return result

# Fact(4) -> 1
# n = 4
# result = 4 * fact(3)

# Fact(3) -> 2
# n = 3
# result = 3 * fact(2)

# Fact(2) -> 3
# n = 2
# result = 2 * fact(1)

# Fact(1) -> 4
# n = 1
# return 1
