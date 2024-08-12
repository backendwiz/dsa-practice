def solve(arr, k):

    n = len(arr)
    low, high = max(arr), sum(arr)

    while low <= high:
        mid = (low + high) // 2
        partitions = countPartitions(arr, mid)
        if partitions > k:
            low = mid + 1
        else:
            high = mid - 1
    return low


def countPartitions(arr, maxSum):
    n = len(arr)
    partitions = 1
    subArraySum = 0

    for i in range(n):
        if subArraySum + arr[i] <= maxSum:
            subArraySum += arr[i]
        else:
            partitions += 1
            subArraySum = arr[i]
    return partitions


if __name__ == "__main__":
    arr = [10, 20, 30, 40]
    target = 2
    print(solve(arr, target))

"""
Time Complexity: O(N * log(sum(arr[])-max(arr[])+1)), where N = size of the array, sum(arr[]) = sum of all array elements, max(arr[]) = maximum of all array elements.
Reason: We are applying binary search on [max(arr[]), sum(arr[])]. Inside the loop, we are calling the countStudents() function for the value of ‘mid’. Now, inside the countStudents() function, we are using a loop that runs for N times.

Space Complexity:  O(1) as we are not using any extra space to solve this problem.
"""
