"""
Return "all distinct solutions" hints to me this is recursive backtracking (brute-force).
Another dead giveaway is the constraints are so small: 1 <= n <= 8

If do recursive backtracking, then we can place a Q and then backtrack to see if there's another valid spot.
Keep recursively backtracking all possible combinations where N queens is valid on the board.

How to calculate if Q is on diagonal? See example: [0, 0], [1, 1], [2, 2]
Math formula (left diagonal) r1 + c1 == r2 + c2
Math formula (right diagonal): r1 - c1 == r2 - c2

Recursive backtracking algorithm:
1. The recursive helper function is helper(row), where row is the row index we're checking against.
2. Store the col indices, computed left_diag, and computed right_diag of all Qs on the current board
3. For each col, check if I place a Q on this index then there's not another Q in the same col or diagonal?
4. If yes, then skip.
5. If no, then we can place Q and:
    a. Recurse helper(row + 1)
    b. Backtrack the Q index
    c. Again recurse helper(row + 1)
"""
class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        # cols of Q
        q_cols = set()
        # computed diagonals of Q
        left_diag = set()
        right_diag = set()

        board = [["."] * n for i in range(n)]
        result = []
        def helper(row):
            if row == n:
                if len(q_cols) == n:
                    # valid board combination
                    copy = ["".join(row) for row in board]
                    result.append(copy)
                return
            for col in range(n):
                l_diag = row + col
                r_diag = row - col
                if col in q_cols or l_diag in left_diag or r_diag in right_diag:
                    # another Q exists in col or diagonal, ignore
                    continue
                # place Q
                board[row][col] = "Q"
                q_cols.add(col)
                left_diag.add(l_diag)
                right_diag.add(r_diag)
                helper(row + 1)
                # backtrack Q
                board[row][col] = "."
                q_cols.remove(col)
                left_diag.remove(l_diag)
                right_diag.remove(r_diag)

        helper(0)
        return result