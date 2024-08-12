def solve(arr, target):

    floor, ceil = -1, -1
    left, right = 0, len(arr) - 1

    # while left <= right:
    #     mid = (left + right) // 2

    #     if arr[mid] <= target:
    #         floor = arr[mid]
    #         left = mid + 1
    #     else:
    #         right = mid - 1

    # left, right = 0, len(arr) - 1

    # while left <= right:
    #     mid = (left + right) // 2

    #     if arr[mid] >= target:
    #         ceil = arr[mid]
    #         right = mid - 1
    #     else:
    #         left = mid + 1

    # return [floor, ceil]

    while left <= right:
        mid = left + (right - left) // 2

        if arr[mid] < target:
            floor = arr[mid]
            left = mid + 1
        elif arr[mid] > target:
            ceil = arr[mid]
            right = mid - 1
        else:
            float = ceil = arr[mid]
            break

    return [floor, ceil]


if __name__ == "__main__":
    arr = [3, 4, 4, 7, 8, 10]
    target = 5
    print(solve(arr, target))

# Time Complexity = O(logn)
# Space Complexity = O(1)
