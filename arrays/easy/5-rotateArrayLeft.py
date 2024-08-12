def solve(arr):
    n = len(arr)
    temp = arr[0]

    for i in range(n - 1):
        arr[i] = arr[i + 1]

    arr[n - 1] = temp
    return arr


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    ans = solve(arr)
    print(*ans)

# Time Complexity = O(n)
# Space Complexity = O(1)
