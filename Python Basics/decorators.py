import time

def time_it(func):
    def wrapper(a):
        start = time.time()
        result = func(a)
        end = time.time()
        print(func.__name__ + " has taken: " + str(end-start))
        return result
    return wrapper

@time_it
def cube(x):
    result = []
    for i in x:
        result.append(i**3)
    return result

@time_it
def square(x):
    result = []
    for i in x:
        result.append(i**2)
    return result

array = range(1,100)
cu = cube(array)
sq = square(array)
print(cu, sq)