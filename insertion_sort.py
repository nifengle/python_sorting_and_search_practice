def insertion_sort(array):
    if len(array) <= 1:
        return array

    i = 1
    while i < len(array):
        current_item = array[i]
        j = i

        while j > 0 and array[j-1] > current_item:
            array[j] = array[j-1]
            j -= 1

        array[j] = current_item
        i += 1

    return array