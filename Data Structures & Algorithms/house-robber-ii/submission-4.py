"""
Same limitations as House Robber I, but i = 0 and i = n - 1 cannot be robbed.

This can be modeled using a Decision Tree, and we only pick the optimal path.
Ex: [2, 9, 8, 3, 6]
1. [2] -> Take 2 = 2
2. [2, 9] -> Take 9 = 9
3. [2, 9, 8] -> Take 9 = 9
4. [2, 9, 8, 3] -> Take 9, 3 = 12
5. [2, 9, 8, 3, 6] -> Take 9, 6 = 15

Recurrence relationship: dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
This formula compares robbing this house vs skipping on the house. This only works
when we're not considering the new constraint, which is we cannot rob the first
and last indices together.

Esentially what we need to do is update the relationship by having two separate DPs:
1. One DP loop when you take nums[0]
2. One DP loop when you take nums[n - 1]
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        def helper(nums):
            i_1 = max(nums[0], nums[1])
            i_2 = nums[0]

            for i in range(2, len(nums)):
                # dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
                temp = i_1
                i_1 = max(nums[i] + i_2, i_1)
                i_2 = temp

            return i_1

        return max(helper(nums[1:]), helper(nums[:-1]))