"""
Brute-force would be iterating backwards from edges and removing the edge then
testing to see if all nodes can be visited using BFS (fully connected).

Optional Solution: What we're trying to detect here is where the "cycle" begins.
If we find two nodes that have 2+ paths to each other, then we can remove one edge
and still have a fully connected graph.
"""
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj_list = defaultdict(list)
        in_degree = [0] * (len(edges) + 1 )
        for a, b in edges:
            # undirected graph, add both nodes from edge
            adj_list[a].append(b)
            adj_list[b].append(a)
            # most node in-degree starts at 2 since graph is undirected
            in_degree[a] += 1
            in_degree[b] += 1

        # add nodes with 1 in-degree (undirected graph, so 1 represents initial)
        queue = deque()
        for i in range(len(in_degree)):
            if in_degree[i] == 1:
                queue.append(i)
        
        # BFS with Kahn's algorithm (Topological sort)
        # After BFS, all in-degree should be at 0 otherwise cycle is detected
        while queue:
            node = queue.popleft()
            in_degree[node] -= 1

            # visit each neighbor
            for neighbor in adj_list[node]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 1:
                    queue.append(neighbor)

        print(in_degree)
        for a, b in reversed(edges):
            if in_degree[a] == 2 and in_degree[b] == 2:
                # after visiting all nodes there was a cycle the BFS did not visit
                return [a, b]
        return []

        