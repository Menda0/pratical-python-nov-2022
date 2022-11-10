# 1. Create a function to calculate the area and parimeter of a square
# Example: a = l*l, p = 4*l
# 2. Create a function to calculate the area of a triangle
# Example: a = (b*h) / 2

### Provided by Jose Castanheira ###

def area_parimeter_square(l):
    area = l * l
    parimeter = l * 4
    return area, parimeter

print("Square - Area and parimeter with size (6) =", area_parimeter_square(6))

def area_parimeter_triangle(b,h):
    area = (b * h) /2
    return area

print("Triangle - Area with base (6) Height (3) =", area_parimeter_triangle(6,3))

# 1. Define a list of values
# Example: l = [1,2,3,4,5,6,7,8,9,10]
# 2. create a function that iterate the list l and create a new list with the multiple of 2

### Provided Ricardo Alves ###

lista = [1,2,3,4,5,6,7,8,9,10]

def multiple_of_2(lista):
    list_multiple_of_2 = []
    for num in lista:
        if num % 2 == 0:
            list_multiple_of_2.append(num)     
    return list_multiple_of_2
print(multiple_of_2(lista))


# Prime Numbers
# Number have to be greater than 1
# And can be divisible by themselves and 1
# def isPrime(n) -> boolean
# 1 -> False
# 2 -> True
# 3 -> True
# 4 -> False
# 5 -> True

# Get the greatest common divisor between two numbers
# get_gcd(number1, number2)

# Seq Fibonnaci

# fib(0) = 0 (constant)
# fib(1) = 1 (constant)
# fib(2) = fib(2-1) + fib(2-2) = fib(1) + fib(0) = 1 + 0 = 1
# fib(3) = fib(3-1) + fib(3-2) = fib(2) + fib(1) = 1 + 1 = 2
# fib(4) = fib(4-1) + fib(4-2) = fib(3) + fib(2) = 2 + 1 = 3
# fib(5) = fib(5-1) + fib(5-2) = 2 + 3 = 5
# fib(n) = fib(n-1) + fib(n-2)