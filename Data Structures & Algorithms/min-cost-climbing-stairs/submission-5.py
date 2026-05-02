"""
Similar problem to "Climbing Stairs", but the twist is we want the min number
of costs to finish iterating the array.

Greedy cannot solve this, local optimum -> global optimum is not true.
Ex: [10, 15, 20]
If we are greedy we start at 10, forced to go to 15 or 20. Total cost is 25.
Instead, if we started at 15, total cost is 15.

Brute-force would explore all decision paths. This can be modeled using a Decision Tree.
We only want the optimal decision of each path. DP array will store the min cost of each path i.
dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
"""
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        i_1 = cost[1]
        i_2 = cost[0]

        for i in range(2, len(cost)):
            # dp[i] = cost[i] + min(dp[i - 1], dp[i - 2])
            temp = i_1
            i_1 = cost[i] + min(i_1, i_2)
            i_2 = temp

        return min(i_1, i_2)