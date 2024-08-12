def solve(A):
    n = len(A)
    mpp = {}
    maxi = 0
    sum = 0
    for i in range(n):
        sum += A[i]
        if sum == 0:
            maxi = i + 1
        else:
            if sum in mpp:
                maxi = max(maxi, i - mpp[sum])
            else:
                mpp[sum] = i
    return maxi


if __name__ == "__main__":
    arr = [9, -3, 3, -1, 6, -5]
    print(solve(arr))
