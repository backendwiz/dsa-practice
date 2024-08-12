def solve(arr):

    count = 0
    maxCount = 0

    for i in range(len(arr)):
        if arr[i] == 1:
            count += 1
        else:
            count = 0
        maxCount = max(maxCount, count)
    return maxCount


if __name__ == "__main__":
    arr = [1, 0, 1, 1, 1]
    print(solve(arr))

# Time Complexity = O(n)
# Space Complexity = O(1)
