"""
Perform a binary search on both arrays using left/right ptrs that read from
both nums1 and nums2 as if the arrays are merged.

The binary search's target is the median value of the two lists. The median
is always the "middle" of the list. We're using two lists, so we need to find
the "middle" value between both the lists.

Assume we merged the two arrays, we need to know many did nums1 contribute
and how many did nums2 contribute to the left half of the merged array.

The target index is the "cut" position of nums1 and nums2 where it cuts
how many elements nums1 contributed and how many elements num2 contributed
to the left half of the merged array.

Example:
nums1:  [ 1  3  5 | 7 ]
                   ^i=3
nums2:  [ 2  4 | 6  8  10 ]
                ^j=2

left1  = nums1[2] = 5
right1 = nums1[3] = 7
left2  = nums2[1] = 4
right2 = nums2[2] = 6
Median = 5

Cut position: left1 <= right2 and left2 <= right1

We can derive left/right ptrs using only the cut position i of nums1:
- left1 = nums1[i - 1], right1 = nums1[i]
- j = cut position of nums2 = ((merged_len + 1) // 2) - i
- left2 = nums2[j - 1], right2 = nums2[j]
"""
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            # set nums1 smaller to prevent j from going out of bounds
            nums1, nums2 = nums2, nums1

        low = 0
        high = len(nums1)
        merged_len = len(nums1) + len(nums2)

        while low <= high:
            # i = cut position of nums1
            i = (low + high) // 2
            left1 = nums1[i - 1] if i > 0 else -math.inf
            right1 = nums1[i] if i < len(nums1) else math.inf

            # j = cut position of nums2
            j = ((merged_len + 1) // 2) - i
            left2 = nums2[j - 1] if j > 0 else -math.inf
            right2 = nums2[j] if j < len(nums2) else math.inf

            if left1 <= right2 and left2 <= right1:
                # found median of merged array
                if merged_len % 2 == 0:
                    return (max(left1, left2) + min(right1, right2)) / 2
                else:
                    return max(left1, left2)
            elif left1 > right2:
                # nums1's left partition is too large — shrink it
                high = i - 1
            else:
                # nums2's left partition is too large — nums1 must contribute more
                low = i + 1


