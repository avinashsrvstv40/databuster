#Method 1
fib_cache = {}

def fibonacci(n):
    if n in fib_cache:
        return fib_cache[n]
    if n==0 or n==1:
        value = n
    else:
        value = fibonacci(n-1) + fibonacci(n-2)
    
    fib_cache[n] = value
    return value

if __name__ == "__main__":
    for i in range(1,1000):
        print("fibonacci of %d is %d" % (i, fibonacci(i)))


#######################################################################################################

#Method 2

from functools import lru_cache

@lru_cache
def fibonacci(n):
    if n == 0 or n == 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

if __name__ == "__main__":
    for i in range(0,1000):
        print("fibonacci of %d is %d" % (i, fibonacci(i)))

