"""
Solution is very simple.
Mark visited nodes from "1" to "0" to not visit them again
"""
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def bfs(row, col):
            queue = deque()
            queue.append((row, col))
            
            while queue:
                cell = queue.popleft()

                # mark as visited
                row, col = cell
                grid[row][col] = "0"

                # add right cell to the queue
                r_col = col + 1
                if r_col < len(grid[0]) and grid[row][r_col] == "1":
                    grid[row][r_col] = "0"  # ← mark here on enqueue
                    queue.append((row, r_col))

                # add left cell to the queue
                l_col = col - 1
                if l_col >= 0 and grid[row][l_col] == "1":
                    grid[row][l_col] = "0"  # ← mark here on enqueue
                    queue.append((row, l_col))

                # add down cell to the queue
                d_row = row + 1
                if d_row < len(grid) and grid[d_row][col] == "1":
                    grid[d_row][col] = "0"  # ← mark here on enqueue
                    queue.append((d_row, col))

                # add up cell to the queue
                u_row = row - 1
                if u_row >= 0 and grid[u_row][col] == "1":
                    grid[u_row][col] = "0"  # ← mark here on enqueue
                    queue.append((u_row, col))

        islands = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    # count this island
                    islands += 1
                    bfs(row, col)
        
        return islands