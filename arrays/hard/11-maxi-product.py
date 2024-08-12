def solve(arr):

    prod1 = arr[0]
    prod2 = arr[0]
    res = arr[0]

    for i in range(1, len(arr)):
        temp = max(arr[i], prod1 * arr[i], prod2 * arr[i])
        # print(temp)
        prod2 = min(arr[i], prod1 * arr[i], prod2 * arr[i])
        prod1 = temp
        res = max(res, prod1)
    return res


if __name__ == "__main__":
    arr = [2, 3, -2, 4]
    # output = 6
    print(solve(arr))

# Time Complexity =
# Space Complexity =
