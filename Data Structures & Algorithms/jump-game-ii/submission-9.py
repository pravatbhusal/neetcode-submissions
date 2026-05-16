"""
Similar to "Jump Game", but in this problem we're minimizing the number of jumps.
Unlike Jump Game I, there is always a valid answer to the last index.

We can greedily get the max reach at each index i, which lets us pick the jump
that would skip the most indices. By maximally skipping, we minimize # of jumps.

But we must also keep a counter to tell us the number of jumps we took.
"""
class Solution:
    def jump(self, nums: List[int]) -> int:
        max_reach = 0
        jump_end = 0
        jumps = 0

        for i in range(len(nums) - 1):  # Fix 1: stop before last index
            max_reach = max(max_reach, i + nums[i])  # Fix 2: update reach first
            if jump_end == i:
                jumps += 1
                jump_end = max_reach

        return jumps