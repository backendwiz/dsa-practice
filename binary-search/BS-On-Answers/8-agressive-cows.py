def solve(stalls, m):
    n = len(stalls)
    stalls.sort()

    low = 1
    high = stalls[n - 1] - stalls[0]
    while low <= high:
        mid = (low + high) // 2
        if cowPlace(stalls, mid, m):
            low = mid + 1
        else:
            high = mid - 1
    return high


def cowPlace(stalls, dist, cows):
    n = len(stalls)
    cnt = 1
    lastCows = stalls[0]
    for i in range(1, n):
        if stalls[i] - lastCows >= dist:
            cnt += 1
            lastCows = stalls[i]
        if cnt >= cows:
            return True
    return False


if __name__ == "__main__":
    arr = [0, 3, 4, 7, 10, 9]
    target = 4
    print(solve(arr, target))

# Time Complexity = O(logn)
# Space Complexity = O(1)
