"""
"Sub-array" problem can be solved greedily sliding window. Keep sliding the window
while the sum is positive. If sum becomes negative, then reset the window.

The academic name for this algorithm is called Kadane's algorithm.
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sum = 0
        max_sum = nums[0]

        for num in nums:
            if sum < 0:
                # negative, reset window
                sum = 0
            sum += num
            max_sum = max(sum, max_sum)
        return max_sum