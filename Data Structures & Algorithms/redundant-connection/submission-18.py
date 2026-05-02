
class Solution:
    """
    When finding "connections" within a graph, Union-Find algorithm is most intuitive.
    
    We can use Union-Find to find a cycle:
    If r1 == r2, then the two nodes (n1 and n2) share the same root, meaning that
    they're already connected. That means union(n1, n2) would create a cycle since
    we're adding another redundant edge.
    """
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # initialize each node as its own parent
        n = len(edges) + 1
        parent = list(range(n))
        rank = [1] * n

        # finds the "root" of node by traversing up the parents
        def find(node):
            cur = node
            
            while cur != parent[cur]:
                parent[cur] = parent[parent[cur]] # path compression, amortized O(1)
                cur = parent[cur]
            return cur

        # union connects two nodes into the same root
        def union(n1, n2):
            r1, r2 = find(n1), find(n2)

            if r1 == r2:
                # u and v are already connected
                # unioning u and v again creates a redundant connection (cycle)
                return False

            # set connection (union)
            if rank[r2] > rank[r1]:
                # set n1's root to be under n2's root
                parent[r1] = r2
                rank[r2] += rank[r1]
            else:
                # set n2's root to be under n1's root
                parent[r2] = r1
                rank[r1] += rank[r2]
            return True

        for n1, n2 in edges:
            if not union(n1, n2):
                # cycle detected
                return [n1, n2]
        return True

    """
    Brute-force would be iterating backwards from edges and removing the edge then
    testing to see if all nodes can be visited using BFS (fully connected).

    Optional Solution: What we're trying to detect here is where the "cycle" begins.
    If we find a nodes that have 2+ paths to itself, then we can remove one edge and
    still have a fully connected graph.

    This can be solved optimally using Topological sort and checking in-degree after BFS.
    """
    def findRedundantConnection_TopoSort(self, edges: List[List[int]]) -> List[int]:
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

        for a, b in reversed(edges):
            if in_degree[a] == 2 and in_degree[b] == 2:
                # detected a cycle the BFS did not visit
                return [a, b]
        return []

        