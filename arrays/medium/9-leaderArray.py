def solve(arr):
    n = len(arr)
    ans = []

    max_element = arr[n - 1]
    ans.append(arr[n - 1])

    for i in range(n - 2, -1, -1):
        if arr[i] > max_element:
            ans.append(arr[i])
            max_element = arr[i]
    return ans


if __name__ == "__main__":
    arr = [4, 7, 1, 0]
    print(solve(arr))

# Time Complexity = O(n)
# Space Complexity = O(n)
