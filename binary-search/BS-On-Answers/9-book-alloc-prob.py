def solve(arr, m):

    n = len(arr)
    if m > n:
        return -1

    low, high = max(arr), sum(arr)

    while low <= high:
        mid = (low + high) // 2
        students = countStudents(arr, mid)
        if students > m:
            low = mid + 1
        else:
            high = mid - 1
    return low


def countStudents(arr, pages):
    n = len(arr)
    students = 1
    pagesStudents = 0
    for i in range(n):
        if pagesStudents + arr[i] <= pages:
            pagesStudents += arr[i]
        else:
            students += 1
            pagesStudents = arr[i]
    return students


if __name__ == "__main__":
    arr = [25, 46, 28, 49, 24]
    target = 4
    print(solve(arr, target))

"""
Time Complexity: O(N * log(sum(arr[])-max(arr[])+1)), where N = size of the array, sum(arr[]) = sum of all array elements, max(arr[]) = maximum of all array elements.
Reason: We are applying binary search on [max(arr[]), sum(arr[])]. Inside the loop, we are calling the countStudents() function for the value of ‘mid’. Now, inside the countStudents() function, we are using a loop that runs for N times.

Space Complexity:  O(1) as we are not using any extra space to solve this problem.
"""
