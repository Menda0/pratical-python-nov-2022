
def fact(n):
    if n == 0 or n == 1:
        return 1
    else:
        result = n * fact(n-1)
        return result

def fib(n):
        if n==0:
            return 0
        elif n==1:
            return 1   
        else:
            result = fib(n-1) + fib(n-2)
            return result