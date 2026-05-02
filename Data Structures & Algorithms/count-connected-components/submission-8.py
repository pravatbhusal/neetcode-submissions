"""
Create an adjancency list from the edges.

Then run a loop to BFS on each node from the list. In the BFS, we need to keep track of
the visited nodes. For any node in that visited set, it's within a single connected component.

On each iteration, do not re-visit nodes in the visited set. When a node is not in the
visited set, that's a new component.
"""
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        for a, b in edges:
            # undirected graph, add both nodes from the edge
            adj_list[a].append(b)
            adj_list[b].append(a)
        
        # BFS for a single component
        visited = set()
        def bfs(start):
            queue = deque()
            queue.append(start)
            visited.add(start)

            while queue:
                node = queue.popleft()
                
                for neighbor in adj_list[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)

        # count each connected component
        result = 0
        for node in adj_list.keys():
            if node not in visited:
                bfs(node)
                result += 1
        
        # add the remainder of nodes not visited (disconnected nodes)
        rem = n - len(visited)
        return result + rem