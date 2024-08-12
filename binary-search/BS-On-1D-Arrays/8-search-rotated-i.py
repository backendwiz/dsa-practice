def solve(arr, target):

    # minEleIndex = arrayRotated(arr)
    # leftMinIndex = binarySearch(arr, 0, minEleIndex - 1, target)
    # rightMinIndex = binarySearch(arr, minEleIndex, len(arr), target)

    # return leftMinIndex if leftMinIndex != -1 else rightMinIndex

    start, end = 0, len(arr) - 1

    while start <= end:
        mid = start + (end - start) // 2
        print(arr[mid])
        if arr[mid] == target:
            return mid

        if arr[start] <= arr[mid]:
            if target > arr[mid] or target < arr[start]:
                start = mid + 1
            else:
                end = mid - 1

        else:
            if target < arr[mid] or target > arr[end]:
                end = mid - 1
            else:
                start = mid + 1
    return -1


# def arrayRotated(arr):
#     left, right = 0, len(arr) - 1
#     n = len(arr)
#     while left <= right:
#         mid = left + (right - left) // 2

#         prev = (mid - 1 + n) % n
#         nxt = (mid + 1) % n

#         if arr[mid] <= arr[prev] and arr[mid] <= arr[nxt]:
#             return mid
#         elif arr[left] <= arr[right]:
#             return left
#         elif arr[left] <= arr[mid]:
#             left = mid + 1
#         elif arr[mid] <= arr[right]:
#             right = mid - 1


# def binarySearch(arr, left, right, target):

#     while left <= right:
#         mid = (left + right) // 2

#         if arr[mid] == target:
#             return mid
#         elif target > arr[mid]:
#             left = mid + 1
#         else:
#             right = mid - 1
#     return -1


if __name__ == "__main__":
    arr = [4, 5, 6, 7, 0, 1, 2]
    target = 9
    print(solve(arr, target))

# Time Complexity = O(logn)
# Space Complexity = O(1)
