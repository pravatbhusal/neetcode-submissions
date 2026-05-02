"""
If we rob nums[i], then we cannot rob nums[i - 1] or nums[i + 1].
Maximize the amount of money we can make from houses we can rob.

This cannot be solved greedily because picking the local maximum at index i
blocks i - 1 and i + 1 neighbors, and those two combined might be worth far
more than i alone. Ex: [1, 1, 3, 3]; It's bad choice to greedily pick i = 2.

This can be modeled using a Decision Tree and optimally solved using DP.

Overlapping sub-problem visual example [2, 9, 8, 3, 6]:
dp[0] = 2 -> [2] (take i = 0)
dp[1] = 9 -> [2, 9] (take i = 1)
dp[2] = 10 -> [2, 9, 8] (take i = 0, 2)
dp[3] = 12 -> [2, 9, 8, 3] (take i = 1, 3)
dp[4] = 16 -> [2, 9, 8, 3, 6] (take i = 0, 2, 4)

Based on the above example, dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
This compares the decision: do we take nums[i] or skip out on i - 1?
"""
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        i_1 = max(nums[0], nums[1])
        i_2 = nums[0]

        for i in range(2, len(nums)):
            # dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])
            temp = i_1
            i_1 = max(nums[i] + i_2, i_1)
            i_2 = temp

        return i_1