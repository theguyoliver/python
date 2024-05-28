def merge_sort(arr, key, descending=False):
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid], key, descending)
    right = merge_sort(arr[mid:], key, descending)

    sorted_list = merge_sort_two_list(left, right, key, descending)
    return sorted_list


def merge_sort_two_list(a, b, key, descending=False):
    merged = []
    len_a = len(a)
    len_b = len(b)

    if descending:
        while len_a > 0 and len_b > 0:
            if a[0][key] >= b[0][key]:
                merged.append(a.pop(0))
            else:
                merged.append(b.pop(0))
    else:
        while len_a > 0 and len_b > 0:
            if a[0][key] <= b[0][key]:
                merged.append(a.pop(0))
            else:
                merged.append(b.pop(0))

    merged.extend(a)
    merged.extend(b)

    return merged


if __name__ == '__main__':
    elements = [
        {'name': 'vedanth', 'age': 17, 'time_hours': 1},
        {'name': 'rajab', 'age': 12, 'time_hours': 3},
        {'name': 'vignesh', 'age': 21, 'time_hours': 2.5},
        {'name': 'chinmay', 'age': 24, 'time_hours': 1.5},
    ]
    sorted_list = merge_sort(elements,'age', False)
    print(sorted_list)
