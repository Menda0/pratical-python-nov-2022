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

### Provided by Fernando Paz ###
def is_prime_number(num):
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                return False
        return True
    else:
        return False

# Get the greatest common divisor between two numbers
# get_gcd(number1, number2)

### Provided by Carlos Lopes ###
def get_gcd(n1,n2):
    n=min(n1,n2)
    i=n
    while i>1:
        if n1%i==0 and n2%i==0:
            return i
        i-=1
    return 1

print("get_gcd(48, 60) =", get_gcd(48, 60))

# Seq Fibonnaci

# fib(0) = 0 (constant)
# fib(1) = 1 (constant)
# fib(2) = fib(2-1) + fib(2-2) = fib(1) + fib(0) = 1 + 0 = 1
# fib(3) = fib(3-1) + fib(3-2) = fib(2) + fib(1) = 1 + 1 = 2
# fib(4) = fib(4-1) + fib(4-2) = fib(3) + fib(2) = 2 + 1 = 3
# fib(5) = fib(5-1) + fib(5-2) = 2 + 3 = 5
# fib(n) = fib(n-1) + fib(n-2)

### Provided By Raquel Marques ###
def fib(n):
        if n==0:
            return 0
        elif n==1:
            return 1   
        else:
            result = fib(n-1) + fib(n-2)
            return result

# fib(24) = fib(23) -> 1 + fib(22) -> 2
# 1 -> fib(23) = fib(22) -> 3 + fib(21) -> 4
# 3 -> fib(22) = fib(21) - fib(20)

# Programacao dinamica
# Solves the inificient recursion
# arr_aux = [0,1,2,3,5, ...]
