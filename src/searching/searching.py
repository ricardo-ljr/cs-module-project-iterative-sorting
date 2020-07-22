def linear_search(arr, target):
    # Your code here
    for i in range(len(arr)):

        if arr[i] == target:
            return i

    return -1   # not found


# Write an iterative implementation of Binary Search
def binary_search(arr, target):

    # Your code here
    a, b = 0, len(arr)-1
    while a <= b:
        mid = a + (b - a) // 2
        mid_value = arr[mid]
        if mid_value == target:
            return mid
        elif mid_value < target:
            a = mid + 1
        else:
            b = mid - 1
    return -1  # not found
