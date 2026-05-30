"""
Transpose the matrix: flip row to columns and vice versa.

If we flip the rows to columns of the vertical reverse matrix, it's the rotated image matrix.
"""
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # Reverse (vertical flip)
        matrix.reverse()

        # Transpose (swap row and col cell above the main diagonal)
        for row in range(len(matrix)):
            for col in range(row + 1, len(matrix)):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]