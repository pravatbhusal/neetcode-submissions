"""
A tree is graph with no cycles and every node is connected with exactly 1 path.

Solution:
1. Build an adjacency list from the edges
2. Run BFS on the adjacency list tracking visited nodes and parent:
   - If we see an already-visited neighbor that isn't our parent → cycle → not a tree
3. After BFS, check len(visited) == n
   - If not all nodes visited → disconnected → not a tree
"""
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return True

        # build an adjacency list using the edges
        adj_list = defaultdict(list)
        for edge in edges:
            # undirected graph, add both nodes from an edge
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])

        # BFS the adjacency list
        visited = set()
        queue = deque([(0, -1)])
        while queue:
            node, parent = queue.popleft()
            visited.add(node)

            for adj in adj_list[node]:
                if adj == parent:
                    # skip the same parent in undirected graph
                    continue
                elif adj in visited:
                    # detected cycle
                    return False
                queue.append((adj, node))

        # all nodes were visited (not disconnected graph)
        return len(visited) == n