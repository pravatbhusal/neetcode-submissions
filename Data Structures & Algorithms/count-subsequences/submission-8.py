"""
"Subsequence" hints this is a DP or recursive backtracking pattern problem.
This problem counts the number of distinct subsequences of s that equal t.
 
Recursive backtracking solution:
1. helper function: track char at i in s and char at j in t
2. If j == len(t), return 1 (base case - fully matched t, count it)
3. If i == len(s), return 0 (base case - exhausted s without matching t)
4. Pick this char at i and recurse: helper(i + 1, j + 1)
5. Backtrack and don't pick this char at i and recurse: helper(i + 1, j)
 
Dynamic Programming (Bottom-up) solution:
From the top-down recursive solution, the recurrence function was:
dp[i][j] = dp[i + 1][j + 1] + dp[i + 1][j]
 
Because the recurrence uses ahead pointers i + 1 and j + 1, the iteration must
happen in reverse.
 
Before iterating in reverse, we seed dp[m] = 1 because when j == len(t),
we've fully matched t — count it as 1 valid subsequence.
 
We can further optimize this to 1D DP in O(len(t)) space. We need two values
from the next row (i + 1): dp[i+1][j] (same column, available as dp[j] before
update) and dp[i+1][j+1] (diagonal, which gets overwritten — so we save it as
`prev` before each iteration step).
"""
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        dp = [0] * (m + 1)

        # base case - seed end of t with 1
        dp[m] = 1

        for i in range(n - 1, -1, -1):
            prev = dp[m]
            for j in range(m - 1, -1, -1):
                # don't pick this char at i
                result = dp[j]
                if s[i] == t[j]:
                    # pick this char at i
                    result += prev
                prev = dp[j]
                dp[j] = result

        return dp[0]


    """
    Below is my bottom-up tabulation solution with 2DP and O(M * N) space.
    This is a more intuitive way to understand the recurrence using iteration.
    """
    def numDistinct_BottomUp_2DSpace(self, s: str, t: str) -> int:
        n = len(s)
        m = len(t)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        # base case - seed end of t with 1
        for i in range(n + 1):
            dp[i][m] = 1

        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                # don't pick this char at i
                dp[i][j] = dp[i + 1][j]
                if s[i] == t[j]:
                    # pick this char at i
                    dp[i][j] += dp[i + 1][j + 1]
        
        return dp[0][0]
    
    """
    Below is my top-down recursive backtracking solution without DP.
    This is to help understand the decision tree and recurrence functions.
    """
    def numDistinct_TopDown_Recursive(self, s: str, t: str) -> int:

        def helper(i, j):
            if j == len(t):
                # base case - found a subsequence
                return 1
            if i == len(s):
                # base case - out of bounds
                return 0

            result = 0
            if s[i] == t[j]:
                # pick this char at i
                result += helper(i + 1, j + 1)
            # backtrack - don't pick this char at i
            result += helper(i + 1, j)
            return result
        
        return helper(0, 0)