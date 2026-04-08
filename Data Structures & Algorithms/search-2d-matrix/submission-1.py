class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # flatten the matrix to a single list, O(N * M) space
        # run binary search on list, O(log(N * M)) time
        # but can we implement binary search on matrix in O(1) space?

        # what if we convert the 2D matrix indices into 1D indices?
        # example: matrix[0,0] = 0, matrix[0, 1] = 1, etc.
        # example: matrix[1,0] = 5, matrix[1, 1] = 6, etc.
        # matrix's 1D index = (row_i * len(matrix[0])) + col_i
        # col_i = (row_i * len(matrix[0])) - 1d_indx) * -1

        left = 0
        right = len(matrix) * len(matrix[0])

        def get_row_col(oned_indx):
            row = oned_indx // len(matrix[0])
            col = oned_indx % len(matrix[0])
            return (row, col)
        
        while left <= right:
            mid = (left + right) // 2
            row, col = get_row_col(mid)

            if row >= len(matrix):
                return False
            elif col >= len(matrix[0]):
                return False
            
            val = matrix[row][col]
            if target == val:
                return True
            elif target > val:
                # target too big, move right
                left = mid + 1
            elif target < val:
                # target too small, move left
                right = mid - 1

        return False