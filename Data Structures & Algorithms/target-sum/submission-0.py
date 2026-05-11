"""
0/1 Knapsack Problem (can only use nums[i] once)

Similar problem: "Coin Change II"
This problem is the exact same as Coin Change II, but with the idea of addition and subtraction and that we can only
use the number exactly once (0/1 Knapsack problem).

The dp array will be the length of the target and tells us at dp[i] = # of ways to sum to i

Let's solve this using top-down Recursive Backtracking:
Base case: Does sum == target?
Then recursively backtrack the two options:
    1. Add num at i
    2. Substract num at i
"""
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        def helper(i, total):
            if i == len(nums):
                return 1 if total == target else 0

            add = helper(i + 1, total + nums[i])
            sub = helper(i + 1, total - nums[i])
            return add + sub

        return helper(0, 0)
            