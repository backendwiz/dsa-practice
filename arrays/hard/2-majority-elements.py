def solve(nums):

    if not nums:
        return []

    candidate1, candidate2, count1, count2 = None, None, 0, 0

    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1
        elif count1 == 0:
            candidate1, count1 = num, 1
        elif count2 == 0:
            candidate2, count2 = num, 1
        else:
            count1 -= 1
            count2 -= 1

    count1, count2 = 0, 0

    for num in nums:
        if num == candidate1:
            count1 += 1
        elif num == candidate2:
            count2 += 1
    res = []

    if count1 > len(nums) // 3:
        res.append(candidate1)

    if count2 > len(nums) // 3:
        res.append(candidate2)

    return res


if __name__ == "__main__":
    arr = [1, 2, 2, 3, 2, 1]
    print(solve(arr))

# Time Complexity =
# Space Complexity =
