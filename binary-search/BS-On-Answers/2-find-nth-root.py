def solve(n, m):
    low, high = 1, m

    while low <= high:
        mid = (low + high) // 2
        midN = func(mid, n, m)
        if midN == 1:
            return mid
        elif midN == 0:
            low = mid + 1
        else:
            high = mid - 1
    return -1


def func(mid, n, m):

    ans = 1
    for i in range(1, n + 1):
        ans = ans * mid
        if ans > m:
            return 2
    if ans == m:
        return 1
    return 0


if __name__ == "__main__":
    n = 3
    m = 27
    print(solve(n, m))

# Time Complexity = O(logn)
# Space Complexity = O(1)
