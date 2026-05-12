"""
0/1 Knapsack Problem (can only use nums[i] once)

Similar problem: "Coin Change II"
This problem is the exact same as Coin Change II, but with the idea of addition and subtraction and that we can only
use the number exactly once (0/1 Knapsack problem).

The dp array will be the length of the target and tells us at dp[i] = # of ways to sum to i

Let's solve this using Top-down Recursive Backtracking:
Base case: Does sum == target?
Then recursively backtrack the two options:
    1. Add num at i = helper(i + 1, total + nums[i])
    2. Substract num at i = helper(i + 1, total - nums[i])

Notice that there are two dimensions (2DP), which is i and the current total.
Top-down recurrence function: dp[i][total] = add + sub

Now let's solve this using Bottom-up Tabulation:
Based on the top-down recurrence function, we can derive the bottom-up recurrence function.
Bottom-up recurrence function: dp[i][total] = dp[i + 1][total + nums[i]] + dp[i + 1][total - nums[i]]

We need to compute i + 1, so we must iterate the nums array in reverse. It's difficult to know which value to assign
dp[n][target] to seed the DP, so instead let's make the recurrence function where we iterate in the array in-order.

Seed dp[0][0] = 1 because there is 1 way with no nums to get total = 0.

Bottom-up recurrence function (in order):
dp[i + 1][total + nums[i]] += dp[i][total]
dp[i + 1][total - nums[i]] += dp[i][total]

At any point, you only ever need two rows — the current (i) and the next (i + 1).
Therefore, we can further optimize the Bottom-up recurrence function to O(N) space:
dp[total + nums[i]] += dp[total]
dp[total - nums[i]] += dp[total]
"""
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = defaultdict(int)
        dp[0] = 1

        for i in range(n):
            next_dp = defaultdict(int)
            for total in dp:
                next_dp[total + nums[i]] += dp[total]
                next_dp[total - nums[i]] += dp[total]
            dp = next_dp

        return dp[target]

    # Top-down Recursive solution, same time complexity and space complexity as iterative approach.
    def findTargetSumWays_Recursive_Top_Down(self, nums: List[int], target: int) -> int:
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
            dp[key] = add + sub
            return dp[key]

        return helper(0, 0)
            