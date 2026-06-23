"""
Recursive solution: Start at each cell and move in horizontal/vertical direction and increment the length of the path.
The path must be strictly increasing, so use a parameter prev and check the current cell is greater than prev cell.
"""
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        dp = dict()
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

        def dfs(r, c, prev):
            if r not in range(ROWS) or c not in range(COLS) or matrix[r][c] <= prev:
                # out of bounds or not strictly increasing
                return 0
            if (r, c) in dp:
                # return memoized
                return dp[(r, c)]
            # store the largest path from each direction
            max_path = 0
            for dir in directions:
                r_next, c_next = r + dir[0], c + dir[1]
                max_path = max(max_path, dfs(r_next, c_next, matrix[r][c]))
            # memoize and return
            dp[(r, c)] = max_path + 1
            return dp[(r, c)]

        max_path = 0
        for r in range(ROWS):
            for c in range(COLS):
                max_path = max(max_path, dfs(r, c, -1))
        return max_path
    