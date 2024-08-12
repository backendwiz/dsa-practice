def solve(arr):

    n = len(arr)
    arr.sort()
    ans = []

    for i in range(n):
        # if the current interval does not
        # lie in the last interval:
        if not ans or arr[i][0] > ans[-1][1]:
            ans.append(arr[i])
        # if the current interval
        # lies in the last interval:
        else:
            ans[-1][1] = max(ans[-1][1], arr[i][1])
    return ans


if __name__ == "__main__":
    arr = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print(solve(arr))

# Time Complexity = O(n)
# Space Complexity = O(n)
