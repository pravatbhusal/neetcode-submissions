"""
This is a graph problem as represented in the problem statement. Build an adjacency list using the tickets.
Example: [["BUF","HOU"],["HOU","SEA"],["JFK","BUF"]]
"JFK" -> "BUF"
"BUF" -> "HOU"
"HOU" -> "SEA"

We must return the "lexicographically smallest" flight path, which means the edge cost from one airport to its neighbor.
The cost is compared by the airports in a ticket, example: ["HOU", "SEA"] > ["BUF", "HOU"]

Why Djikstra's won't work here:
Because we are given the source node "JFK", have positive edge weights (lexigraphic cost), my first thought is to
use Djikstra's algorithm.

But Djikstra's won't work because we need 1 single path from JFK that visits each edge once. Djikstra cannot build
1 single path from a source node to every edge because it creates multiple paths using BFS.

Ex: tickets = [["JFK","KUL"], ["JFK","NRT"], ["NRT","JFK"]]
Dijkstra's shortest-path from JFK = {JFK->KUL, JFK->NRT}
The ticket NRT->JFK is silently discarded — it doesn't shorten the path to any node.
But we have 3 tickets and must use all 3.

This is an Eulerian path problem (use every edge exactly once). Two ways to solve it: Backtracking vs Hierholzer's.

Backtracking O(E * V):
To ensure we process the lexicographically smallest first, we sort the tickets and build an adjacency list.
Then visit every node in the graph and backtrack if we hit a dead-end. Keep recursing and backtracking
until we find a path that visits all the edges (# of nodes visited = # of tickets + 1).

Hierholzer's algorithm O(ELog(E)):
To ensure we process the lexicographically smallest first, sort the tickets in descending order and build an adjacency list.
Then visit every node in the graph and and pop from the end of the adjacency list to get the smallest.
Add the node to the result after visiting all neighboring edges (post-order DFS).
"""
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        # build adjancency list from lexicographically descending order of tickets
        adj = defaultdict(list)
        for src, dst in sorted(tickets, reverse=True):
            print(src, dst)
            adj[src].append(dst)
        
        result = []
        def dfs(src):
            while adj[src]:
                # pop lexigraphically smallest ticket (at the end)
                dst = adj[src].pop()
                dfs(dst)
            # post-order: append after visting all outgoing edges of this node
            result.append(src)

        dfs("JFK")
        result.reverse()
        return result