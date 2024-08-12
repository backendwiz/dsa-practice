def search(arr, target):

    start, end = 0, len(arr) - 1

    while start <= end:
        mid = start + (end - start) // 2

        if arr[mid] == target:
            return True

        if arr[start] == arr[mid] and arr[mid] == arr[end]:
            start += 1
            end -= 1
            continue

        if arr[start] <= arr[mid]:
            if target > arr[mid] or target < arr[start]:
                start = mid + 1
            else:
                end = mid - 1

        else:
            if target < arr[mid] or target > arr[end]:
                end = mid - 1
            else:
                start = mid + 1
    return False


if __name__ == "__main__":
    nums = [1, 0, 1, 1, 1]
    target = 0
    print(search(nums, target))
