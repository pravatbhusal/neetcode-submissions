"""
-1 = cannot traverse
0 = good, find this!
INF = can traverse

Problem is asking to fill each INF with the shortest distance to 0.

Don't confuse this with Djikstra's, which is weighted shortest path.
Plain BFS will guarantee shortest path if there is no weights on edges.

Solution using Multi-source BFS:
Start BFS with all treasure chests (sources) and fill the shortest distance for
each node, time is O(m*n). This is much better than running BFS on each
land cell, which would be O((m*n)^2).

Because BFS expands level-by-level, the first node that a treasure reaches
is always the closest. So with multi-source BFS, if a treasure A finds
that a node is already filled by treasure B, then skip traversing it.
"""
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # enqueue all the treasure chests
        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 0:
                    queue.append((i, j, 0))

        directions = [[1,0], [-1, 0], [0, 1], [0, -1]]

        # multi-source BFS - fill each land cell starting from a treasure chest
        while queue:
            cell = queue.popleft()
            row, col, distance = cell

            # check all directions
            for dir in directions:
                n_row, n_col = row + dir[0], col + dir[1]
                in_bounds = n_row in range(len(grid)) and n_col in range(len(grid[n_row]))
                if in_bounds and grid[n_row][n_col] == 2147483647:
                    queue.append((n_row, n_col, distance + 1))
                    grid[n_row][n_col] = distance + 1

            