def binary_search(item, array):
    upper, lower = len(array), 0

    while upper >= lower:
        mid = (upper + lower)/2
        try:
            if item == array[mid]:
                return mid
        except IndexError:
            break

        if item < array[mid]:
            upper = mid - 1
        else:
            lower = mid + 1


    return -1

arr = list(range(1, 101))
arr.pop(50)
print binary_search(12, arr) == 11
print binary_search(99, arr) == 97
print binary_search(6, arr) == 5
print binary_search(100, arr) == 98
print binary_search(101, arr) == -1
print binary_search(51, arr) == -1
print binary_search(1, arr) == 0