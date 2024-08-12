def solve(arr):
    """
    Dutch Nation flag problem
    """
    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1
    return arr


if __name__ == "__main__":
    arr = [2, 0, 2, 1, 1, 0, 0]
    print(solve(arr))

# Time Complexity = O(n)
# Space Complexity = O(1)
