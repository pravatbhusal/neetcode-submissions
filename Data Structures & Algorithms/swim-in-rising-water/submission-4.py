"""
We need to find the shortest path from (0, 0) to (n - 1, n - 1) that minimizes the cost of visting a node in that path.

We can use a modified Djikstra's algorithm, where instead of summing the total cost of each edge in the path, we only need
to store the max node cost seen so far in the path. Then use a min heap to visit a path that minimizes the max cost so far.
"""
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        n = len(grid)
        min_heap = [(grid[0][0], 0, 0)]
        visited = set()
        dist = dict()
        directions = [[1, 0], [0, 1], [0, -1], [-1, 0]]

        while min_heap:
            max_cost, row, col = heapq.heappop(min_heap)
            if (row, col) in visited:
                continue
            visited.add((row, col))
            dist[(row, col)] = max_cost

            # check each adjacent direction from this node
            for dir in directions:
                row_n, col_n = row + dir[0], col + dir[1]
                if row_n in range(n) and col_n in range(n):
                    if (row_n, col_n) not in visited:
                        # enqueue the neighbor and store max cost seen so far for this path
                        max_cost_n = max(max_cost, grid[row_n][col_n])
                        heapq.heappush(min_heap, (max_cost_n, row_n, col_n))

        return dist[(n - 1, n - 1)]