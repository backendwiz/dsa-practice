def solve(arr, k):

    n = len(arr)
    maxLen = 0
    hashMap = {}
    maxSum = 0

    for i in range(n):
        maxSum += arr[i]

        if maxSum == k:
            maxLen = max(maxLen, i + 1)

        rem = maxSum - k
        print(hashMap)

        if rem in hashMap:
            length = i - hashMap[rem]
            # print(length)
            maxLen = max(maxLen, length)

        if maxSum not in hashMap:
            hashMap[maxSum] = i
    return maxLen


if __name__ == "__main__":
    arr = [2, 3, 5, 1, 9]
    k = 10
    print(solve(arr, k))

# Time Complexity = O(2*n) = O(n)
# Space Complexity = O(n)
