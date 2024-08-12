def solve(arr, target):
    ## count occurences use first and last occurence code

    left = first_occurence(arr, target)
    right = last_occurence(arr, target)

    return right - left + 1


def first_occurence(arr, target):
    left = 0
    right = len(arr) - 1
    res = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            res = mid
            right = mid - 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return res


def last_occurence(arr, target):
    left = 0
    right = len(arr) - 1
    res = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            res = mid
            left = mid + 1
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return res


if __name__ == "__main__":
    arr = [1, 1, 2, 2, 2, 2, 3]
    target = 2
    print(solve(arr, target))

# Time Complexity = O(logn)
# Space Complexity = O(1)
