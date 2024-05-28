
def swap(a, b, arr):
    tmp = arr[a]
    arr[a] = arr[b]
    arr[b] = tmp


def bubble_sort(elements, key=None):
    size = len(elements)

    for i in range(size - 1):
        swapped = False

        for j in range(size - 1 - i):
            a = elements[j][key]
            b = elements[j+1][key]

            if a > b:
                swap(j, j + 1, elements)
                swapped = True

        if not swapped:
            break

# To solve this exercise we want to be able to access the dict inside elements, so each list would
# be at elements[i] where 'i' start from 0 to len(elements) - 1. Then in each dict we can access a
# value using its key, and then we can sort this values both strings and int. Hence, why we have
# elements[i] to access the dict and elements[i][key] to access the value of a key within that dict.


if __name__ == '__main__':
    e = [11, 9, 29, 7, 2, 15, 28]
    elements = [
        {'name': 'mona', 'transaction_amount': 1000, 'device': 'iphone-10'},
        {'name': 'dhaval', 'transaction_amount': 400, 'device': 'google pixel'},
        {'name': 'kathy', 'transaction_amount': 200, 'device': 'vivo'},
        {'name': 'aamir', 'transaction_amount': 800, 'device': 'iphone-8'},
    ]
    bubble_sort(elements, 'transaction_amount')
    print(elements)