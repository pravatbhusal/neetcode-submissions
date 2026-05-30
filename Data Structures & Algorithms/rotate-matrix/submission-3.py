"""
Transpose the matrix: flip row to columns and vice versa.

If we flip the rows to columns of the vertical reverse matrix, we would have the rotated image matrix.
"""
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # Reverse (vertical flip)
        matrix.reverse()
        print("Original:", matrix)

        # Transpose (swap row and col cell)
        for row in range(len(matrix)):
            for col in range(row, len(matrix)):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]