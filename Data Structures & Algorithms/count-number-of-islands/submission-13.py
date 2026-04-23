"""
Solution is very simple.
Mark visited nodes from "1" to "0" to not visit them again
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # right, left, down, up
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def bfs(row, col):
            queue = deque()
            queue.append((row, col))
            
            while queue:
                cell = queue.popleft()
                row, col = cell

                # for each direction, check the cell == "1"
                for dir in directions:
                    d_row, d_col = row + dir[0], col + dir[1]
                    in_bounds = d_row < len(grid) and d_row >= 0 and d_col < len(grid[0]) and d_col >= 0
                    if in_bounds and grid[d_row][d_col] == "1":
                        grid[d_row][d_col] = "0"
                        queue.append((d_row, d_col))

        islands = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    # count this island
                    islands += 1
                    bfs(row, col)
        
        return islands