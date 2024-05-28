
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


if __name__ == '__main__':
    e = [2, 1, 5, 7, 2, 0, 5, 1, 2, 9, 5, 8, 3]
    shell_sort(e)
    print(e)
    print(set(e))
