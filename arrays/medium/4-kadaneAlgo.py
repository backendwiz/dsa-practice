import sys


def solve(arr):

    # currSum = 0
    # maxSum = arr[0]
    # for i in arr:
    #     currSum = max(currSum, 0)
    #     currSum = currSum + i
    #     maxSum = max(currSum, maxSum)
    # return maxSum

    n = len(arr)
    maxNum = -sys.maxsize - 1
    maxSum = 0
    for i in range(n):
        maxSum = maxSum + arr[i]
        if maxSum > maxNum:
            maxNum = maxSum

        if maxSum < 0:
            maxSum = 0
    return maxNum


if __name__ == "__main__":
    # arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    arr = [5, 4, -1, 7, 8]
    print(solve(arr))

# Time Complexity = O(N)
# Space Complexity = O(1)
