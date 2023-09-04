


def insertion_sort(list_to_sort):
    # the first element is already in the "sorted side"
    # for all the other elements, we should do things
    # starting at the second element, iterate until the end of the array
    for i in range(1, len(list_to_sort)):
        # the current number at the index represents the value that's currently being sorted
        current_num = list_to_sort[i]
        # move the current number back through the array (to the sorted side)
        j = i
        #     keep moving until: it's greater than the number before it OR we reach the start of the array
        while j > 0 and current_num < list_to_sort[j-1]:
            # swap the current value and the one to the left of it
            list_to_sort[j] = list_to_sort[j-1]
            j -= 1
        # set the value at the current index to the current number
        # at this moment, j represents the new location for the current number
        list_to_sort[j] = current_num
    return list_to_sort

print(insertion_sort([8, 2, 4, 5, 1, 3]))