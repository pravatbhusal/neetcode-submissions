"""
Problem mentions "unlimited number of times" and lets us choose between adding, deleting, or replacing at each index i.
This can be solved using Recursive Backtracking since we must choose between 3 options.

If word1[i] != word2[j]:
    1. Add char at word1[i]
    2. Remove char at word1[i]
    3. Replace char word1[i] with a letter to make it equal to word2[j]

2DP Problem:
This is a 2DP problem because we need to memoize the result on dp[i][j].
dp[i][j] = min num of operations for sub-problem up to word1[i] and word2[j]

Top-down Recursive Backtracing approach:
We must explore all three paths, if word1[i] != word2[j]:
    1. Add char at word1: 1 + helper(i, j + 1)
    2. Remove char at word1: 1 + helper(i + 1, j)
    3. Replace char at word1: 1 + helper(i + 1, j + 1)
If word1[i] == word[j]:
    1. helper(i + 1, j + 1)

Store dp[i][j] = min of all paths
"""
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        dp = dict()
        
        def helper(i, j):
            key = (i , j)
            if key in dp:
                # return memoized result
                return dp[key]
            if i == len(word1):
                # word1 exhausted, insert remaining word2 chars
                return len(word2) - j
            if j == len(word2):
                # word2 exhausted, delete remaining word1 chars
                return len(word1) - i

            min_ops = math.inf
            if word1[i] != word2[j]:
                # add char at word1
                add = 1 + helper(i, j + 1)
                # remove char at word1
                remove = 1 + helper(i + 1, j)
                # replace char at word1
                replace = 1 + helper(i + 1, j + 1)
                min_ops = min(add, remove, replace)
            else:
                # same char, no op
                no_op = helper(i + 1, j + 1)
                min_ops = min(min_ops, no_op)
            dp[key] = min_ops
            return min_ops

        return helper(0, 0)
            