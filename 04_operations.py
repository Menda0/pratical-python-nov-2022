# Math operations

number1 = 2
number2 = 3

number3 = number1 + number2

print("number3 =",number3)
print("type(number3) =", type(number3))

number4 = number1 + 3.5

print("number4 =", number4)
print("type(number4) =", type(number4))

number5 = number1 - 2

print("number5 =", number5)

number6 = 3.14
number7 = 1
number8 = number6 + number7

print("number8 =", number8)

number9 = number1 * 2

print("number9 =", number9)

number10 = number1 / 2

print("number10 =", number10)

number11 = number1 % 2

print("number11 =", number11)

number12 = 10 % 2 

print("number12 =", number12)

number13 = 9 % 3 

# is 0 becayse us devisable by 3
print("number13 =", number13)

# is not 0 because 10 is not devisable by 3
number14 = 10 % 3

print("number14 =", number14)

verdadeiro = True
falso = False

print("verdadeiro == falso" , verdadeiro == falso)

print("number1 == number2", number1 == number3)

print("number1 != number2 ", number1 != number2)

print("0 != None", 0 != None)

print("number1 > number2", number1 > number2)

print("number1 <= number2", number1 <= number2)

boolean1 = number1 >= number2

print("boolean1 =", boolean1)
print("type(boolean1) =", type(boolean1))

# False and True = False
boolean2 = number1 >= number2 and number1 == 2
print(boolean2)

# False or True = True
boolean3 = number1 >= number2 or number1 == 2

# False and False = False
boolean4 = number1 >= number2 and number1 == 1

# False or False = False
boolean5 = number1 >= number2 or number1 == 1

# Type casting
age = 32

message = "Marco is " + str(age) + " years old"

print(message)

string1 = "1000"
string2 = "2000"

print(string1 + string2)

print(int(string1) + int(string2))