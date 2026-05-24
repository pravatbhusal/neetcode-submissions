"""
Merge operation intuition is that if we merge triplets[i] and triplets[j],
then update the triplets[j] list to the max of the elements in the two lists.

Recursive-backtracking O(2^n) solution: Generate all possible subsets when merging
at index i. If operation fails to equal target, backtrack the merge.

Greedy solution: Very simple solution! Check each index 0, 1, 2 of target and check
each triplets index 0, 1, 2 to see if there is a value that equals index of target.
To short-circuit a triplet, if any index in a triplet is greater than target then
skip checking that because it's impossible to use that triplet to equal target.
"""
class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        found = set()

        for triplet in triplets:
            # short-circuit, this triplet index is larger than target
            if triplet[0] > target[0] or triplet[1] > target[1] or triplet[2] > target[2]:
                continue
            
            # check if this triplet's index equals target index
            for i, value in enumerate(target):
                if value == triplet[i]:
                    found.add(i)

        return len(found) == 3