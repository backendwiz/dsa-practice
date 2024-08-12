# Using Map


# def solve(arr, arr2):
#     freq = {}
#     union = []

#     for i in arr:
#         freq[i] = freq.get(i, 0) + 1

#     for i in arr2:
#         freq[i] = freq.get(i, 0) + 1

#     for i in freq:
#         union.append(i)

#     return union


def solve(arr, arr2):
    s = set()
    union = []

    for num in arr:
        s.add(num)

    for num in arr2:
        s.add(num)

    for num in s:
        union.append(num)
    return union


if __name__ == "__main__":
    arr = [1, 2, 3, 4, 5]
    arr2 = [2, 3, 6]
    ans = solve(arr, arr2)
    print(ans)

# Time Complexity = O(m+n)
# Space Complexity = O(1)
