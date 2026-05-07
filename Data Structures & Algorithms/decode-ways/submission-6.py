"""
This is like recursive backtracking, where we brute-force every possibile combination of the sub-problem.
Can we memoize the recursive sub-problem and solve using DP?

Ex: "1012"
"J", "A", "B" = (10 1 2)
"J", "L" = (10, 12)

The only possible number combinations are 1 - 26, meaning at most 2 digits can form a character.
How do we handle 0? We only allow it to be used at the end of a 2 digit number (e.g. 10 or 20)

Solution:
1. Base case: i == len(s), return 1 (completed a grouping)
2. Base case: s[i] == 0, return 0 (cannot use 0 as mapping)
3. Add these two recursive results together:
    1. Recursively consume each char as 1 number.
    2. If s[i:i+2] <= 26, consume 2 chars as 1 number and continue recursion.

Memoize the result at each value i using dp[i] = result.

FOLLOW-UP: Can we do this in O(1) space?
Yes, we can. We only need 2 variables for i + 1 and i + 2 and use an iterative approach to solve the problem.
The O(N) space solution is fine for interviews since it's more readable.
Be prepared if the interviewer may ask follow-up to code the O(1) solution.
"""
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = dict()

        def helper(i):
            if i in dp:
                # return memoized result
                return dp[i]

            if i == len(s):
                # completed a grouping
                return 1
            
            if s[i] == "0":
                # 0 cannot be used as a decoding
                return 0

            # 1-digit path
            sum = helper(i + 1)

            # 2-digit path
            if i + 1 < len(s) and int(s[i:i+2]) <= 26:
                sum += helper(i + 2)

            # memoize sum for future recursive calls
            dp[i] = sum
            return sum

        return helper(0)




