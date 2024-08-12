def solve(arr, k):

    n = len(arr)
    l, r = 0, 0
    total = arr[0]
    maxLen = 0

    while r < n:
        while l <= r and total > k:
            total -= arr[l]
            l += 1

        if total == k:
            maxLen = max(maxLen, r - l + 1)
        r += 1
        if r < n:
            total += arr[r]
    return maxLen


if __name__ == "__main__":
    arr = [2, 3, 5, 1, 9]
    k = 10
    print(solve(arr, k))

# Time Complexity = O(2*n) = O(n)
# Space Complexity = O(1)
