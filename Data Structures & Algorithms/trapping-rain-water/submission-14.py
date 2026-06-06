"""
Keep track of the tallest heights on left-side and right-side to maximize the area of water at i.

To get maximal water area at i, compute the tallest wall to my left (max_left) and
what's the tallest wall to my right (max_left)? Then maximal water at i would
be the water trapped (min of max_left and max_right) minus the "space" at i.

Max water at i = max(0, min(max_left, max_right) - height[i])

The hard-part is the condition when to move left and right ptr. We move the
ptr that is smaller so that we keep the maximal ptr on the other side.
This guarantees that whichever side we calculate, the OTHER side's wall is
already tall enough.

For an O(N) solution, the problem space is split in two halves: left and right.
The max_left is the max height so far on the left-side (left ptr).
The max_right is the max height so far on the right-side (right ptr).

When we process left-side, max water at i collapses to: max_left - height[left]
When we process right-side, max water at i collapses to: max_right - height[right]
"""
class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        max_left, max_right = height[left], height[right]

        sum = 0
        while left < right:
            if max_left < max_right:
                # keep taller right-side height, so move left ptr
                left += 1
                # running sum from left-side
                max_left = max(height[left], max_left)
                sum += max_left - height[left]
            else:
                # keep taller left-side height, so move right ptr
                right -= 1
                # running sum from right-side
                max_right = max(height[right], max_right)
                sum += max_right - height[right]

        return sum
