import math


def solve(arr, threshold):

    n = len(arr)

    if n > threshold:
        return -1
    low, high = 1, max(arr)
    ans = -1

    while low <= high:
        mid = (low + high) // 2
        if sumByD(arr, mid) <= threshold:
            ans = mid
            high = mid - 1
        else:
            low = mid + 1
    return ans


def sumByD(arr, div):
    n = len(arr)
    total_sum = 0
    for i in range(n):
        total_sum += math.ceil(arr[i] / div)
    return total_sum


if __name__ == "__main__":
    nums = (1, 2, 5, 9)
    threshold = 6
    print(solve(nums, threshold))

# Time Complexity = O(logn)
# Space Complexity = O(1)
