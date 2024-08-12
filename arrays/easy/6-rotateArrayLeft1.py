def solve(nums, k):
    # reverse(nums, 0, k - 1)
    # reverse(nums, k, len(nums) - 1)
    # reverse(nums, 0, len(nums) - 1)

    k = k % len(nums)

    l, r = 0, k - 1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l, r = l + 1, r - 1

    l, r = k, len(nums) - 1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l, r = l + 1, r - 1

    l, r = 0, len(nums) - 1
    while l < r:
        nums[l], nums[r] = nums[r], nums[l]
        l, r = l + 1, r - 1


# def reverse(nums, l, r):
#     while l < r:
#         nums[l], nums[r] = nums[r], nums[l]
#         l += 1
#         r -= 1


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    solve(arr, 2)
    print(arr)

# Time Complexity = O(n)
# Space Complexity = O(n)
