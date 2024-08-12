def solve(arr):
    n = len(arr)
    hashMap = [0] * (n + 1)

    # update hashMap
    for i in range(n):
        hashMap[arr[i]] += 1
    print(hashMap)

    # find numbers
    repeating, missing = -1, -1
    for i in range(1, n + 1):
        if hashMap[i] == 2:
            repeating = i
        elif hashMap[i] == 0:
            missing = i

        if repeating != -1 and missing != -1:
            break
    return [repeating, missing]


if __name__ == "__main__":
    arr = [3, 1, 2, 5, 3]
    print(solve(arr))

# Time Complexity = O(2n)
# Space Complexity = O(1)


"""
instead of counting occurences everytime we will store those occurences in hashing technique.

"""
