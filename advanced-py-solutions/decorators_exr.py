def num_check(func):
    def wrapper(num):
        if type(num) is int and num >= 0:
            return func(num)
        else:
            raise Exception('Enter a positive integer')
    return wrapper


@num_check
def factorial_calc(number):
    if number < 2:
        return number
    else:
        return number * factorial_calc(number - 1)


print(factorial_calc(6))