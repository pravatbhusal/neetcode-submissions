"""
Similar problem: "Longest Increasing Subsequence"

The "longest common subsequence" can only be determined through recursive backtracking. This is because
the sub-sequence may not be contigous. This is because you can delete some or no elements and then test
to see if the subsequence is valid.

We must try every possibility and then build on those sub-problems using DP to find the "longest" sub-problem.
This is a 2DP problem because we're building DP on two dimensions: text1 and text2.

Example using Decision Tree (Recursive Backtracking): text1 = "cat", text2 = "crabt"
t1 = "c", t2 = "c"
t1 = "ca", t2 = "cr" <- Does not work, backtrack
t1 = "ca", t2 = "ca"
t1 = "cat", t2 = "cab" <- Does not work, backtrack
t1 = "cat", t2 = "cat" <- Answer!

Bottom-up Tabluation Solution:
Create 2D dp matrix dp[i][j] that stores the longest subsequence up to i = index of text1, j = index of text2.

When text1[i] != text2[j], then dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
This is because we're re-using the previous sub-problem since we couldn't build a subsequence.

If text1[i] == text[j], then we can increment the subsequence at dp[i][j].
Recurrence question we need to ask: Which dp value represents "the LCS before we looked at either of these characters"?
That would be dp[i - 1][j - 1]
"""
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n = len(text1)
        m = len(text2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                if text1[i - 1] == text2[j - 1]:
                    # Equal subsequence, increment 1 from before i and j
                    dp[i][j] = 1 + dp[i - 1][j - 1]
                else:
                    # Not equal subsequence, use prev solution
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
        
        return dp[n][m]

    """
    The below solution was my initial top-down recursive solution. The reason it's incorrect is because the
    memoization is wrong. Why is it wrong?
    
    You visit (i, j) once with a short t1/t2, mark it True, then later reach the same (i, j) with a longer
    t1/t2 that could lead to a better answer — but you skip it because dp[i][j] is already True.

    Also, we don't need to do 4 recursive calls. We can do this with only 2 recursive calls that move i and j
    together. In the base-case, check that both text[i] == text[j], do 1 call if equal or two calls if not equal.
    """
    def longestCommonSubsequence_Wrong_TopDown_Recursive(self, text1: str, text2: str) -> int:
        longest = 0
        dp = dp = [[False] * len(text2) for _ in range(len(text1))]

        def helper(i, j, t1, t2):
            nonlocal longest
            if t1 == t2:
                # found largest subsequence
                longest = max(longest, len(t1))
            if i < len(text1) and j < len(text2) and dp[i][j]:
                # already explored this path
                return dp[i][j]
            if i < len(text1):
                t1 += text1[i]
                helper(i + 1, j, t1, t2)
                t1 = t1[:-1]
                helper(i + 1, j, t1, t2)
            if j < len(text2):
                t2 += text2[j]
                helper(i, j + 1, t1, t2)
                t2 = t2[:-1]
                helper(i, j + 1, t1, t2)
            if i < len(text1) and j < len(text2):
                dp[i][j] = True

        helper(0, 0, "", "")
        return longest
