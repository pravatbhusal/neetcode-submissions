"""
Top-down recursive DP solution:
Number of unique possible paths implies brute-force with recursive bactracking.
Memoize the grid[i][j] path that we already took to prevent re-counting.

Can we think of a bottom-up tabulation DP solution? Solution:

Initialize dp 2D matrix, which'll store the number of unique paths at dp[i][j].

Recurrence function: dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
This function sums the count of paths above the row i and left of the col j.
Doing this function on the entire matrix builds up the total count of unique paths.
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
         dp = [[1] * n for _ in range(m)]
         
         # Build-up the number of unique paths from the prev row and col
         for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i - 1][j] + dp[i][j - 1]
         
         return dp[m-1][n-1]