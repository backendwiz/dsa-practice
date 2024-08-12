def solve(arr, target):

    start, end = 0, 1
    while target > arr[end]:
        start = end
        end = 2 * end

        for i in range(len(arr)):
            mid = start + end // 2

            if arr[mid] < target:
                start = mid + 1
            elif arr[mid] > target:
                end = mid - 1
            else:
                return mid
    return -1


if __name__ == "__main__":
    arr = [3, 5, 7, 9, 10, 90, 100, 130, 140, 160, 170]
    target = 10
    print(solve(arr, target))

# Time Complexity = O(logn)
# Space Complexity = O(1)
