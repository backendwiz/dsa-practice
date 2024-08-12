def solve(x):
    l, r = 0, x
    while l <= r:
        mid = (l + r) // 2
        if mid * mid == x:
            return mid
        if mid * mid < x:
            l = mid + 1
        else:
            r = mid - 1
    return r


if __name__ == "__main__":
    arr = 6
    print(solve(arr))

# Time Complexity =
# Space Complexity =
