def solve(arr):

    n = len(arr)
    ans = [0] * n

    posIndex, negIndex = 0, 1

    for i in range(n):

        if arr[i] < 0:
            ans[negIndex] = arr[i]
            negIndex += 2
        else:
            ans[posIndex] = arr[i]
            posIndex += 2
    return ans


if __name__ == "__main__":
    arr = [3, 1, -2, -5, 2, -4]
    print(solve(arr))

# Time Complexity = O(n)
# Space Complexity = O(n)
