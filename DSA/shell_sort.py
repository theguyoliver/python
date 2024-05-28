
def shell_sort(arr):
    size = len(arr)
    gap = size//2

    while gap > 0:
        for i in range(gap, size):
            anchor = arr[i]
            j = i
            while j >= gap and arr[j-gap] > anchor:
                arr[j] = arr[j-gap]
                j -= gap
            arr[j] = anchor
        gap = gap // 2
# breakdown of what the above function means. First of all we initialize our gap to n//2 which is
# the standard, then we calculate the size(length) of our array. We then run a for loop starting from
# our gap, so the index of the first item will be indexed n/2. For e.g. our list comprises 8 elements
# so our first index will be 4. Within this for loop we define our anchor i.e. arr[i] and then we
# create another variable 'j' and initialize it to 'i'. Now this variable allows us to play around with i
# without calling it directly. Next we want to check if the very first index in the list i.e. j-gap
# (that should give us index 0 in the original list) is greater than our anchor and if it is we want to swap
# it, and we continue to this as long as our j is >= gap. After swap our arr[j] value to the value we
# had at arr[j-gap]. We update our value of j by subtracting gap that is set the value at arr[j-gap]
# to our anchor which was initially arr[j] this completes the swap, and then we create an outer while loop
# which ensures the inner block of code is only executed when gap>0. Remember that we're reducing gap
# everytime by n/2, so we divide up to a point where further division would force us to have a negative
# index which isn't possible.


if __name__ == '__main__':
    tests = [
        [89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1],
        [],
        [1, 5, 8, 9],
        [234, 3, 1, 56, 34, 12, 9, 12, 1300],
        [5]
    ]

    for elements in tests:
        shell_sort(elements)
        print(elements)