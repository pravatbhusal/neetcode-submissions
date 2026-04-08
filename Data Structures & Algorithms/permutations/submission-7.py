class Solution:
    """
    This problem looks like Combination Sum I. However, the recursive backtracking
    solution is very different because this is solved through recursively building
    subproblems. Similar to a DP "bottom up" solution.

    Subproblem "bottom up" Solution:
    Example: nums = [1, 2, 3]
    1. Permutations of empty = [[]]
    2. Permutations of [3] = [[3]]
    3. Permutations of [2, 3] = [[2, 3], [3, 2]]
    4. Permutations of [1, 2, 3] = [[3,2,1],[2,3,1],[1,3,2],[3,1,2],[2,1,3],[1,2,3]]

    The subproblem solution adds nums[0] at each index of the previous
    recursive call's permutations.
    """
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return [[]]

        result = []

        # get permutations of subproblem
        permutations = self.permute(nums[1:])

        for p in permutations:
            # append nums[0] at each index of the subproblem's permutations
            # Ex: p = [3], nums[0] = 2 --> result = [2, 3] and [3, 2]
            for i in range(len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(i, nums[0])
                result.append(p_copy)
        
        return result
            