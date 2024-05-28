import time
import math


def time_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, 'took', str((end - start) * 1000) + 'ms')
        return result
    return wrapper


@time_time
def calc_square(numbers):
    result = []
    # start = time.time()
    if numbers:
        for n in numbers:
            result.append(n * n)
        # end = time.time()
        # print('Time taken by calc_square:', str((end - start) * 1000) + 'ms')
        return result


@time_time
def calc_cube(numbers):
    result = []
    # start = time.time()
    if numbers:
        for n in numbers:
            result.append(math.pow(n,3))
        # end = time.time()
        # print('Time taken by calc_square:', str((end - start) * 1000) + 'ms')
        return result

# In the above examples the comments showcase the other way of calculating time without decorators
# However, because this method is not very efficient - makes our code less readable and the logic
# of time also contributes to the time taken to execute the function. We implement decorators instead
# as is shown in the executable pieces of code


arr = range(1, 100000)
output_square = calc_square(arr)
output_cube = calc_cube(arr)
