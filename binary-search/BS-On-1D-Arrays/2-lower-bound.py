def solve(arr, target):

    left, right = 0, len(arr) - 1
    ans = len(arr)

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] >= target:
            ans = mid
            right = mid - 1
        else:
            left = mid + 1

    return ans


if __name__ == "__main__":
    arr = [1, 2, 8, 10, 11, 12, 19]
    target = 9
    print(solve(arr, target))

# Time Complexity = O(logn)
# Space Complexity = O(1)
