class Solution:
    """
    return "all possible" tells me this is recursive backtracking.
    we need to get every possible answer, hence it will be inefficient.
    """

    """
    recursive backtracking solution:
    At each step, you decide: include this number or skip it.

    Example: nums = [1, 2, 3]

    Recursive backtracking would append each sublist in this order:
    [1, 2, 3]
    [1, 2]
    [1, 3]
    [1]
    [2, 3]
    [2]
    [3]
    []
    """
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        temp = []
        def recurse(i):
            if i >= len(nums):
                # base case, add sublist
                result.append(temp.copy())
                return
            # decide to keep the number at i
            temp.append(nums[i])
            recurse(i + 1)
            # decide not to keep the number at i
            temp.pop()
            recurse(i + 1)
        
        recurse(0)
        return result

        