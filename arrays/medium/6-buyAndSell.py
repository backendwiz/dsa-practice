def solve(arr):
    maxProfit = 0
    minPrice = float("inf")
    for i in range(len(arr)):
        minPrice = min(minPrice, arr[i])
        maxProfit = max(maxProfit, arr[i] - minPrice)
    return maxProfit


if __name__ == "__main__":
    arr = [7, 1, 5, 3, 6, 4]
    print(solve(arr))

# Time Complexity = O(n)
# Space Complexity = O(1)


"""
2. Iteration through arr:
    Day 1: Price = 7
    minPrice becomes 7 (minimum of infinity and 7).
    maxProfit remains 0 (maximum of 0 and 7-7).
    Day 2: Price = 1
    minPrice becomes 1 (minimum of 7 and 1).
    maxProfit remains 0 (maximum of 0 and 1-1).
    Day 3: Price = 5
    minPrice remains 1.
    maxProfit becomes 4 (maximum of 0 and 5-1).
    Day 4: Price = 3
    minPrice remains 1.
    maxProfit remains 4 (maximum of 4 and 3-1).
    Day 5: Price = 6
    minPrice remains 1.
    maxProfit becomes 5 (maximum of 4 and 6-1).
    Day 6: Price = 4
    minPrice remains 1.
    maxProfit remains 5 (maximum of 5 and 4-1).
"""
