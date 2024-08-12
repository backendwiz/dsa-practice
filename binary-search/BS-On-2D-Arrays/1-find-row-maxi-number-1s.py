def solve(arr):

    n = len(arr)
    m = len(arr[0])

    max_row_index = -1
    j = m - 1  # Start from the last column

    # Iterate over each row
    for i in range(n):
        # Move left while the current cell is 1
        while j >= 0 and arr[i][j] == 1:
            j -= 1
            max_row_index = i  # Update the row index with the maximum 1s

    return max_row_index


if __name__ == "__main__":
    arr = [[0, 1, 1, 1], [0, 0, 1, 1], [1, 1, 1, 1], [0, 0, 0, 0]]
    print(solve(arr))

# Time Complexity = O(m+n)
# Space Complexity = O(1)
