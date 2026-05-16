"""
Similar to "Jump Game", but in this problem we're minimizing the number of jumps.

From Jump Game I: Greedily get the max reach at each index i, which lets us pick the
jump that would skip the most indices. By maximally skipping, we minimize # of jumps.

But we must also keep a window to tell us when we reach the end of our jump.
We can use a jump end variable to track the end of the window.

Lastly, if at the end of the list our max reach is larger than len(nums), we
may be off-by-one. To prevent this, we terminate incrementing jumps before
the end of the list.
"""
class Solution:
    def jump(self, nums: List[int]) -> int:
        max_reach = 0
        jump_end = 0
        jumps = 0

        for i in range(len(nums) - 1):
            max_reach = max(max_reach, i + nums[i])
            if jump_end == i:
                # reached the end of this jump
                jumps += 1
                # start new jump
                jump_end = max_reach

        return jumps