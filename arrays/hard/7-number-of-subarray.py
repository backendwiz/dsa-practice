from collections import defaultdict


def solve(arr, k):
    n = len(arr)  # size of the given array.
    xr = 0
    mpp = defaultdict(int)
    mpp[xr] = 1  # setting the value of 0.
    cnt = 0

    for i in range(n):

        xr = xr ^ arr[i]
        x = xr ^ k

        cnt += mpp[x]

        mpp[xr] += 1
    return cnt


if __name__ == "__main__":
    arr = [4, 2, 2, 6, 4]
    k = 6
    print(solve(arr, k))

# Time Complexity =
# Space Complexity =
