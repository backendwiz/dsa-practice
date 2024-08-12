def binary_search(arr, low, high, key, is_asc=True):
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        if (arr[mid] > key) == is_asc:
            high = mid - 1
        else:
            low = mid + 1
    return -1


def find_bitonic_point(arr, low, high):
    while low <= high:
        mid = (low + high) // 2
        if mid > 0 and mid < len(arr) - 1:
            if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
                return mid
            elif arr[mid] < arr[mid + 1]:
                low = mid + 1
            else:
                high = mid - 1
        elif mid == 0:
            return 1 if arr[0] < arr[1] else 0
        else:
            return len(arr) - 2 if arr[-1] < arr[-2] else len(arr) - 1
    return -1


def search_bitonic(arr, key):
    n = len(arr)
    bitonic_point = find_bitonic_point(arr, 0, n - 1)
    if key > arr[bitonic_point]:
        return -1
    if key == arr[bitonic_point]:
        return bitonic_point
    index = binary_search(arr, 0, bitonic_point - 1, key, True)
    if index != -1:
        return index
    return binary_search(arr, bitonic_point + 1, n - 1, key, False)


def main():
    arr = [-8, 1, 2, 3, 4, 5, -2, -3]
    key = 4
    index = search_bitonic(arr, key)
    if index == -1:
        print("Element Not Found")
    else:
        print("Element Found at index", index)


main()
