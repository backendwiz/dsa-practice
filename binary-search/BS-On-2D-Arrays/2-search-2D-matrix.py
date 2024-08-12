def solve(arr, target):

    rows = len(arr)
    cols = len(arr[0])

    i = 0
    j = cols - 1

    while i >= 0 and i < rows and j >= 0 and j < cols:

        if arr[i][j] == target:
            return True

        elif arr[i][j] > target:
            j -= 1
        else:
            i += 1
    return False


if __name__ == "__main__":
    arr = [[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]]
    target = 4
    print(solve(arr, target))

# Time Complexity = O(m+n)
# Space Complexity = O(1)
