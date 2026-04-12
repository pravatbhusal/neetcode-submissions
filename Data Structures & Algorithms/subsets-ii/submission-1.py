class Solution:
    """
    This is a blend of the Subsets and Combination Sum II problem.
    Subsets because it's asking for the subsets, which is classic backtracking problem.
    Combination Sum II because we don't want to include duplicate indices.

    We solved subsets by deciding to keep i and not keep i.
    We solved Combination Sum II by sorting nums and then skipping the
    duplicate indices.
    """
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []

        # sort to make skipping the same number possible
        nums.sort()

        temp = []
        def helper(i):
            if i >= len(nums):
                # base case, add this subset
                result.append(temp.copy())
                return
            # decide to keep this number
            temp.append(nums[i])
            helper(i + 1)

            # decide not to keep this number
            temp.pop()

            # skip i if it's the same number (works because list is sorted)
            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            helper(i + 1)
            
        helper(0)
        return result