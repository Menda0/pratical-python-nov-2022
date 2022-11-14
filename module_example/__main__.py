# actual module -> module_example
from . import fib, fact
# from sys import argv
import sys


num = int(sys.argv[1])
print(f"fact({num}) =", fact(num))

if __name__ == "__main__":

    # sys -> native module 
    # sys.argv -> its a list, with all arguments
    # sys.argv[0] -> module name
    # sys.argv[1] -> number to be calculate in our fib function
    # python -m module_example 23 
    # print(sys.argv) -> [__main__.py, 23]
    num = int(sys.argv[1])
    print(f"fib({num}) =",fib(num))