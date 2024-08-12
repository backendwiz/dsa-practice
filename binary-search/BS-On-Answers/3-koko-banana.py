import math


def solve(piles, h):

    low = 1
    high = findMax(piles)

    while low <= high:
        mid = (low + high) // 2
        reqTime = totalHours(piles, mid)
        if reqTime <= h:
            high = mid - 1
        else:
            low = mid + 1
    return low


def findMax(arr):
    maxi = float("-inf")
    n = len(arr)

    for i in range(n):
        maxi = max(maxi, arr[i])
    return maxi


def totalHours(v, h):

    totalH = 0
    n = len(v)
    for i in range(n):

        totalH += math.ceil(v[i] / h)
    return totalH


if __name__ == "__main__":
    piles = [3, 6, 7, 11]
    hours = 8
    print(solve(piles, hours))

# Time Complexity = O(logn)
# Space Complexity = O(1)


"""
koko needs to total bananas in h hours. find k which who many banana she eats in an hour to comple all the pile.
find min and max possible k bananas. It will be min 1 banana or max value in arr.
find range

"""
