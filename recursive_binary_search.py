def binary_search(item, array, lower=0, upper=None):
    upper = upper if upper else len(array)
    mid = (lower + upper)/2

    if upper < lower or 0 < mid >= len(array):
        return -1
    elif item == array[mid]:
        return mid
    else:
        if item < array[mid]:
            upper = mid - 1
        else:
            lower = mid + 1

        return binary_search(item, array, lower, upper)


arr = list(range(1, 101))
arr.pop(50)
print binary_search(12, arr) == 11
print binary_search(99, arr) == 97
print binary_search(6, arr) == 5
print binary_search(100, arr) == 98
print binary_search(101, arr) == -1
print binary_search(51, arr) == -1
print binary_search(1, arr) == 0