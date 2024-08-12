def solve(arr, target):

    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif target > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1
    return -1


if __name__ == "__main__":
    arr = [-1, 0, 3, 5, 9, 12]
    target = 9
    print(solve(arr, target))

# Time Complexity = O(logn)
# Space Complexity = O(1)
