"""
Similar question to "Number of Islands".

We can likely use the same search for loop as that solution when we detect
a 1 in the matrix. And keep track of the island with the max number of 1s.
"""
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # right, left, down, up
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]

        def bfs(row, col):
            area = 1
            queue = deque()
            queue.append((row, col))

            # mark initial as visited as 0
            grid[row][col] = 0
            
            while queue:
                cell = queue.popleft()
                row, col = cell

                # for each direction, check the cell == "1"
                for dir in directions:
                    d_row, d_col = row + dir[0], col + dir[1]
                    in_bounds = d_row < len(grid) and d_row >= 0 and d_col < len(grid[0]) and d_col >= 0
                    if in_bounds and grid[d_row][d_col] == 1:
                        # mark cell visited as 0
                        grid[d_row][d_col] = 0
                        # add to queue to check this cell's directions
                        queue.append((d_row, d_col))
                        area += 1
            return area

        max_area = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 1:
                    # calculate this island's area
                    area = bfs(row, col)
                    max_area = max(max_area, area)
        
        return max_area