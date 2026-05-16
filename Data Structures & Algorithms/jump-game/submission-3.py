"""
Do not get confused, we are NOT jumping between indices otherwise we won't be
able to "go back" if we pick a wrong jump. Rather, we need to always ensure
that we can jump to the next index until we get to the end of the list.

This can be solved using DP and modeled with decision trees, but we don't need
overlapping sub-problems to figure out the result. We only need the local optimal
answer if we can reach the index at i.

We can be greedy and check the indices from i + nums[i] and choose the index
with the largest reach. This guarantees we're always picking the largest jump
length at all times.

Similar to Kadane's algorithm, we don't need to have an inner-loop to track the
"running best" for indices till i + nums[i]. We'll have a single running variable
that tracks all prior decision optimally.

We keep checking at index i, can we reach it? If we keep going for all i, then it
can reach the last index of the list.
"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0

        for i in range(len(nums)):
            if max_reach < i:
                # cannot reach at i, return False
                return False
            max_reach = max(max_reach, i + nums[i])

        # max_reach >= i held for all i, so every index was reachable
        return True