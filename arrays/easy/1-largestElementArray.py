def largestElementArray(arr):
    max = arr[0]
    for i in range(0, len(arr)):
        if max < arr[i]:
            max = arr[i]
    return max


if __name__ == "__main__":
    arr = [1, 2, 3, 45]
    print(largestElementArray(arr))

# Time Complexity: O(n)
# Space Complexity:  O(1)
