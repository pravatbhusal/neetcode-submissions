"""
There are two cases we need to be aware of using a 2DP matrix:
 - Current char we're indexing on (e.g. "aa" we would index on "a")
 - If we're matching to zero or more preceding elements (e.g. "a*" we would know the preceding element is "a" so we match True always to "a" in future elements)

We need two pointers: i and j where i = ptr on s and j = ptr on p
- if i == len(s) and j == len(p) then we matched p to s, return True
- j will track which index we're checking for p and if p pattern breaks at j then we return False

Three cases for the Top-Down recursive solution:
 - Case 1: p[j] matches s[i] directly (same char or '.') → recurse dfs(i+1, j+1)
 - Case 2: p[j+1] is '*' and current char doesn't match s[i] → zero occurrences, recurse dfs(i, j+2)
 - Case 3: p[j+1] is '*' and current char matches s[i] → one or more occurrences
           recurse dfs(i+1, j), or zero occurrences recurse dfs(i, j+2)
"""
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp = {}

        def dfs(i, j):
            if (i, j) in dp:
                return dp[(i, j)]

            # base case: pattern exhausted
            if j == len(p):
                return i == len(s)

            # does the current char pair match?
            first_match = i < len(s) and (p[j] == s[i] or p[j] == '.')

            if j + 1 < len(p) and p[j + 1] == '*':
                # zero occurrences (skip a*) OR one+ more occurrences (consume s[i])
                result = dfs(i, j + 2) or (first_match and dfs(i + 1, j))
            else:
                # direct match, advance both pointers
                result = first_match and dfs(i + 1, j + 1)

            dp[(i, j)] = result
            return result

        return dfs(0, 0)