def bubble_sort(array):
    if len(array) <= 1:
        return array

    while True:
        swapped = False
        i = 0
        while i < len(array) - 1:
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
                swapped = True
            i += 1
        if not swapped:
            break
    return array