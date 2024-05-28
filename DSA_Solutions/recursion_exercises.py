def list_sum(arr, n):
    if n == 0:
        return 0
    elif n == 1:
        return arr[n - 1]

    # This adds from the end of the list to the first
    return arr[n - 1] + list_sum(arr, n - 1)

    # This will start dding from the beginning of the list and will reduce the list each time
    # and add the item at index 0 to the previous sum. But we have to modify our fun to not take n as
    # parameter
    return arr[0] + list_sum(arr[1:])


# This functions aims to recursively sum all the elements within a list starting from the last element


def int_to_string(i):
    return str(i)


# Here we're just converting any integer to a string, to confirm that this function works we try
# to concatenate our output with another string and if it doesn't display an error then this func works.


# Define a function named recursive_list_sum that calculates the sum of elements in a nested list
def recursion_list_sum(arr):
    total = 0

    for i in arr:
        if type(i) is type([]):
            total += recursion_list_sum(i)
        else:
            total += i

    return total


def factorial_int(n):
    if n <= 1:
        return 1
    else:
        return n * factorial_int(n - 1)


# Define a function named fibonacci that calculates the nth Fibonacci number
def fib(n):
    if n == 0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        return fib(n-1) + fib(n-2)


# Define a function named sumDigits that calculates the sum of the digits of a given number 'n'
def int_sum(n):
    if n == 0:
        return n
    else:
        return n % 10 + int_sum(int(n / 10))
#    or return n%10 + int_sum(n//10)


# Define a function named sum_series that calculates the sum of a series of numbers
def sum_series(n):
    size = 2

    if n < 1:
        return 0
    else:
        return n + sum_series(n - size)


# Define a function named harmonic_sum that calculates the sum of a series of numbers
def harmonic_sum(n):
    if n < 2:
        return n
    else:
        return 1/n + harmonic_sum(1 / (n-1))


# Define a function named geometric_sum that calculates the geometric sum up to 'n' terms
def geometric_sum(n, r):
    if n < 1:
        return 0
    else:
        return n + geometric_sum(n/r, r)


# Define a function named power that calculates the result of 'a' raised to the power of 'b'
def power(a,b):
    if b == 0:
        return 1
    elif b == 1:
        return a
    if a == 0:
        return 0

    return a * pow(a, b - 1)


# Define a function named Recurgcd that calculates the greatest common divisor (GCD)
# of two numbers 'a' and 'b' using recursion and the Euclidean algorithm
def recurgcd(a, b):
    low = min(a,b)
    high = max(a,b)

    if low == 0:
        return high
    if low == 1:
        return 1
    else:
        return recurgcd(low, high % low)
#     here we drop the high and pick the low and remainder everytime


if __name__ == '__main__':
    e = [1, 5, 8, 9]
    # print(list_sum(e, len(e)))
    # print(int_to_string(19) + ' years')
    # print(factorial_int(-8))
    # print(sum_series(8))
    # print(recursion_list_sum([3, 4, [12, 3], [1, 2]]))
    # print(geometric_sum(8, 2))
    print(power(8, 2))
    print(recurgcd(14, 12))
