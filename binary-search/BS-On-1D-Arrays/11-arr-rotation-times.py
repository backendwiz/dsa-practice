def solve(arr):
    left, right = 0, len(arr) - 1
    n = len(arr)
    while left <= right:
        mid = left + (right - left) // 2

        prev = (mid - 1 + n) % n
        nxt = (mid + 1) % n

        if arr[mid] <= arr[prev] and arr[mid] <= arr[nxt]:
            return mid
        elif arr[left] <= arr[right]:
            return left
        elif arr[left] <= arr[mid]:
            left = mid + 1
        elif arr[mid] <= arr[right]:
            right = mid - 1
        else:
            return -1


if __name__ == "__main__":
    arr = [4, 5, 6, 7, 0, 1, 2, 3]
    print(solve(arr))

# Time Complexity = O(logn)
# Space Complexity = O(1)

# answer also called as minimum rotation array
