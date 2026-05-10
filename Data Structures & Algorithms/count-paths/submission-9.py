"""
Looks familiar to a Graph problem (Num of Islands). However, this problem is different
because we're counting all "possible unique paths", which builds on sub-problems.

Bottom-up tabulation DP solution:

Initialize dp 2D matrix, which'll store the number of unique paths at dp[i][j].

Recurrence function: dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

This function sums the count of paths from the prev row (i - 1) and prev col (j - 1).
Doing this function on the entire matrix builds up the total count of unique paths.
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
         dp = [[1] * n for _ in range(m)]
         
         # Build-up the number of unique paths from the prev row and col
         for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
         
         return dp[m - 1][n - 1]