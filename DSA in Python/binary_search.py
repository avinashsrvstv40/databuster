import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print(func.__name__ +" has taken "+ str(start_time - end_time))
        return result
    return wrapper


@time_it
def linear_search(numer_list, num):
    for indx, element in enumerate(numer_list):
        if element == num:
            return indx


@time_it
def binary_search(numer_list, num):
    left_index = 0
    right_index = len(numer_list) - 1
    mid_index = 0

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        mid_number = numer_list[mid_index]

        if mid_number == num:
            return mid_index

        if mid_number < num:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1

    return -1


if __name__ == '__main__':
    num_list = [i for i in range(100000)]
    number = 9560000

    print(linear_search(num_list, number))
    print(binary_search(num_list, number))