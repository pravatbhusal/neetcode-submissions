"""
"Sub-array" problem can be solved greedily. The academic name for this algorithm is called Kadane's algorithm.
This is actually a Dynamic Programming problem under the hood, but we only need 1 variable (sum).

The DP recurrence function is: dp[i] = max(nums[i], dp[i-1] + nums[i])
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