"""
Similar problem as "Number of Islands".

Solution:
We can find the island of "O"s and get the outer cells of that island.
Then check that every outer cell is surrounded by an X. If it is, then
we can mark every "O" cell in that island with "X".

This solution is efficient (verified with Claude Code), but it is too difficult
to implement. There is a simpler solution.

Simpler Solution:
Find the "O" cells that are NOT connected at the border and flip those.
This is because an "O" cell is connected to the border, all other cells
that are connected to it cannot be surronded by "X".

1. Start a BFS from each border "O" cell and mark each "O" as "S" to not flip.
2. Then iterate the entire board to only flip the "O" cells that still exist.
3. And replace the "S" cells with "O" cells to put those back to normal.
"""
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        if not board:
            return

        rows = len(board)
        cols = len(board[0])
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def bfs(r, c):
            # initial row and col from border
            queue = deque()
            queue.append((r, c))
            board[r][c] = "S"

            while queue:
                o_cell = queue.popleft()
                row, col = o_cell
                for dir in directions:
                    n_row, n_col = row + dir[0], col + dir[1]
                    in_bounds = n_row in range(rows) and n_col in range(cols)
                    if in_bounds and board[n_row][n_col] == "O":
                        # "O" cell touches border, mark as "S"
                        board[n_row][n_col] = "S"
                        queue.append((n_row, n_col))

        # start BFS on each border cells to mark as "S"
        for i in range(rows):
            for j in range(cols):
                outer_row = i == 0 or i == rows - 1
                outer_col = j == 0 or j == cols - 1
                if outer_row or outer_col:
                    if board[i][j] == "O":
                        bfs(i, j)

        # replace all remaining "O" with "X"
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "O":
                    board[i][j] = "X"
        
        # revert "S" back to "O"
        for i in range(rows):
            for j in range(cols):
                if board[i][j] == "S":
                    board[i][j] = "O"
