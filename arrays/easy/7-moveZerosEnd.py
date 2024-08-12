def moveZeros(nums):
    nonZero = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[nonZero], nums[i] = nums[i], nums[nonZero]
            nonZero += 1
    return nums


if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]
    ans = moveZeros(nums)
    print(ans)

# Time Complexity = O(n)
# Space Complexity = O(1)
