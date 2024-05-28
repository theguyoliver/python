
def insertion_sort(elements):
    for i in range(1, len(elements)):
        anchor = elements[i]
        j = i - 1
        while j >= 0 and anchor < elements[j]:
            elements[j+1] = elements[j]
            j = j -1
        elements[j+1] = anchor
# Explaining what each line of code here means, the outer for loop allows us to start our comparison
# from the element at index 1, since we consider or first element, elements[0] to already be sorted since
# it's the only element in the list, next we run an inner while loop which checks every element after our
# anchor one by one until it gets to the end, i.e elements[0] which here or j will become minus one and we break out
# of the loop.So we want to go over each element until or j is either positive or zero because if it's negative
# it means we've reach the end of the list from the list so we break out of the loop.Also, we want the block
# of code under this loop t be executed when our anchor is less than the element just before it, and
# if that is true then we want to move the element before the anchor to the position the anchor is located
# so we can insert the anchor into the space it just left elements[j], we continue this way until we get to
# an element greater than our anchor, then we input our anchor after it.


if __name__ == '__main__':
    e = [11, 9, 29, 7, 2, 15, 28]
    insertion_sort(e)
    print(e)
