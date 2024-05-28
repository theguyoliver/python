
def swap(a, b, arr):
    tmp = arr[a]
    arr[a] = arr[b]
    arr[b] = tmp
# how to swap values in a list in python


def partition(elements, start, end):
    pivot_index = start
    pivot = elements[pivot_index]

    while start < end:
        while start < len(elements) and elements[start] <= pivot:
            start += 1

        while elements[end] > pivot:
            end -= 1

        if start < end:
            swap(start, end, elements)

    swap(pivot_index, end, elements)

    return end
# In the above we are returning end because after swapping that's going to be the new
# position of our pivot


def quick_sort(elements, start, end):
    if start < end:
        pi = partition(elements, start, end)
        quick_sort(elements, start, pi - 1)
        quick_sort(elements, pi + 1, end)


if __name__ == '__main__':
    e = [11, 9, 29, 7, 2, 15, 28]
    quick_sort(e, 0, len(e) - 1)
    print(e)
