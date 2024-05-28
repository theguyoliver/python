
def selection_sort(arr):
    for i in range(len(arr)-1):
        min_index = i
        for j in range(min_index+1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        if i != min_index:
            arr[i], arr[min_index] = arr[min_index], arr[i]

# Breakdown of what that block of code means. First of all we run a for loop for range(len(list)) and we
# assign our min index to the first index which in our case above was 'i', we then run a second for loop
# with range min index + 1 this allows us to compare all elements after our min index with our min index
# and any one which is less than our min index, we set the index of min index to that index(to that j)
# then we swap the element at position/index i with the element at our new min_index

# we don't run through the entire list we stop at the item just before the last index because if the
# rest of the list is sorted then it too will be sorted. Talking about our outer for loop.


if __name__ == '__main__':
    tests = [
        [89, 78, 61, 53, 23, 21, 17, 12, 9, 7, 6, 2, 1],
        [],
        [1, 5, 8, 9],
        [234, 3, 1, 56, 34, 12, 9, 12, 1300],
        [5]
    ]

    for elements in tests:
        selection_sort(elements)
        print(elements)