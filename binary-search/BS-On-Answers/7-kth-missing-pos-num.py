def solve(arr, k):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2
        missing = arr[mid] - (mid + 1)
        if missing < k:
            low = mid + 1
        else:
            high = mid - 1
    return k + high + 1


if __name__ == "__main__":
    arr = [2, 3, 4, 7, 11]
    target = 5
    print(solve(arr, target))

# Time Complexity = O(logn)
# Space Complexity = O(1)
