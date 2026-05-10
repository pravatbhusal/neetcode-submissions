"""
Looks familiar to a Graph problem (Num of Islands). But, this problem is different
because we're counting all "possible unique paths", which builds on sub-problems.

Bottom-up tabulation DP solution:

Initialize dp 2D matrix, which'll store the number of unique paths at dp[i][j].

Recurrence function: dp[i][j] = dp[i - 1][j] + dp[i][j - 1]

This function sums the count of paths from the prev row (i - 1) and prev col (j - 1).
Doing this function on the entire matrix builds up the total count of unique paths.

We can make a O(N) space solution only storing the number of unique paths for a row.
Recurrence function: dp[j] = dp[j] + dp[j - 1]
"""
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
         dp_row = [1] * n
         
         # Build-up the number of unique paths from the prev col of this row
         for i in range(1, m):
            for j in range(1, n):
                dp_row[j] = dp_row[j - 1] + dp_row[j]
         
         return dp_row[n - 1]