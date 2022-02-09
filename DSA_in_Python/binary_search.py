import time
from functools import lru_cache

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


# @time_it
# def binary_search(numer_list, num):
#     left_index = 0
#     right_index = len(numer_list) - 1
#     mid_index = 0

#     while left_index <= right_index:
#         mid_index = (left_index + right_index) // 2
#         mid_number = numer_list[mid_index]

#         if mid_number == num:
#             return mid_index

#         if mid_number < num:
#             left_index = mid_index + 1
#         else:
#             right_index = mid_index - 1

#     return -1

@lru_cache
def binary_search_recurssion(numer_list, num, left_index, right_index):
    if right_index < left_index:
        return -1

    mid_index = (left_index + right_index) // 2
    mid_number = numer_list[mid_index]

    if mid_number == num:
        return mid_index

    if mid_number < num:
        left_index = mid_index + 1
    else:
        right_index = mid_index - 1

    return binary_search_recurssion(numer_list, num, left_index, right_index)


if __name__ == '__main__':
    num_list = tuple([i for i in range(190000)])
    number = 95600
    left_index = 0
    right_index = len(num_list) - 1

    print(linear_search(num_list, number))
    # print(binary_search(num_list, number))
    binary_search_recurssion(num_list, number , left_index, right_index)