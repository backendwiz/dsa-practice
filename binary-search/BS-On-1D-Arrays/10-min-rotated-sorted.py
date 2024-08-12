def solve(arr):

    start, end = 0, len(arr) - 1
    ans = float("inf")

    while start <= end:
        mid = start + (end - start) // 2

        if arr[start] <= arr[mid]:
            ans = min(ans, arr[start])
            start = mid + 1
        else:
            ans = min(ans, arr[mid])
            end = mid - 1
    return ans


if __name__ == "__main__":
    arr = [3, 1, 2]
    print(solve(arr))


## flow even odd and odd even

# Time Complexity = O(logn)
# Space Complexity = O(1)
