def swap(a, b, arr):
    tmp = arr[a]
    arr[a] = arr[b]
    arr[b] = tmp


def bubble_sort(elements):
    size = len(elements)

    for i in range(size - 1):
        swapped = False

        for j in range(size - 1 - i):
            if elements[j] > elements[j + 1]:
                swap(j, j + 1, elements)
                swapped = True
        if not swapped:
            break


# in the inner for loop when we subtract i we are trying to reduce the range of the elements
# we are trying to sort, this way we can save some extra time since, those elements in the list
# are already sorted. Example the normal range without subtracting 'i' would be 7-1=6. Here the size
# of the list is size, meaning that we'll reach the last item each time we iterate over that
# even tho we would have reach it and sorted it in previous iterations, so subtracting 'i' ensures
# we only stop at items which haven't been sorted yet.

# The outer for loop cause our inner for loop to repeat the process the range number of times to
# sort all the elements in the list

# Another challenge we may experience with bubble sort is that after running the first comparison
# without swapping, the computer will still go on to run the entire for loop despite our list being
# sorted already. To tackle this, we include a variable named swapped and initialize it to false.
# so when we actually swap any item in the list this variable is initialized true, else if false
# after our first iteration we break out of the loop, to save time.


if __name__ == '__main__':
    e = [11, 9, 29, 7, 2, 15, 28]
    bubble_sort(e)
    print(e)
