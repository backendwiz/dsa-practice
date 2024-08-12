def solve(arr, target):

    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return arr[mid]

        elif target > arr[mid]:
            left = mid + 1
        else:
            right = mid - 1

    if (abs(arr[left] - target)) < abs(arr[right] - target):
        return arr[left]
    return arr[right]


if __name__ == "__main__":
    arr = [2, 5, 10, 12, 15]
    target = 6
    print(solve(arr, target))

# Time Complexity = O(logn)
# Space Complexity = O(1)
