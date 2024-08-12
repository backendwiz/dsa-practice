def solve(weights, days):

    low, high = max(weights), sum(weights)

    while low <= high:
        mid = (low + high) // 2
        numDays = findDays(weights, mid)
        if numDays <= days:
            high = mid - 1
        else:
            low = mid + 1
    return low


def findDays(weights, cap):
    days = 1
    load = 0

    n = len(weights)
    for i in range(n):
        if load + weights[i] > cap:
            days += 1
            load = weights[i]
        else:
            load += weights[i]
    return days


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    target = 5
    print(solve(arr, target))

    """
    

Time Complexity: O(N * log(sum(weights[]) - max(weights[]) + 1)), where sum(weights[]) = summation of all the weights, max(weights[]) = maximum of all the weights, N = size of the weights array.
Reason: We are applying binary search on the range [max(weights[]), sum(weights[])]. For every possible answer ‘mid’, we are calling findDays() function. Now, inside the findDays() function, we are using a loop that runs for N times.

Space Complexity: O(1) as we are not using any extra space to solve this problem.
    """
