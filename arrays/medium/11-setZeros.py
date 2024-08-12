def solve(arr):
    m = len(arr)  # row
    n = len(arr[0])  # col
    cols = 1

    for i in range(m):
        for j in range(n):

            if arr[i][j] == 0:

                # mark i-th row:
                arr[i][0] = 0

                if j != 0:

                    # mark j-th column:
                    arr[0][j] = 0
                else:
                    cols = 0

    for i in range(1, m):
        for j in range(1, n):
            if arr[i][0] == 0 or arr[0][j] == 0:
                arr[i][j] = 0

    if arr[0][0] == 0:
        for j in range(n):
            arr[0][j] = 0
    if cols == 0:
        for i in range(m):
            arr[i][0] = 0
    return arr


if __name__ == "__main__":
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    print(solve(matrix))

# Time Complexity =
# Space Complexity =
