"""
There are 4 directions: right, down, left, up.

Solution with tracking indices, (O(N^2)) space using visited set:
Repeat this process without encountering already visited indices:
1. If we arrive at dead-end when moving right, move down.
2. If we arrive at dead-end when moving down, move left.
3. If we arrive at dead-end when moving left, move up.
4. If we arrive at dead-end when moving up, move right.

Solution with shrinking indices, O(1) space:
Same process as above, but shrink the bounds. We shrink bounds as
we encounter a dead-end on the side we just moved along:
1. If we arrive at dead-end when moving right, shrink top_bound += 1, move down.
2. If we arrive at dead-end when moving down, shrink right_bound -= 1, move left.
3. If we arrive at dead-end when moving left, shrink bottom_bound -= 1, move up.
4. If we arrive at dead-end when moving up, shrink left_bound += 1, move right.
"""
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top_bound = 0
        right_bound = len(matrix[0])
        bottom_bound = len(matrix)
        left_bound = 0

        result = []
        while top_bound < bottom_bound and left_bound < right_bound:
            # move right
            for i in range(left_bound, right_bound):
                result.append(matrix[top_bound][i])
            top_bound += 1
            
            # move down
            for i in range(top_bound, bottom_bound):
                result.append(matrix[i][right_bound - 1])
            right_bound -= 1

            # move left
            if top_bound < bottom_bound:
                for i in range(right_bound - 1, left_bound - 1, -1):
                    result.append(matrix[bottom_bound - 1][i])
                bottom_bound -= 1
            
            # move up
            if left_bound < right_bound:
                for i in range(bottom_bound - 1, top_bound - 1, - 1):
                    result.append(matrix[i][left_bound])
                left_bound += 1

        return result
        