def solve(arr):

    res = len(arr)

    # for i in range(len(arr)):
    #     res = res + i - arr[i]
    # return res

    for i, num in enumerate(arr):
        res = res + i - num
    return res


if __name__ == "__main__":
    arr = [1, 0, 3]
    print(solve(arr))

# Time Complexity = O(n)
# Space Complexity = O(1)
