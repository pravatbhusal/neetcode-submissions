"""
This problem asks to find the shortest path in a weighted graph, which is Djikstra's algorithm.
Djikstra's algorithm is Greedy algorithm, which runs BFS in the direction of the edge with the least weight.

Djikstra's greediness uses a Priority Queue, which is implemented using a Min-Heap. The priority queue must store
the total cost so far taking that path. This would ensure we're always visiting the shortest path so far.

n = # of nodes in graph
k = starting node (seed BFS)
"""
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # build an adjacency list with key = node, value = tuple(neighbor, weight)
        adj_list = defaultdict(list)
        for time in times:
            node, neighbor, weight = time
            adj_list[node].append((neighbor, weight))

        # min-heap as prio queue, seed with node k
        queue = [(0, k)]

        # BFS on priority queue
        visited = set()
        time = 0
        while queue:
            weight, node = heapq.heappop(queue)
            if node in visited:
                continue
            visited.add(node)
            time = weight

            # enqueue neighbors
            for neighbor, n_weight in adj_list[node]:
                if neighbor not in visited:
                    # push weight of path so far
                    heapq.heappush(queue, (weight + n_weight, neighbor))
            
        return time if len(visited) == n else -1