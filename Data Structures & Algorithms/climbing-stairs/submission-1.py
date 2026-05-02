"""
This can be visualized with a Decision Tree. We can memoize each decision
(climb 1 step or 2 steps) from the decision tree.

Solution:
1. Create a dp array of len(n)
2. dp[0] = # of ways to climb to 0th stair (answer = 0)
3. dp[1] = # of ways to climb to 1st stair (answer = 1)
4. dp[2] = # of ways to climb to 2nd stair (answer = 2)
5. dp[3] = # of ways to climb to 3rd stair (answer = 3)
6. dp[4] = # of ways to climb to 4th stair (answer = 5)

This looks very similar to Fibonacci sequence.
The decision tree can be modeled using: dp[i] = dp[i - 1] + dp[i - 2]
"""
class Solution:
    def climbStairs(self, n: int) -> int:
        i_1 = 1
        i_2 = 0
        for i in range(n):
            # dp[i] = dp[i - 1] + dp[i - 2]
            temp = i_1
            i_1 = i_1 + i_2
            i_2 = temp
        return i_1