class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # we need to iterate the board 3 separate times, where each loop:
        # 1) store a set for each row
        # 2) store a set for each column
        # 3) store a 3x3 set for each sub-box

        # check each row
        for row in board:
            dups = set()
            for col in row:
                if col in dups:
                    return False
                if col != ".":
                    dups.add(col)
        
        # check each col
        for i, col in enumerate(board[0]):
            dups = set()
            for j, row in enumerate(board):
                val = board[j][i]
                if val in dups:
                    return False
                if val != ".":
                    dups.add(val)

        # helper to check within 3x3 sub grid
        def helper_subox(start_row, start_col):
            dups = set()
            for row in range(start_row, start_row + 3):
                for col in range(start_col, start_col + 3):
                    val = board[row][col]
                    if val in dups:
                        return False
                    if val != ".":
                        dups.add(val)
            return True

        # run the helper_subox on each 3x3 grid
        for row in range(3):
            for col in range(3):
                if not helper_subox(row * 3, col * 3):
                    return False
        return True