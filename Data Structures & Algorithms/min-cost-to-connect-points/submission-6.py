"""
This problem is asking to find the minimum distance to traverse the graph. The weights are defined as the distance
from node i to node j.

My first intuition is Dijkstra's, which finds the shortest path from a source node to all others.
But we don't care about paths from a source — we just need every node connected as cheaply as possible.
That means finding a Minimum Spanning Tree (MST): a subset of edges that connects all N nodes with no cycles,
minimizing the total edge cost. A graph can have many combinations of Spanning Trees, but we want the MST
that minimizes the distance across all nodes.

We use Prim's algorithm to build the MST greedily — always adding the cheapest edge that connects a new unvisited
node to the current tree.

Prim's algoritm is implemented very similarly to Djikstra's.
Same concept, priority queue (min heap) and run BFS.
"""
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        # build an adjacency list for the complete graph with distance between two nodes
        # Complete Graph = a maximal dense graph, all nodes have edges to other nodes
        n = len(points)
        adj_list = defaultdict(list)
        for i in range(n):
            xi, yi = points[i]
            for j in range(i + 1, n):
                xj, yj = points[j]
                distance = abs(xi - xj) + abs(yi - yj)
                # node at point i
                adj_list[i].append((j, distance))
                # node at point j
                adj_list[j].append((i, distance))

        # min-heap as prio queue, seed with (cost 0, node 0)
        queue = [(0, 0)]

        # Prim's (BFS on priority queue)
        visited = set()
        cost = 0
        while queue:
            distance, node = heapq.heappop(queue)
            if node in visited:
                continue
            visited.add(node)
            cost += distance

            # enqueue neighbors
            for neighbor, n_distance in adj_list[node]:
                if neighbor not in visited:
                    # push distance of neighbor
                    heapq.heappush(queue, (n_distance, neighbor))
            
        return cost