"""
Transpose the matrix: flip row to columns and vice versa.

We want to transpose the vertical reverse of the matrix. If we flip the rows to columns of the
vertical reverse matrix, we would have the rotated image matrix.
"""
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        # Reverse (vertical flip)
        matrix.reverse()
        print("Original:", matrix)

        # Transpose (swap row and col cell)
        for i in range(len(matrix)):
            for j in range(i, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            print(matrix)