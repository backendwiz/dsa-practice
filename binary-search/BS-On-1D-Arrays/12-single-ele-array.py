def solve(nums):
    start, end = 0, len(nums) - 1
    while start <= end:
        mid = start + (end - start) // 2

        # we are in left
        if (mid % 2 == 0 and nums[mid] == nums[mid + 1]) or (
            mid % 2 == 1 and nums[mid] == nums[mid - 1]
        ):
            start = mid + 1
        else:
            end = mid - 1

    return nums[start]


if __name__ == "__main__":
    arr = [1, 1, 2, 3, 3, 4, 4, 8, 8]
    print(solve(arr))

# Time Complexity = O(logn)
# Space Complexity = O(1)
