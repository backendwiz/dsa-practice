def solve(arr):

    n = len(arr)
    ans = []
    arr.sort()
    for i in range(n):
        if i != 0 and arr[i] == arr[i - 1]:
            continue
        j = i + 1
        k = n - 1

        while j < k:
            total_sum = arr[i] + arr[j] + arr[k]
            if total_sum < 0:
                j += 1
            elif total_sum > 0:
                k -= 1
            else:
                temp = [arr[i], arr[j], arr[k]]
                ans.append(temp)
                j += 1
                k -= 1
                while j < k and arr[j] == arr[j - 1]:
                    j += 1
                while j < k and arr[k] == arr[k + 1]:
                    k -= 1
    return ans


if __name__ == "__main__":
    arr = [-1, 0, 1, 2, -1, -4]
    print(solve(arr))

# Time Complexity = O(n^2)
# Space Complexity = O(1)

"""
While solving this problem find two elements for start point. first write basic and rough version of algorithm and then improve it.
"""
