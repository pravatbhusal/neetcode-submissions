"""
Interleaving means we can split s1 and s2 into different combinations
and then merge them together to form s3. All chars of s1 and s2 must be
used to create s3.

We must maintain order, meaning we cannot skip using a char. This implies
the problem requires us to use s1[i] or s2[j] if it becomes a substr of s3.

Top-down Recursive Backtracking Solution:
helper(i, j, temp) where i = index of s1, j = index of s2, s = string so far

Base case: i == len(s1) and j == len(s2)
If we arrived to this base-case, return True.

There are two paths we can recurse into:
if adding i + 1 is a substr of s3:
    helper(i + 1, j, temp + s1[i])
if adding j + 1 is a substr of s3:
    helper(i, j + 1, temp + s1[j])
"""
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            # all chars of s1 and s2 must build to s3
            return False

        dp = dict()
        
        def helper(i, j, k):
            key = (i, j)
            if key in dp:
                # return memoized result
                return dp[key]
            if i == len(s1) and j == len(s2):
                # can build s3 using all chars of s1 and s2!
                return True
            if i < len(s1) and k < len(s3):
                # does adding s1[i] make it a substr of s3?
                if s1[i] == s3[k]:
                    found = helper(i + 1, j, k + 1)
                    if found:
                        dp[key] = True
                        return True
            if j < len(s2) and k < len(s3):
                # does adding s2[j] make it a substr of s3?
                if s2[j] == s3[k]:
                    found = helper(i, j + 1, k + 1)
                    if found:
                        dp[key] = True
                        return True
            dp[key] = False
            return False
        
        return helper(0, 0, 0)