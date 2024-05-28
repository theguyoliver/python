def linear_search(number_list, number_to_find):
    index_list = []
    for i, n in enumerate(number_list):
        if n == number_to_find:
            index_list.append(i)
    if index_list:
        return index_list
    return -1


def binary_search(number_list, number_to_find):
    left_index = 0
    right_index = len(number_list) - 1

    while left_index <= right_index:
        mid_index = (left_index + right_index) // 2
        # we use double slash to obtain whole numbers for division
        # instead of float obtainable with a single slash
        mid_number = number_list[mid_index]

        if mid_number == number_to_find:
            return mid_index
        # This is the line that is responsible for returning the number we are looking for
        # because after finding the mid_number in each case, the code below is responsible for
        # changing where our middle is an eventually the number we are looking for becomes our
        # mid_number, and then we return it. i.e. if that number is in the list.
        if mid_number < number_to_find:
            left_index = mid_index + 1
        else:
            right_index = mid_index - 1
    return -1


# this return line above takes care of scenarios where we do not have the number_to_find in the
# number_list

def repeated_item_search(number_list, number_to_find):
    index = binary_search(number_list, number_to_find)
    index_list = [index]

    # Check for the occurrence of the num on the LHS
    i = index - 1
    while i >= 0:
        if number_list[i] == number_to_find:
            index_list.append(i)
        else:
            break
        i = i - 1

    # Check if the number also exists on the rhs from the mid_number found

    i = index + 1
    while i < len(number_list):
        if number_list[i] == number_to_find:
            index_list.append(i)
        else:
            break
        i = i + 1

    return sorted(index_list)
# Break down of what this function does:
# first, we create an instance of the binary search function and pass the necessary parameters
# This provides a single index of our number in the list, since it sorts for numbers in the middle
# of the list at all times. Once it finds this number it doesn't search anymore.
# Knowing the index where this number is located in the list we can iterate backwards from there to see
# if we also have the number on the LHS by subtracting 1 from the index and passing the new
# index to the list to see if the corresponding value of any is the value we're searching for
# if it is we append the index to the list, if it isn't we break out of the loop and update the value
# of our counter in all cases. We do the same thing for the RHS but instead by adding 1 to the index.
# Notice that after we created the list we passed the instance of the binary search function, index
# to this list, what this does is once the previous function returns the index of the number it is
# immediately added to the list.


def binary_search_recursive(number_list, number_to_find, left_index, right_index):
    if right_index < left_index:
        return -1
    # right index is always greater than left index so if this happens we want to return -1
    mid_index = (left_index + right_index) // 2
    mid_number = number_list[mid_index]

    if right_index > len(number_list) or mid_index < 0:
        return -1
    # if the right index is greater than the length of the list itself or the mid_index is less
    # than 0, remember even when we have only one item left and our mid_number is now that one
    # item, the mid_index will be 0, so if less than 0 return -1

    if mid_number == number_to_find:
        return mid_index

    if mid_number < number_to_find:
        left_index = mid_index + 1
    else:
        right_index = mid_index - 1

    return binary_search_recursive(number_list, number_to_find, left_index, right_index)


if __name__ == '__main__':
    num_list = [3, 10, 15, 27, 52, 70, 153]
    num_to_find = 15
    numbers = [1, 4, 6, 9, 11, 15, 15, 15, 17, 21, 34, 34, 56]
    # sorted_numbers = sorted(numbers)
    print(linear_search(numbers, num_to_find))
    print(binary_search(numbers, num_to_find))
    print(binary_search_recursive(numbers, num_to_find, 0, len(numbers) - 1))
    print(repeated_item_search(numbers, num_to_find))
    print(len(numbers))