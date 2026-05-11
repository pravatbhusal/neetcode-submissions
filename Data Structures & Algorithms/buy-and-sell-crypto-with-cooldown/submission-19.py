"""
Similar DP Problem: "House Robber"
If we robbed a house on nums[i], we cannot rob adjacent homes nums[i - 1] and nums[i + 1]
House Robber recurrence function: dp[i] = max(nums[i] + dp[i - 2], dp[i - 1])

Restrictions for this problem:
1. If we sell coin at prices[i], we cannot buy another coin at prices[i + 1].
2. We can only hold 1 coin at a time, so we are forced to sell.

There are three states to maintain for this problem:
1. You are currently holding a stock
2. You are currently in cooldown (just sold)
3. You are currently idle (no stock, not in cooldown, free to buy)

This is a 2DP problem because of the two dimensions:
1. Store the best profit at dp[i].
2. Are we able to buy or not buy at day i?

Top-down solution O(N) space:
The top-down solution using recursive backtracking with memoization is O(N) space.
Space complexity is the same both bottom-up and top-down, so let's solve top-down.

This can be modeled using a Decision Tree, using example: [1, 3, 4, 0, 4]
O(N) space solution because: dp[i][0] = True (can buy), dp[i][1] = False (cannot buy)
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        dp = dict()

        def helper(i, buy):
            if i >= len(prices):
                return 0
            if (i, buy) in dp:
                return dp[(i, buy)]
            
            if buy:
                # buy at i
                buy_profit = helper(i + 1, False) - prices[i]
                # skip buying at i
                not_buy_profit = helper(i + 1, True)
                # store max profit
                dp[(i, buy)] = max(buy_profit, not_buy_profit)
            else:
                # sell at i
                sell_profit = helper(i + 2, True) + prices[i]
                # skip selling at i
                not_sell_profit = helper(i + 1, False)
                # store max profit
                dp[(i, buy)] = max(sell_profit, not_sell_profit)
            
            return dp[(i, buy)]

        return helper(0, True)