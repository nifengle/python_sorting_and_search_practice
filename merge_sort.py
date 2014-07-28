def merge_sort(array):
    if len(array) <= 1:
        return array

    mid = len(array)/2
    left, right = array[:mid], array[mid:]

    left = merge_sort(left)
    right = merge_sort(right)

    return merge(left, right)

def merge(left, right):
    result = []

    while len(left) > 0 or len(right) > 0:
        try:
            if left[0] <= right[0]:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))
        except IndexError:
            if len(left) > 0:
                result.append(left.pop(0))
            else:
                result.append(right.pop(0))

    return result