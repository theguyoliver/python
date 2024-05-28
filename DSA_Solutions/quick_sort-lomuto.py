def swap(a, b, arr):
    if a != b:
        tmp = arr[a]
        arr[a] = arr[b]
        arr[b] = tmp


def lomuto_partition(elements, start, end):
    pi = start
    pivot = elements[end]

    for j in range(start, end):
        if elements[j] <= pivot:
            swap(j, pi, elements)
            pi += 1

    swap(pi, end, elements)

    return pi
# Break down of the block of code above, we set our pivot to the last element, and p_index to start
# Then we iterate through our list and if we find an element which is less than or equal
# to our picot we swap it with the element at p_index and increase the index by 1, if it is
# greater than our pivot we leave it and don't increase p_index.
# Since that block of code swaps up until the element in front of our pivot
# we then swap our pivot with the element at p_index. From here we have LHS which is< pivot and RHS
# greater than pivot. We then perform the recursion in our quicksort() working on each side separately
# by setting an appropriate start and end point in each case.


def quick_sort(elements, start, end):
    if len(elements) == 1:
        return
    if start < end:
        pi = lomuto_partition(elements, start, end)
        quick_sort(elements, start, pi-1)
        quick_sort(elements, pi+1, end)


if __name__ == '__main__':
    e = [11, 9, 29, 7, 2, 15, 28]
    quick_sort(e, 0, len(e)-1)
    print(e)
