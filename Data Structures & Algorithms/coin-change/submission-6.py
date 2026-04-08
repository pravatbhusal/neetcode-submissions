class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # store the min coins at each value from [0, ..., amount]
        # then at each index, look for the amount - min = 0
        # where min is the index u check diff from the dp array
        # at start, each value in array is greater than amount
        dp = [amount + 1] * (amount + 1)
        # 0 amount needs 0 coins
        dp[0] = 0

        if amount == 0:
            return 0
        
        for amn in range(1, amount + 1):
            for c in coins:
                if amn - c >= 0:
                    # if this coin has less needed for amn, then store it
                    dp[amn] = min(dp[amn - c] + 1, dp[amn])
        if dp[amount] < amount + 1:
            return dp[amount]
        return -1
