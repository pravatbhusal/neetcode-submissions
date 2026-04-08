class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # two pointers
        # slide the window when encountering lowest/highest value
        left_ptr = 0
        right_ptr = 0
        max_profit = 0

        while right_ptr < len(prices):
            if prices[right_ptr] < prices[left_ptr]:
                # update the new lowest ptr
                left_ptr = right_ptr
            # update max profit if the current window is larger
            cur_profit = prices[right_ptr] - prices[left_ptr]
            if cur_profit > max_profit:
                max_profit = cur_profit
            # continue
            right_ptr += 1

        return max_profit
