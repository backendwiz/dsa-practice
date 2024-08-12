def solve(arr):

    n = len(arr)
    cnt = 0
    element = None

    for i in range(n):
        if cnt == 0:
            cnt = 1
            element = arr[i]
            print(element)
        elif element == arr[i]:
            cnt += 1
        else:
            cnt -= 1

    cnt1 = 0
    for i in range(n):
        if arr[i] == element:
            cnt1 += 1
    if cnt1 > n / 2:
        return element
    return -1


if __name__ == "__main__":
    arr = [2, 2, 1, 1, 1, 2, 2]
    print(solve(arr))

# Time Complexity =
# Space Complexity =
