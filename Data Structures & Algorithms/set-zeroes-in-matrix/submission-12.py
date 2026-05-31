"""
Iterate rows and cols, if you see a 0 then mark the entire row and col indices to all 0s.
The hard part is ensuring if we iterate to one of the replaced 0s, we don't try to make those also 0s.
We need to somehow mark a cell as "overwritten to 0" so that we don't try to replace with 0 at the overwritten cell.

Time complexity:
Do not modify the matrix while scanning otherwise we'll end up cascading the newly updated 0s to trigger more 0s.
The solution is O(M * N) time with one loop to mark the row and col indices then another loop to replace with 0s.

Space complexity:
This is easy using an O(N) space solution to store which row and col indices should be set to all 0s.
To space optimize O(1), we can re-use the matrix itself to tell us which row and col indices should be all 0s.

First loop: If we see a 0, on the matrix we can mark the row's first index to be 0 and mark the column's first index to be 0.
Second loop: If we see either the row's first index or column's first index is 0, then mark that cell to 0.
Edge-case: Because we're re-using the first row and first col for marking, if there is any actual 0 on first row or first col,
then we must replace the first row and first col as all 0 in a separate loop.
"""
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        rows = len(matrix)
        cols = len(matrix[0])

        # edge case - does the first row or col have a 0?
        first_row_zero = False
        first_col_zero = False
        for i in range(cols):
            if matrix[0][i] == 0:
                first_row_zero = True
        for i in range(rows):
            if matrix[i][0] == 0:
                first_col_zero = True

        # mark the fisrt row and first col
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][j] == 0:
                    # mark this row to be all 0
                    matrix[i][0] = 0
                    # mark this col to be all 0
                    matrix[0][j] = 0

        # replace marked cells to 0
        for i in range(1, rows):
            for j in range(1, cols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        # edge case - replace first row or col if it has zero
        if first_row_zero:
            for i in range(cols):
                matrix[0][i] = 0
        if first_col_zero:
            for i in range(rows):
                matrix[i][0] = 0