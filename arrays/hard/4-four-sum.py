def solve(arr, target):
    n = len(nums)
    ans = []

    nums.sort()

    for i in range(n):
        if i > 0 and nums[i] == nums[i - 1]:
            continue

        for j in range(i + 1, n):
            if j > i + 1 and nums[j] == nums[j - 1]:
                continue

            k = j + 1
            l = n - 1

            while k < l:
                total_sum = nums[i] + nums[j] + nums[k] + nums[l]
                if total_sum == target:
                    temp = [nums[i], nums[j], nums[k], nums[l]]
                    ans.append(temp)
                    k += 1
                    l -= 1
                    while k < l and nums[k] == nums[k - 1]:
                        k += 1
                    while k < l and nums[l] == nums[l + 1]:
                        l -= 1
                elif total_sum < target:
                    k += 1
                else:
                    l -= 1
    return ans


if __name__ == "__main__":
    nums = [1, 0, -1, 0, -2, 2]
    target = 0
    print(solve(nums, target))

# Time Complexity =
# Space Complexity =
