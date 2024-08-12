def check(nums):
    n = len(nums)
    count = 0
    for i in range(n):
        if nums[i] < nums[i - 1]:
            count += 1
    return count <= 1


if __name__ == "__main__":
    nums = [6, 1, 2, 3, 4, 5]
    ans = check(nums)
    if ans:
        print("True")
    else:
        print("False")

# Time Complexity: O(n)
# Space Complexity:  O(1)
