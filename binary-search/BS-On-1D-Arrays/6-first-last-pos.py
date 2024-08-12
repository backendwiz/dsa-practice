def solve(arr, target):

    first = first_occurence(arr, target)
    last = last_occurence(arr, target)
    return [first, last]


def first_occurence(arr, target):
    left = 0
    right = len(arr) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid
            right = mid - 1  # Continue searching to the left
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result


def last_occurence(arr, target):
    left = 0
    right = len(arr) - 1
    result = -1

    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            result = mid
            left = mid + 1  # Continue searching to the right
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return result


if __name__ == "__main__":
    arr = nums = [5, 7, 7, 7, 8, 8, 10]
    target = 7
    print(solve(arr, target))

# Time Complexity = O(logN)
# Space Complexity = O(1)
