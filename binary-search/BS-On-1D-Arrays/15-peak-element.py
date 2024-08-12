def solve(arr):
    n = len(arr)

    if n == 1:
        return 0
    if arr[0] > arr[1]:
        return 0

    if arr[n - 1] > arr[n - 2]:
        return n - 1

    left, right = 1, n - 2

    while left <= right:

        mid = left + (right - left) // 2

        if arr[mid] > arr[mid - 1] and arr[mid] > arr[mid + 1]:
            return mid

        if arr[mid] > arr[mid - 1]:
            left = mid + 1
        else:
            right = mid - 1
    return -1


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 5, 1]
    print(solve(arr))

# Time Complexity = O(logn)
# Space Complexity = O(1)
