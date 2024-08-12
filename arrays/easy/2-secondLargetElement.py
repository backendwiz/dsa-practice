def getElements(arr):
    n = len(arr)
    if n < 2:
        return -1, -1

    small = float("inf")
    second_small = float("inf")

    largest = float("-inf")
    second_large = float("-inf")

    for i in range(n):
        if arr[i] < small:
            second_small = small
            small = arr[i]
        elif arr[i] < second_small and arr[i] != small:
            second_small = arr[i]

        if arr[i] > largest:
            second_large = largest
            largest = arr[i]
        elif arr[i] > second_large and arr[i] != largest:
            second_large = arr[i]

    return second_small, second_large


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5, 6, 7]
    print(*getElements(arr))

# Time Complexity: O(n)
# Space Complexity:  O(1)
