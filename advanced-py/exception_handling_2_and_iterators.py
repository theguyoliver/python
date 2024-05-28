
# We make use of the try and except block for exception handling in python, and we can raise exceptions
# as they occur using the raise keyword.

arr = [2, 5, 9, 12, 0]
reversed_arr = reversed(arr)

for i in arr:
    try:
        i / 1
    except ZeroDivisionError as e:
        print('We cannot divide an int by 0')
    # finally:
    #     print('This line of code is always executed irrespective of what happens in the try and except blocks')
    else:
        print('This line of code is executed when we do not execute our except block of code because we did not '
              'encounter any exception')
# Once we call finally block of code the computer exits the sequence, when we're using it, it must
# be the last block we call

print(dir(arr))
itr = iter(arr)
itr1 = iter(reversed_arr)
print(dir(itr))
print(next(itr))
print(next(itr1))
# The above code then begins to bring out each element in our just like we would do when running a
# for loop, hence this is the underlying mechanism of how our for loops are run.
