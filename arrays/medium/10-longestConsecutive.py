def solve(arr):
    num_set = set(arr)
    longest = 0

    for num in num_set:
        if num - 1 not in num_set:
            curr_num = num
            curr_streak = 1

            while curr_num + 1 in num_set:
                curr_num += 1
                curr_streak += 1
            longest = max(longest, curr_streak)
    return longest


if __name__ == "__main__":
    arr = [100, 200, 1, 3, 2, 4]

    print(solve(arr))

# Time Complexity = O(n) O(3 * n)
# Space Complexity = O(n)
