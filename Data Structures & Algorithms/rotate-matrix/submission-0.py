"""
Transpose the matrix: flip row to columns and vice versa.
"""
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # Transpose the matrix (swap row and col cell)
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reverse each row
        for row in matrix:
            row.reverse()