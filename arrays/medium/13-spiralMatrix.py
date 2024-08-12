def solve(matrix):
    ans = []
    m = len(matrix)  # rows
    n = len(matrix[0])  # cols

    top = 0
    left = 0
    bottom = m - 1
    right = n - 1

    while top <= bottom and left <= right:
        # top row i.e 1 2 3
        for i in range(left, right + 1):
            ans.append(matrix[top][i])
        top += 1

        for i in range(top, bottom + 1):
            ans.append(matrix[i][right])
        right -= 1

        if top <= bottom:
            for i in range(right, left - 1, -1):
                ans.append(matrix[bottom][i])
            bottom -= 1

        if left <= right:
            for i in range(bottom, top - 1, -1):
                ans.append(matrix[i][left])

            left += 1

    return ans


if __name__ == "__main__":
    arr = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print(solve(arr))

# Time Complexity =
# Space Complexity =
