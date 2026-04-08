class Solution:
    """
    Problem says "list of all unique combinations", which hints to recursive backtracking.
    This requires brute-forcing all possibilities.

    Recursive backtracking Solution:
    Option 1) Keep nums[i]
    Option 2) Do not keep nums[i]
    Base case) We can keep subtracting from target until diff == 0.

    We also need to consider the possibility of using nums[i] multiple times.    
    To do this, do not increment i + 1 when we keep the number.
    This will use the number again in the next call stack.
    """
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []

        temp = []
        def helper(i, diff):
            if diff == 0:
                # base case, found a combination sum
                result.append(temp.copy())
                return
            if i >= len(nums) or diff < 0:
                # base case, not combination sum
                return
            # decide to keep num
            # do not increment i to use the same number in the next recurse
            temp.append(nums[i])
            helper(i, diff - nums[i])
            # decide to not keep num
            temp.pop()
            helper(i + 1, diff)
            
        helper(0, target)
        return result
