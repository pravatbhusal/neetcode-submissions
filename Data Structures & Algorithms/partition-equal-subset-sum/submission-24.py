"""
Similar problem: "Longest Increasing Subsequence"
This is also a variation of the 0/1 Knapsack Problem.

Recursive Backtracking O(2^N) Brute-force Solution:
Create every possible subset and check if two sub-sets equal each other.
This can be done using a Decision Tree and stopping iteration when i == len(nums).
Subset #1: The numbers we decided to keep
Subset #2: The numbers we decided not to keep
At i == len(nums), check if sum(Subset #1) == sum(Sumset #2).
If we tried every possible combination but the above condition is never true, then return False.

Now how can we memoize the results so that we don't repeat the same Decision Tree branch again?
And can we do this iteratively without needing to make a Decision Tree recursive stack?
"""
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            # short-circuit, odd sum cannot be partitioned
            # also further optimizes because we only need to check up to target (half of total)
            return False

        # dp stores if subset sum can be achieved at each sub-problem
        target = total // 2
        dp = [False] * (target + 1)
        dp[0] = True
        
        # build dp to verify that sum can be reached using subset of nums
        for num in nums:
            dp_updated = dp.copy()
            for i in range(len(dp)):
                dp_updated[i] = dp[i] or dp[i - num]
            dp = dp_updated

        return dp[target]

    # Recursive solution has same time complexity as iterative but O(N * total) space
    def canPartition_Recursion(self, nums: List[int]) -> bool:
        total = sum(nums)
        if total % 2 == 1:
            # short-circuit, odd sum cannot be partitioned
            return False

        dp = dict()

        def dfs(i: int, s1: int, s2: int) -> bool:
            if (i, s1, s2) in dp:
                # return memoized result
                return dp[(i, s1, s2)]

            # Base case: processed all numbers
            if i == len(nums):
                return s1 == s2

            # Branch 1: add nums[i] to Subset #1 (keep)
            # Branch 2: add nums[i] to Subset #2 (skip)
            result = dfs(i + 1, s1 + nums[i], s2) or \
                dfs(i + 1, s1, s2 + nums[i])
            dp[(i, s1, s2)] = result
            return result

        return dfs(0, 0, 0)