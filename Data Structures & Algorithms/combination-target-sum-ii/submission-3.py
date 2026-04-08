class Solution:
    """
    The difference between this question and combination sum #1 is that
    each element can be chosen "at most once" within a combination.

    In question #1, you can choice the element multiple times hence why
    we didn't increment i + 1 in that solution.

    However, in this solution, we must increment i + 1 to not re-use the
    same element more than once.

    Another constraint is that we cannot have the same combination list.
    Even if same number appears twice, cannot be same combination list.

    To not re-use the same number index, we need to skip the used indices.
    To make skipping possible, we can sort the candidates and skip every number
    that is the same as i. That way an index is used only ever once because
    we never re-use the same number of that i.
    """
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []

        # sort to make skipping the same number possible
        candidates.sort()

        temp = []
        def helper(i, diff):
            if diff == 0:
                # base case, found a combination sum
                result.append(temp.copy())
                return
            if i >= len(candidates) or diff < 0:
                # base case, not combination sum
                return
            # decide to keep num
            # increment i to not use the same number in the next recurse
            temp.append(candidates[i])
            helper(i + 1, diff - candidates[i])

            # decide to not keep num
            temp.pop()
            # skip i if it's the same number (works because list is sorted)
            while i + 1 < len(candidates) and candidates[i] == candidates[i + 1]:
                i += 1
            helper(i + 1, diff)
            
        helper(0, target)
        return result
