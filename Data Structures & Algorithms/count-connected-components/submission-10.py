class Solution:
    """
    When finding "connections" within a graph, Union-Find algorithm is most intuitive.
    """
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # initialize each node as its own parent
        parent = list(range(n))
        rank = [0] * n

        # finds the "root" of node
        def find(node):
            cur = node
            
            while cur != parent[cur]:
                cur = parent[parent[cur]] # path compression, becomes amortized O(1)
                cur = parent[cur]
            return cur

        # union connects two nodes into the same root
        def union(n1, n2):
            r1, r2 = find(n1), find(n2)

            if r1 == r2:
                # u and v are already connected
                return 0

            # set connection (union)
            if rank[r2] > rank[r1]:
                # set n1's root to be under n2's root
                parent[r1] = r2
                rank[r2] += rank[r1]
            else:
                # set n2's root to be under n1's root
                parent[r2] = r1
                rank[r1] += rank[r2]
            return 1

        connections = n
        for n1, n2 in edges:
            connections -= union(n1, n2)
        return connections

    """ 
    Note: Keeping this BFS solution because it is a valid and optimal.

    Create an adjancency list from the edges.

    Then run a loop to BFS on each node from the list. In the BFS, we need to keep track of
    the visited nodes. For any node in that visited set, it's within a single connected component.

    On each iteration, do not re-visit nodes in the visited set. When a node is not in the
    visited set, that's a new component.
    """
    def countComponents_BFS(self, n: int, edges: List[List[int]]) -> int:
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