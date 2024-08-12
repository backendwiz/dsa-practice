def nCr(row):
    res = 1
    resRow = [1]

    for col in range(1, row):
        res = res * (row - col)
        res = res // col
        resRow.append(res)
    return resRow


def solve(arr):
    ans = []

    for row in range(1, arr + 1):
        ans.append(nCr(row))
    return ans


if __name__ == "__main__":
    n = 5
    ans = solve(n)
    for it in ans:
        for ele in it:
            print(ele, end=" ")
        print()

# Time Complexity = O(n2)
# Space Complexity = O(1)
