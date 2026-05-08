"""
My first intuition is building a Trie and traversing the tree on wordDict to find all the words.
This can be built on sub-problem of each word in wordDict, so we can solve this using DP.

To think up of a DP solution, follow the roadmap: Decision Tree (Brute-force) -> DP
Decision Tree requires recursive backtracking, and DP would memoize each solution.

Example: s = "leetcode", wordDict = ["l", "leet", "code"]
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = dict()

        def dfs(i):
            if i in dp:
                # return memoized result
                return dp[i]
            if i == len(s):
                # base case - can segment string s
                dp[i] = True
                return True

            for j in range(i + 1, len(s) + 1):
                word = s[i:j]
                if word in wordDict and dfs(j):
                    dp[i] = True
                    return True
            
            dp[i] = False
            return False
        
        return dfs(0)
            