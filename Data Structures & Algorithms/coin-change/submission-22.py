"""
At first, I see the "fewest numnber of coins" and my intuition is greedy solution to always use the largest coin.
Greedy fails for example: coins = [1, 3, 4], amount = 6
We would pick 4, then 3 (cannot do), then 1, then 1 = 3 coins needed.
However, actual solution is 3, 3 = 2 coins needed.

Since greedy fails, we can use DP to solve this.
Find the most optimal way to coin change create a DP array of size amount, and build up the solution till amount.

Ex: coins = [1, 5, 10], amount = 12
dp[0] = 0
dp[1] = 1
dp[2] = 2
...
dp[5] = 1
dp[6] = 2
dp[7] = 3
...
dp[10] = 1
dp[11] = 2
dp[12] = 3

Solution:
1. If i is a coin, then dp[i] = 1
2. Else dp[i] = dp[i - c] + 1
"""
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [math.inf] * (amount + 1)
        dp[0] = 0
        
        for amt in range(amount + 1):
            for c in coins:
                if c == amt:
                    # most efficient to use the exact coin that equals amount
                    dp[amt] = 1
                if amt - c >= 0:
                    # use the smallest sub-problem and consume this coin (add +1)
                    dp[amt] = min(dp[amt], dp[amt - c] + 1)
        
        return dp[amount] if dp[amount] is not math.inf else -1