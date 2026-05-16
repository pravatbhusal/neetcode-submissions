"""
We can be greedy and check the indices from i + nums[i] and jump to the index
with the largest value. This guarantees we're always picking the largest jump
length at all times.

Similar to Kadane's algorithm, we don't need to have an inner-loop to track the
"running best" for indices till i + nums[i]. We'll have a single running variable
that tracks all prior decision optimally.
"""
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0

        for i in range(len(nums)):
            if max_reach < i:
                # dead state, return False
                return False
            max_reach = max(max_reach, i + nums[i])
        return True