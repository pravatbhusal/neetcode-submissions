"""
This is a Graph problem because flights is an adjacency list of [from, to].

Understanding the variables:
src = starting airport
dst = destination airport
k = max # layovers from source to destination

Djikstra's algoritm (Not optimal):
Because we are given a stating airport, initial idea is to solve using Djikstra's,
which computes the shortest path from a source node to all of the nodes. However,
Djikstra's may not be the most optimal because restricted by k stops. At an edge,
the algorithm needs to store both (cost, stops) and optimize two dimensions.

Bellman Ford algorithm (Optimal):
This is a problem solved using Bellman Ford's algorithm. Bellman Ford is similar to
Djikstra's, but it supports computing short path for negative edge costs. But why
Bellman Ford if there are no negative edges in this problem?

We don't care about optimizing negatives in this problem. Rather, we'll reuse the
round-based relaxation that lets you control exactly how many edges are used.
The round-based principle of Bellman Ford is it visits edges at most n - 1 times.

It uses 2D Dynamic Programming (DP) to store the optimal path up to n - 1 times.
Recurrence function: dp[i][v] = cheapest cost to reach node v using at most i edges

We'll do round-based relaxation k + 1 times because k + 1 rounds gives us the
cheapest price using at most k + 1 edges, which equals at most k stops.

Example: src = Austin, dst = NYC, k = 0
We cannot have any layovers, must be a direct flight (because k = 0)
"""
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        # prices = cheapest known cost to reach each airport from src.
        prices = [math.inf] * n
        prices[src] = 0

        for i in range(k + 1):
            tmp_prices = prices.copy()
            for source, dest, price in flights:
                # store the min price from source -> destination
                tmp_prices[dest] = min(prices[source] + price, tmp_prices[dest])
            prices = tmp_prices

        if prices[dst] == math.inf:
            # cannot arrive to dst with k stops
            return -1
        return prices[dst]