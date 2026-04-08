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

        # TODO: use division / 3 to check within 3x3 grid
        for box_row in range(3):
            for box_col in range(3):
                seen = set()
                for r in range(box_row * 3, box_row * 3 + 3):
                    for c in range(box_col * 3, box_col * 3 + 3):
                        val = board[r][c]
                        if val == ".":
                            continue
                        if val in seen:
                            return False
                        seen.add(val)
        return True