def solve(arr):

    freq = {}

    for i in arr:
        freq[i] = freq.get(i, 0) + 1

    for i, num in freq.items():
        if num == 1:
            return i


if __name__ == "__main__":
    arr = [2, 2, 1]
    print(solve(arr))

# Time Complexity = O(n)
# Space Complexity = O(1)
