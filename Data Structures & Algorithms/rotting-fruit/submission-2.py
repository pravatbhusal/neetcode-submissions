"""
Every minute, 1 -> 2 if it's adjacent to 2.
How many minutes until all fruits are 2?

This is a similar question to "Walls and Gates" problem.

Solution: Multi-source BFS

BFS will always be the "shortest path" for unweighted edges, so it will guarantee
the minimum number of minutes if queue is empty.

Start a BFS from each rotten fruit and traverse level-by-level till all fruits
that are adjacent become rotten.

Then iterate the grid to ensure there are no more fresh fruit (isolated 1st that
were never reached). If there are fresh fruits, then return -1.
"""
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # enqueue all rotten fruits
        queue = deque()
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 2:
                    queue.append((i, j, 0))

        directions = [[1,0], [-1, 0], [0, 1], [0, -1]]

        # multi source BFS - rot each fruit starting from a rotten fruit
        minutes = 0
        while queue:
            cell = queue.popleft()
            row, col, minutes = cell

            for dir in directions:
                n_row, n_col = row + dir[0], col + dir[1]
                in_bounds = n_row in range(len(grid)) and n_col in range(len(grid[n_row]))
                if in_bounds and grid[n_row][n_col] == 1:
                    # rot this fresh fruit and add it to the queue
                    grid[n_row][n_col] = 2
                    queue.append((n_row, n_col, minutes + 1))

        # if any fruit is still fresh (could not be reached), return -1
        for i in range(len(grid)):
            for j in range(len(grid[i])):
                if grid[i][j] == 1:
                    return -1
        
        return minutes
        