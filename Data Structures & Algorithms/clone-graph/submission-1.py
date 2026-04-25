"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

"""
Similar question to "Copy List with Random Pointer" LinkedList problem.
The difference is that we are copying a graph with multiple nodes (neighbors).

Solution requires two loop passes with O(2(N + E)) time:
1. BFS the graph to create a dict of refs where the key is the node's ref
and the value is the copied node ref.
2. BFS the graph again to re-build the graph using the cloned nodes from the dict.

Or do it in a single pass with O(N + E) time:
1. Create the clones then wire them up in the same iteration
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None

        copies = defaultdict(None)
        copies[node] = Node(node.val)
        
        # BFS - copy the nodes
        queue = deque()
        queue.append(node)
        while queue:
            original = queue.popleft()
            copy = copies[original]
            
            for neighbor in original.neighbors:
                if neighbor not in copies:
                    # copy the neighbor
                    copies[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                # link the copied neighbor
                copy.neighbors.append(copies[neighbor])

        return copies[node]