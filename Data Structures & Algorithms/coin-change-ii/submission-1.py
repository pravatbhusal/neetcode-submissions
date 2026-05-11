"""
Similar Problems: "Coin Change"
The difference is that we're not trying to minimize the number of coins to amount. Instead, we're trying to find the
distinct combinations to amount.

Bottom-up DP approach:
Initialize dp array with length amount. dp[amt] is the number of distincts combinations that total to amt.
For each coin, iterate each amt and count the different combinations that equal i.

Unlike the Coin Change I, the outer loop is the coins. This builds coin combinations (not permutations)
because the coin outer loop means you commit to an ordering of coins.
This answers the question: "using coin c and the coins that came before it, how many ways can I make amt"?

Let's try to think of the recurrence function using an example.
Example: amount = 4, coins = [1, 2, 3]
dp[0] = 1
dp[1] = (1) = 1
dp[2] = (1 + 1), (2) = 2
dp[3] = (1 + 1 + 1), (2 + 1), (3) = 3
dp[4] = (1 + 1 + 1 + 1), (2 + 2), (2 + 1 + 1), (3 + 1) = 4

Recurrence function: dp[amt] += dp[amt - c]
This is because we're adding the number of combinations before this coin.
"""
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        dp = [0] * (amount + 1)
        dp[0] = 1
        
        for c in coins:
            for amt in range(amount + 1):
                if amt - c >= 0:
                    dp[amt] += dp[amt - c]

        return dp[amount]