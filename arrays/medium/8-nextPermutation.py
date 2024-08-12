def solve(arr):
    n = len(arr)

    # Step 1: Find the break point:
    ind = -1
    for i in range(
        n - 2, -1, -1
    ):  # start loop from second to last ele to first in reverse order
        if arr[i] < arr[i + 1]:
            ind = i
            break

    if ind == -1:
        arr.reverse()
        return arr
    # Step 2: Find the next greater element
    #         and swap it with arr[ind]:
    for i in range(n - 1, ind, -1):
        if arr[i] > arr[ind]:
            arr[i], arr[ind] = arr[ind], arr[i]
            break

    # reverse remaining array
    arr[ind + 1 :] = reversed(arr[ind + 1 :])
    return arr


if __name__ == "__main__":
    arr = [1, 2, 3]
    print(solve(arr))

# Time Complexity = O(3N)
# Space Complexity = O(1)
