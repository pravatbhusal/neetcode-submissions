"""
Brute-force: Create every possible subset and check if two sub-sets equal each other.
This can be done using a Decision Tree and stopping iteration when i == len(nums).
Subset #1: The numbers we decided to keep
Subset #2: The numbers we decided not to keep
At i == len(nums), check if sum(Subset #1) == sum(Sumset #2).
If we tried every possible combination but the above condition is never true, then return False.

Now how can we memoize the results so that we don't repeat the same Decision Tree branch again?
"""
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total = sum(nums)
        memo = {}

        def dfs(i: int, s1: int) -> bool:
            if i == len(nums):
                return s1 == total - s1  # s1 == s2

            if (i, s1) in memo:
                return memo[(i, s1)]

            result = dfs(i + 1, s1 + nums[i]) or dfs(i + 1, s1)
            memo[(i, s1)] = result
            return result

        return dfs(0, 0)