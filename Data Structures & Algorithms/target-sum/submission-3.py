"""
0/1 Knapsack Problem (can only use nums[i] once)

Similar problem: "Coin Change II"
This problem is the exact same as Coin Change II, but with the idea of addition and subtraction and that we can only
use the number exactly once (0/1 Knapsack problem).

The dp array will be the length of the target and tells us at dp[i] = # of ways to sum to i

Let's solve this using top-down Recursive Backtracking:
Base case: Does sum == target?
Then recursively backtrack the two options:
    1. Add num at i ->  helper(i + 1, total + nums[i])
    2. Substract num at i -> helper(i + 1, total - nums[i])

Notice that there are two dimensions (2DP), which is i and the current total.
"""
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        dp = dict()

        def helper(i, total):
            key = (i, total)
            if key in dp:
                # return memoized result
                return dp[key]
            if i == len(nums):
                return 1 if total == target else 0

            # add at nums[i]
            add = helper(i + 1, total + nums[i])
            # subtract from nums[i]
            sub = helper(i + 1, total - nums[i])
            # memoize result
            result = add + sub
            dp[key] = result
            return dp[key]

        return helper(0, 0)
            