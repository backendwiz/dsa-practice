import sys


def solve(arr):

    if not arr:
        return []

    maxSum = currSum = arr[0]
    start = end = s = 0

    for i in range(1, len(arr)):
        if arr[i] > currSum + arr[i]:
            currSum = arr[i]
            s = i
        else:
            currSum = currSum + arr[i]

        if currSum > maxSum:
            maxSum = currSum
            start = s
            end = i
    return arr[start : end + 1]

    # n = len(arr)
    # maxNum = -sys.maxsize - 1
    # currSum = 0
    # start = 0
    # ansStart = -1
    # ansEnd = -1

    # for i in range(n):
    #     if currSum == 0:
    #         start = i

    #     currSum = currSum + arr[i]
    #     if currSum > maxNum:
    #         maxNum = currSum
    #         ansStart = start
    #         ansEnd = i

    #     if currSum < 0:
    #         currSum = 0
    # return arr[ansStart : ansEnd + 1]


if __name__ == "__main__":
    arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    print(solve(arr))

# Time Complexity = O(N)
# Space Complexity = O(1)
