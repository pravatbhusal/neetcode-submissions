"""
nums --> longest length.
we are looking for a "subsequence", which tells me we have sub-prpblems.

subsequence: a sub-set from a sequence where i can delete an element
and the list is still the same "order". order means the list is sorted.

Ex: nums = [9, 1, 4, 2, 3, 3, 7]
If I delete 9, 4, 3 the list is now sorted: [1, 2, 3, 7]
The length of that list is 4.

The problem is asking how many numbers can we delete from nums
to make the list sorted.

This can be solved using recursive backtracking, which becomes a Decision Tree.
This is because we need to try every possible combination of what we can delete.

How can we optimize the recursive backtracking? By memoizing!
We memoize each decision so that if we know deleting that number
doesn't sort the list then we know next time in the recursive stack
if we're at that index we do not delete it.
"""
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sys.setrecursionlimit(10000)
        dp = {}
        temp = []

        def helper(i, prev):
            if (i, prev) in dp:
                return dp[(i, prev)]
            if i == len(nums):
                # base case, this sub-problem is sorted ascending
                return 0
            
            # keep this number
            result = 0
            if nums[i] > prev: # verify keeping num makes sub-array stay sorted
                result = 1 + helper(i + 1, nums[i])
            # do not include this num
            result = max(result, helper(i + 1, prev))
            dp[(i, prev)] = result
            return result

        return helper(0, -math.inf)
        