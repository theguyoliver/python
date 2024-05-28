
def merge_sort(arr):
    if len(arr) <= 1:
        return

    mid = len(arr)//2
    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    merge_sort_two_list(left, right, arr)


def merge_sort_two_list(a, b, arr):
    len_a = len(a)
    len_b = len(b)
    i = j = k = 0

    while i < len_a and j < len_b:
        if a[i] < b[j]:
            arr[k] = a[i]
            i += 1
        else:
            arr[k] = b[j]
            j += 1
        k += 1
    while i < len_a:
        arr[k] = a[i]
        i += 1
        k += 1
    while j < len_b:
        arr[k] = b[j]
        j += 1
        k += 1

# What that block of code means is that we start at i and j = 0, and we compare the values of the two lists
# at that index, and that which is lesser is appended to our sorted_list, and we increase the index by 1
# i.e. from 0 to 1, again we compare it with the previous index of the other list i.e. 0 and the lesser
# one is appended to the list. The second and the third while loops are used to cater for cases where
# either list a or list b longer than the other. What we do in these situations is just to append the remain
# elements to the list. Remember that the two lists are sorted and the rightmost elements will be greater
# than the rest. Lastly we return the new sorted list we created.

# Due to the expensiveness of space complexity with the method described above, we can modify the function
# to not return anything, so once we call the function on an array it rearranges the array without the
# need to create a new array(sorted_list)


if __name__ == '__main__':
    e = [17, 12, 9, 21, 33, 2, 8]
    # f = [90, 20, 1, 8]
    # sorted_e = sorted(e)
    # sorted_f = sorted(f)
    # print(merge_sort_two_list(sorted_e, sorted_f))
    merge_sort(e)
    print(e)


