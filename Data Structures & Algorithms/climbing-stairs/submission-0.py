class Solution:
    def climbStairs(self, n: int) -> int:
        # O(N) space dp: store array from [0, ..., n]
        # for each i, find out distinct steps to reach
        # dp[i] = 1 step before + 2 step before = dp[i - 1] + dp[i - 2]
        
        # optimize space O(1), only need to store 3 variables
        # space optimized dp: dp[i], d[i - 1], dp[i - 2]
        one, two = 1, 1
        for i in range(n - 1):
            temp = one
            one = one + two
            two = temp
        return one