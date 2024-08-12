def findPeakGrid(mat):

    ans = [-1, -1]
    n = len(mat)
    m = len(mat[0])
    low = 0
    high = m - 1

    while low <= high:
        mid = (low + high) // 2
        row = maxEl(mat, mid, n)
        left = mat[row][mid - 1] if mid - 1 >= 0 else -1
        right = mat[row][mid + 1] if mid + 1 < m else -1

        if mat[row][mid] > left and mat[row][mid] > right:
            return [row, mid]
        elif mat[row][mid] < left:
            high = mid - 1
        else:
            low = mid + 1
    return [-1, -1]


def maxEl(mat, mid, n):
    maxValue = -1
    index = -1

    for i in range(n):
        if mat[i][mid] > maxValue:
            maxValue = mat[i][mid]
            index = i
    return index


if __name__ == "__main__":
    arr = [[1, 4], [3, 2]]
    print(findPeakGrid(arr))

# Time Complexity = O(logn)
# Space Complexity = O(1)
