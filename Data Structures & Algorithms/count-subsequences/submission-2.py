"""
"Subsequence" hints this a DP or recursive backtracking pattern problem.
This is a simple problem that counts unique subsequences matching another string.

Recursive backtracking solution:
1. helper function: char at i in s and track char at j in t
2. If i goes out of bound, return 0 (base case)
3. If j == len(t), return 1 (base case)
3. Pick this char at i and recurse: helper(i + 1, j + 1)
4. Backtrack and not pick this char at i and recurse: helper(i + 1, j)

Dynamic Programming (Bottom-up) solution:
From the top-down recursive solution, the recurrence function was:
dp[i][j] = dp[i + 1][j + 1] + dp[i + 1][j]

Because the recurrence uses ahead pointers i + 1 and j + 1, the iteration must
happen in reverse.

Before iterating in reverse, we seed the DP with every dp[i][len(t)] = 1 because
each dp[i] means that's 1 subsequence that built string t.

We can further optimize this to 1DP in O(len(t)) space. Since we only need the prev value
on each iteration (i + 1 and j + 1), we only need to have a single variable prev where
prev = dp[j] and use that as the ref to dp[i][j + 1] when iterating backwards.
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
                # pick this char at i
                if s[i] == t[j]:
                    result += prev
                prev = dp[j]
                dp[j] = result

        return dp[0]
    def numDistinct_TopDown_Recursive(self, s: str, t: str) -> int:

        def helper(i, j):
            if j == len(t):
                # base case - found a subsequence
                return 1
            if i == len(s):
                # base case - out of bounds
                return 0

            # pick this char at i
            result = 0
            if s[i] == t[j]:
                result += helper(i + 1, j + 1)
            # backtrack - don't pick this char at i
            result += helper(i + 1, j)
            return result
        
        return helper(0, 0)