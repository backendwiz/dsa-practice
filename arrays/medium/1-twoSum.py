def solve(arr, target):

    # hashMap = {}
    # for i in range(len(arr)):
    #     diff = target - arr[i]
    #     if diff in hashMap:
    #         return [i, hashMap[diff]]
    #     hashMap[arr[i]] = i
    hashMap = {}
    for i, num in enumerate(arr):
        diff = target - num
        if diff in hashMap:
            return [i, hashMap[diff]]
        hashMap[num] = i

    """"
        i = 0
        diff = 12
        12 not in hashMap
        so hashMap becomes = {0:2}
        i = 1
        diff = 8
        8 not in hashMap
        so hashMap becomes = {0:2, 1:6}
        i = 2
        diff = 9
        9 not in hashMap
        so hashMap becomes = {0:2,1:6,2:5}
        i = 3
        diff = 6
        6 in hashMap
        it returns [i, hashMap[diff]] = returns [3, 1]

        we can also use enumerate
        """


if __name__ == "__main__":
    arr = [2, 6, 5, 8, 11]
    target = 14
    print(solve(arr, target))

# Time Complexity = O(n)
# Space Complexity = O(n)
