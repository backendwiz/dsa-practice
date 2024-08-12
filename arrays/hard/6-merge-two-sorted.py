def solve(nums1, m, nums2, n):

    i, j, k = m - 1, n - 1, m + n - 1

    while j >= 0:
        if i >= 0 and nums1[i] > nums2[j]:
            nums1[k] = nums1[i]
            i -= 1
        else:
            nums1[k] = nums2[j]
            j -= 1
        k -= 1


if __name__ == "__main__":
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    solve(nums1, m, nums2, n)
    print(nums1)

"""
We can solve this using two pointers i and j pointing towards end of arrays and pointer k will point towards end of merge array.
We repeatedly compare the last elements of the two arrays, placing the larger one at the end of the merged array and moving that array's pointer forward, until we reach the beginning of both arrays.
"""

# Time Complexity = O(m+n)
# Space Complexity = O(1)
