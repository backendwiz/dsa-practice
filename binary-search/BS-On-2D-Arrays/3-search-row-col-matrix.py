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
    arr = [
        [1, 4, 7, 11, 15],
        [2, 5, 8, 12, 19],
        [3, 6, 9, 16, 22],
        [10, 13, 14, 17, 24],
        [18, 21, 23, 26, 30],
    ]
    target = 5
    print(solve(arr, target))

# Time Complexity = O(m+n)
# Space Complexity = O(1)
